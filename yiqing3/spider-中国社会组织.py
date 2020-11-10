import requests, sys, time
from lxml import html
import random
from fake_useragent import UserAgent
import pymysql
import traceback

# 记录起始时间
startTime = time.time()

# 创建CSV文件，并写入表头信息
china_zuzhi_data = []

#----------------------------------------------抓取数据----------------------------------------------
def spider_html_info(url):
    time.sleep(random.randint(1000,2000)/1000.0)
    try:
        headers = {
            "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
        }
        response = requests.get(url=url, headers=headers).text
        text_html = html.fromstring(response)
        
        # 获取下一页链接,先其他元素获取一页链接，保证程序的强壮性
        next_url = "http://www.chinanpo.gov.cn" + text_html.xpath('/html/body/div[2]/div/ul[1]/li[2]/a[2]/@href')[0]
        print("next_url", next_url)
    
        # 获取文章标题
        article_title = text_html.xpath('//*[@id="fontinfo"]/p[2]/b[1]//text()')
        title = "".join(article_title)
        if title == "":
            title = "".join(text_html.xpath('//*[@id="fontinfo"]/p[3]/b[1]//text()'))
        print ("title = ",title)
        
        # 获取发布时间
        publish_time = text_html.xpath('/html/body/div[2]/div/ul[1]/li[3]/strong/text()')[0][5:]
        print ("publish_time = ", publish_time)
        print ("url = ", url)
        
        # 获取来源
        source_text = text_html.xpath('//*[@id="fontinfo"]/p[last()]//text()')[0]
        source = source_text[3:]
        
        # 爬取文本
        text_list = text_html.xpath('//*[@id="fontinfo"]//text()')
        article_text = "".join(text_list).replace('\r\n','').replace("\xa0", "").replace("\t", "").replace(source_text,"").replace(title, "")    

        china_zuzhi_data.append([title, publish_time, url, article_text, source])
    except:
        print("Error: url not found")
        pass
    
    if url == 'http://www.chinanpo.gov.cn/1944/123496/index.html':
        # 获取结束时的时间
        endTime =time.time()           
        useTime =(endTime-startTime)/60
        print ("该次所获的信息一共使用%s分钟"%useTime)
        # 正常退出程序
        sys.exit(0)       
    else:
        return next_url


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

#插入update_china_zuzhi_spider数据
def update_china_zuzhi_spider():
	cursor = None
	conn = None
	try:
		li = china_zuzhi_data   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into china_zuzhi_spider(title_name,title_created_YMD,title_url,title_text,title_from) values (%s,%s,%s,%s,%s)"
		for item in li:
			cursor.execute(sql,item)
		conn.commit()
		print(f"{time.asctime()}china_zuzhi_data内容更新到最新数据")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#清空表数据
def clean_zuzhi_table():
    conn = pymysql.connect(host="192.168.198.13", user="root", password="Xiaoi@123456", db="yq", charset="utf8mb4")
    mycursor = conn.cursor()
    sql1 = "truncate table china_zuzhi_spider" # 清空
    mycursor.execute(sql1)
    conn.commit()
    conn.close()
    print("清表操作完成......")



#----------------------------------------------主函数----------------------------------------------
def main():
    url = "http://www.chinanpo.gov.cn/1944/127178/index.html" # 125177第一篇文章
    count = 1
    while True:
        print ("正在爬取第%s篇："%count, url)
        next_url = spider_html_info(url)
        url = next_url
        count = count + 1
        if(count == 100):
            break
                
if __name__ == '__main__':
    clean_zuzhi_table()
    main()
    update_china_zuzhi_spider()
