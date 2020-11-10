# -*- coding: utf-8 -*-
import requests,random,re
import time
import sys
import pymysql
import traceback
import importlib
from fake_useragent import UserAgent

importlib.reload(sys)
startTime = time.time() #记录起始时间


#设置heades
headers = {
    'Cookie': '_T_WM=22822641575; H5_wentry=H5; backURL=https%3A%2F%2Fm.weibo.cn%2F; ALF=1584226439; MLOGIN=1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5RJaVYrb.BEuOvUQ8Ca2OO5JpX5K-hUgL.FoqESh-7eKzpShM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMceoBfeh2EeKBN; SCF=AnRSOFp6QbWzfH1BqL4HB8my8eWNC5C33KhDq4Ko43RUIzs6rjJC49kIvz5_RcOJV2pVAQKvK2UbAd1Uh6j0pyo.; SUB=_2A25zQaQBDeRhGeBM71cR8SzNzzuIHXVQzcxJrDV6PUJbktAKLXD-kW1NRPYJXhsrLRnku_WvhsXi81eY0FM2oTtt; SUHB=0mxU9Kb_Ce6s6S; SSOLoginState=1581634641; WEIBOCN_FROM=1110106030; XSRF-TOKEN=dc7c27; M_WEIBOCN_PARAMS=oid%3D4471980021481431%26luicode%3D20000061%26lfid%3D4471980021481431%26uicode%3D20000061%26fid%3D4471980021481431',
    'Referer': 'https://m.weibo.cn/detail/4312409864846621',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

#临时存放数据列表
weibo_title_data = []
weibo_user_data = []

#-----------------------------------爬取战疫情首页的每个主题的ID------------------------------------------
comments_ID = []
def get_title_id():
    for page in range(1,21):  #每个页面大约有18个话题
        headers = {
            "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
        }
        time.sleep(1)
        #该链接通过抓包获得
        api_url = 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_600059_-_ctg1_600059&page=' + str(page)
        print(api_url)
        rep = requests.get(url=api_url, headers=headers)
        #获取ID值并写入列表comment_ID中
        for json in rep.json()['data']['statuses']:
            comment_ID = json['id'] 
            comments_ID.append(comment_ID)

#-----------------------------------爬取战疫情每个主题的详情页面------------------------------------------         
def spider_title(comment_ID):
    try:
        article_url = 'https://m.weibo.cn/detail/'+ comment_ID
        print ("article_url = ", article_url)
        html_text = requests.get(url=article_url, headers=headers).text
        #话题内容
        find_title = re.findall('.*?"text": "(.*?)",.*?', html_text)[0]
        title_text = re.sub('<(S*?)[^>]*>.*?|<.*? />', '', find_title) #正则匹配掉html标签
        print ("title_text = ", title_text)
        #楼主ID
        title_user_id = re.findall('.*?"id": (.*?),.*?', html_text)[1]
        print ("title_user_id = ", title_user_id)
        #楼主昵称
        title_user_NicName = re.findall('.*?"screen_name": "(.*?)",.*?', html_text)[0]
        print ("title_user_NicName = ", title_user_NicName)
        #楼主性别
        title_user_gender = re.findall('.*?"gender": "(.*?)",.*?', html_text)[0]
        print ("title_user_gender = ", title_user_gender)
        #发布时间
        created_title_time = re.findall('.*?"created_at": "(.*?)".*?', html_text)[0].split(' ')
        #日期
        if 'Mar' in created_title_time:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '03', created_title_time[2])
        elif 'Feb' in created_title_time:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '02', created_title_time[2])
        elif 'Jan' in created_title_time:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '01', created_title_time[2])
        elif 'Apr' in created_title_time:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '04', created_title_time[2])
        elif 'May' in created_title_time:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '05', created_title_time[2])
        else:
            title_created_YMD = "{}/{}/{}".format(created_title_time[-1], '00', created_title_time[2])
        
        print ("title_created_YMD = ", title_created_YMD)
        #发布时间
        add_title_time = created_title_time[3]
        print ("add_title_time = ", add_title_time)
        #转发量
        reposts_count = re.findall('.*?"reposts_count": (.*?),.*?', html_text)[0]
        print ("reposts_count = ", reposts_count)
        #评论量
        comments_count = re.findall('.*?"comments_count": (.*?),.*?', html_text)[0]
        print ("comments_count = ", comments_count)
        #点赞量
        attitudes_count = re.findall('.*?"attitudes_count": (.*?),.*?', html_text)[0]
        print ("attitudes_count = ", attitudes_count)   
        comment_count = int(int(comments_count) / 20) #每个ajax一次加载20条数据
        #写入列表
        weibo_title_data.append(
            [article_url, title_text, title_user_id, title_user_NicName, title_user_gender, title_created_YMD,
             add_title_time, reposts_count, comments_count, attitudes_count])
        return comment_count
    except:
        pass


#-------------------------------------------------抓取评论信息---------------------------------------------------
#comment_ID话题编号
def get_page(comment_ID, max_id, id_type):
    params = {
        'max_id': max_id,
        'max_id_type': id_type
    }
    url = ' https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id'.format(comment_ID, comment_ID)
    try:
        r = requests.get(url, params=params, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print('error', e.args)
        pass

#-------------------------------------------------抓取评论item最大值---------------------------------------------------
def parse_page(jsondata):
    if jsondata:
        items = jsondata.get('data')
        item_max_id = {}
        item_max_id['max_id'] = items['max_id']
        item_max_id['max_id_type'] = items['max_id_type']
        return item_max_id

#-------------------------------------------------抓取评论信息---------------------------------------------------
def write_user(jsondata):
    for json in jsondata['data']['data']:
        #用户ID
        user_id = json['user']['id']
        # 用户昵称
        user_name = json['user']['screen_name']
        # 用户性别,m表示男性，表示女性
        user_gender = json['user']['gender']
        #获取评论
        comments_text = json['text']
        comment_text = re.sub('<(S*?)[^>]*>.*?|<.*? />', '', comments_text) #正则匹配掉html标签
        # 评论时间
        created_times = json['created_at'].split(' ')
        if 'Feb' in created_times:
            created_YMD = "{}/{}/{}".format(created_times[-1], '02', created_times[2])
        elif 'Jan' in created_times:
            created_YMD = "{}/{}/{}".format(created_times[-1], '01', created_times[2])
        elif 'Mar' in created_times:
            created_YMD = "{}/{}/{}".format(created_times[-1], '03', created_times[2])
        elif 'Apr' in created_times:
            created_YMD = "{}/{}/{}".format(created_times[-1], '04', created_times[2])
        elif 'May' in created_times:
            created_YMD = "{}/{}/{}".format(created_times[-1], '05', created_times[2])
        else:
            created_YMD = "{}/{}/{}".format(created_times[-1], '00', created_times[2])
        created_time = created_times[3] #评论时间时分秒
        #写入列表
        weibo_user_data.append([user_id, user_name, user_gender, created_YMD, created_time, comment_text])


def get_conn():
	#建立连接
	conn = pymysql.connect(host="192.168.198.13", user="root", password="Xiaoi@123456", db="yq", charset="utf8mb4")
	#创建游标
	cursor = conn.cursor()
	return conn,cursor

def close_conn(conn,cursor):
	if cursor:
		cursor.close()
	if conn:
		conn.close()

#插入weibo_spider数据
def update_weibo_spider():
	cursor = None
	conn = None
	try:
		li = weibo_title_data   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into weibo_spider(article_url,title_text,title_user_id,title_user_NicName,title_user_gender,title_created_YMD,add_title_time,reposts_count,comments_count,attitudes_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		for item in li:
			cursor.execute(sql,item)
		conn.commit()
		print(f"{time.asctime()}主题内容更新到最新数据")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#插入weibo_user_spider数据
def update_weibo_user_spider():
	cursor = None
	conn = None
	try:
		li = weibo_user_data   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into weibo_user_spider(user_id, user_name, user_gender, created_YMD, created_time, comment_text) values (%s,%s,%s,%s,%s,%s)"
		for item in li:
			cursor.execute(sql,item)
		conn.commit()
		print(f"{time.asctime()}评论者更新到最新数据")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#清空表数据
def clean_table():
    conn = pymysql.connect(host="192.168.198.13", user="root", password="Xiaoi@123456", db="yq", charset="utf8mb4")
    mycursor = conn.cursor()
    sql1 = "truncate table weibo_spider" ## 清空
    sql2 = "truncate table weibo_user_spider" ## 清空
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    conn.commit()
    conn.close()
    print("清表操作完成......")



#-------------------------------------------------主函数---------------------------------------------------
def main():
    count_title = len(comments_ID)
    for count, comment_ID in enumerate(comments_ID):
        print ("正在爬取第%s个话题，一共找到个%s话题需要爬取"%(count+1, count_title))
        time.sleep(random.randint(1000,2000)/1000.0)
        #maxPage获取返回的最大评论数量
        maxPage = spider_title(comment_ID)
        print ('maxPage = ', maxPage)
        m_id = 0
        id_type = 0
        if maxPage != 0: #小于20条评论的不需要循环
            try:
                #用评论数量控制循环
                for page in range(0, maxPage):
                    #自定义函数-抓取网页评论信息
                    jsondata = get_page(comment_ID, m_id, id_type)
                    
                    #自定义函数-写入列表
                    write_user(jsondata)
                    
                    #自定义函数-获取评论item最大值
                    results = parse_page(jsondata)
                    time.sleep(1)
                    m_id = results['max_id']
                    id_type = results['max_id_type']              
            except:
                pass
        print ("--------------------------分隔符---------------------------")

    
if __name__ == '__main__':
    clean_table()
    #获取话题ID
    get_title_id()
    
    #主函数操作
    main()
    update_weibo_spider()
    update_weibo_user_spider()
    #计算使用时间
    endTime = time.time()
    useTime = (endTime-startTime) / 60
    print("该次所获的信息一共使用%s分钟"%useTime)
