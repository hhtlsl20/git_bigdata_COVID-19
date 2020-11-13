import requests
import json
import time
import pymysql
#from selenium.webdriver import Chrome,ChromeOptions
import traceback
import sys
#from selenium import webdriver
from lxml import etree

#返回历史数据和当日详细数据
def get_data():
    #url来自腾讯：https://news.qq.com//zt2020/page/feiyan.htm  ，F12找到js中Get方法的数据json的url
    #国内当日新增
    url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    #国内历史数据
    url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    #国外历史数据
    url3 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"
    #国外当日数据
    url4 = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    r1 = requests.get(url1, headers)
    time.sleep(1)
    r2 = requests.get(url2, headers)
    time.sleep(1)
    r3 = requests.get(url3, headers)
    time.sleep(1)
    r4 = requests.get(url4, headers)

    #json字符串转字典
    r1 = json.loads(r1.text)
    r2 = json.loads(r2.text)
    r3 = json.loads(r3.text)
    r4 = json.loads(r4.text)
    #print(r1)
    data_all1 = json.loads(r1["data"])
    data_all2 = json.loads(r2["data"])
    data_all3 = json.loads(r3["data"])

    #print(data_all3['foreignList'][3])
    #print(data_all3)
    #print(data_all2["provinceCompare"]['上海'])
    #print("-----"*30)
    #print(data_all2["chinaDayList"])

    #国内历史数据
    chinahistory = {}
    for i in data_all2["chinaDayList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  #改变时间输入格式，不然插入数据库会报错，数据库是datatime格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        chinahistory[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_all2["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  #数据库datatime格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        chinahistory[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})
    #print(chinahistory)

    #全球历史数据
    globalhistory = {}
    for i in data_all3["globalDailyHistory"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  #数据库datatime格式
        confirm = i["all"]["confirm"]
        newAddConfirm = i["all"]["newAddConfirm"]
        heal = i["all"]["heal"]
        dead = i["all"]["dead"]
        globalhistory[ds] = {"confirm": confirm, "newAddConfirm": newAddConfirm, "heal": heal, "dead": dead}
    for i in data_all3["globalDailyHistory"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  #数据库datatime格式
        confirm = i["all"]["confirm"]
        newAddConfirm = i["all"]["newAddConfirm"]
        heal = i["all"]["heal"]
        dead = i["all"]["dead"]
        globalhistory[ds].update({"confirm_add": confirm, "newAddConfirm": newAddConfirm, "heal_add": heal, "dead_add": dead})
    #print(globalhistory)

    #国内当日详细数据，这里默认为境外输入，当前编写时间为4月24日，主要来自境外
    details = []
    update_time = data_all1["lastUpdateTime"]
    data_country = data_all1["areaTree"]  #list 25个国家
    data_province = data_country[0]["children"] #中国各省
    for pro_infos in data_province:
        province = pro_infos["name"] #省名
        tip = pro_infos["today"]["tip"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            #新增
            deadrate = city_infos["total"]["deadRate"]
            healrate = city_infos["total"]["healRate"]
            #tips = city_infos["today"]["tip"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead,healrate,deadrate,tip])
    #print("国内每日数据"*10)
    #print(details)

    #美国各州当日详细数据
    detailsusa = []
    #update_time = data_all3["lastUpdateTime"]  #此json里没有这个列
    data_province = data_all3['foreignList'][0]['children']
    for city_infos in data_province:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        update_time = time.strftime("%Y-%m-%d", tup)  #数据库datatime格式
        city = city_infos["name"]
        namemap = city_infos["nameMap"]
        confirm = city_infos["confirm"]
        confirm_add = city_infos["confirmAdd"]
        heal = city_infos["heal"]
        dead = city_infos["dead"]
        detailsusa.append([update_time,city,namemap, confirm, confirm_add, heal, dead])
    #

    #全球当日详细数据
    globaldata = []
    for i in r4["data"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        update_time = time.strftime("%Y-%m-%d", tup)  #数据库datatime格式
        name = i['name']
        continent = i['continent']
        confirmAdd = i['confirmAdd']
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        nowConfirm = i['nowConfirm']
        globaldata.append([update_time,name,continent,confirmAdd,confirm,suspect,heal,dead,nowConfirm])
    #print(globaldata)


    return chinahistory,globalhistory,details,globaldata,detailsusa


def get_conn():
	#建立连接
	conn = pymysql.connect(host="47.115.148.142", user="root", password="hht*LSL520", db="yq", charset="utf8")
	#创建游标
	cursor = conn.cursor()
	return conn,cursor

def close_conn(conn,cursor):
	if cursor:
		cursor.close()
	if conn:
		conn.close()


#插入detailsusa数据
def update_detailsusa():
	cursor = None
	conn = None
	try:   
		li = get_data()[4]   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into detailsusa(update_time,city,namemap, confirm, confirm_add, heal, dead) values(%s,%s,%s,%s,%s,%s,%s)"
		sql_query = "select %s=(select update_time from details order by id desc limit 1)"  #对比当前最大时间戳
		#对比当前最大时间戳
		cursor.execute(sql_query,li[0][0])
		if not cursor.fetchone()[0]:
			print(f"{time.asctime()}开始更新数据")
			for item in li:
				cursor.execute(sql,item)
			conn.commit()
			print(f"{time.asctime()}更新到最新数据")
		else:
			print(f"{time.asctime()}已是最新数据！")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#插入globaldata数据
def update_globaldata():
	cursor = None
	conn = None
	try:   
		li = get_data()[3]   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into globaldata(update_time,name,continent,confirmAdd,confirm,suspect,heal,dead,nowConfirm) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		sql_query = "select %s=(select update_time from details order by id desc limit 1)"  #对比当前最大时间戳
		#对比当前最大时间戳
		cursor.execute(sql_query,li[0][0])
		if not cursor.fetchone()[0]:
			print(f"{time.asctime()}开始更新数据")
			for item in li:
				cursor.execute(sql,item)
			conn.commit()
			print(f"{time.asctime()}更新到最新数据")
		else:
			print(f"{time.asctime()}已是最新数据！")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#插入details数据
def update_details():
	cursor = None
	conn = None
	try:   
		li = get_data()[2]   #返回的数据
		conn,cursor = get_conn()
		sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead,healrate,deadrate,tip) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		sql_query = "select %s=(select update_time from details order by id desc limit 1)"  #对比当前最大时间戳
		#对比当前最大时间戳
		cursor.execute(sql_query,li[0][0])
		if not cursor.fetchone()[0]:
			print(f"{time.asctime()}开始更新数据")
			for item in li:
				cursor.execute(sql,item)
			conn.commit()
			print(f"{time.asctime()}更新到最新数据")
		else:
			print(f"{time.asctime()}已是最新数据！")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)


#插入chinahistory数据
def insert_chinahistory():
    cursor = None
    conn = None
    try:
        dic = get_data()[0]   #0代表历史数据字典
        print(f"{time.asctime()}开始插入历史数据")
        conn,cursor = get_conn()
        sql = "insert into chinahistory values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k,v in dic.items():
            cursor.execute(sql,[k, v.get("confirm"),v.get("confirm_add"),v.get("suspect"),
                           v.get("suspect_add"),v.get("heal"),v.get("heal_add"),
                           v.get("dead"),v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)


#更新国内历史数据
def update_chinahistory():
    cursor = None
    conn = None
    try:
        dic = get_data()[0]#0代表历史数据字典
        print(f"{time.asctime()}开始更新历史数据")
        conn,cursor = get_conn()
        sql = "insert into chinahistory values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from chinahistory where ds=%s"
        for k,v in dic.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k, v.get("confirm"),v.get("confirm_add"),v.get("suspect"),
                               v.get("suspect_add"),v.get("heal"),v.get("heal_add"),
                               v.get("dead"),v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

#插入globalhistory数据
def insert_globalhistory():
    cursor = None
    conn = None
    try:
        dic = get_data()[1]   #0代表历史数据字典
        print(f"{time.asctime()}开始插入历史数据")
        conn,cursor = get_conn()
        sql = "insert into globalhistory values (%s,%s,%s,%s,%s,%s,%s,%s)"
        for k,v in dic.items():
            cursor.execute(sql,[k, v.get("confirm"),v.get("newAddConfirm"),v.get("heal"),
                               v.get("dead"),v.get("confirm_add"),v.get("heal_add"),
                               v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

#更新全球历史数据
def update_globalhistory():
    cursor = None
    conn = None
    try:
        dic = get_data()[1]    #代表历史数据字典
        print(f"{time.asctime()}开始更新历史数据")
        conn,cursor = get_conn()
        sql = "insert into globalhistory values (%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from globalhistory where ds=%s"
        for k,v in dic.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k, v.get("confirm"),v.get("newAddConfirm"),v.get("heal"),
                               v.get("dead"),v.get("confirm_add"),v.get("heal_add"),
                               v.get("dead_add")])
        conn.commit()
        #{"confirm": confirm, "newAddConfirm": newAddConfirm, "heal": heal, "dead": dead}
        #{"confirm_add": confirm, "newAddConfirm": newAddConfirm, "heal_add": heal, "dead_add": dead}
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)



#返回百度疫情复工复课热搜
def get_baidu_hot():
	#option = ChromeOptions() #创建谷歌浏览器实例
	#option.add_argument("--headless")#隐藏浏览器
	#option.add_argument("--no-sandbox")  #禁用沙盘    部署在linux上访问chrome要求这样
	#url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
	#brower = Chrome(options = option)
	#brower.get(url)
	#找到展开按钮
    #driver_path = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
    driver_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1')
    #but = driver.find_element_by_xpath("//*[@id="ptab-0"]/div/div[1]/section/div") #定位到点击展开按钮
    #but.click() #点击展开
    time.sleep(2)#
    c = driver.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[2]/section/a/div/span[2]')
    context = [i.text for i in c]  #获取标签内容
    # 关闭浏览器窗口
    driver.close()
    print(context)
    return context

#将疫情复工复课热搜插入数据库
def update_hotsearch():
	cursor = None
	conn = None
	try:
		context = get_baidu_hot()
		print(f"{time.asctime()}开始更新热搜数据")
		conn, cursor = get_conn()
		sql = "insert into hotsearch(dt,content) values(%s,%s)" 
		ts = time.strftime("%Y-%m-%d %X")
		for i in context:
			cursor.execute(sql,(ts,i))  #插入数据
		conn.commit() #提交事务保存数据
		print(f"{time.asctime()}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

#清空表数据
def clean_table():
    conn = pymysql.connect(host="47.115.148.142", user="root", password="hht*LSL520", db="yq", charset="utf8")
    mycursor = conn.cursor()
    sql1 = "truncate table chinahistory" ## 清空
    sql2 = "truncate table details" ## 清空
    sql3 = "truncate table detailsusa" ## 清空
    sql4 = "truncate table globaldata" ## 清空
    sql5 = "truncate table globalhistory" ## 清空
    #sql6 = "truncate table hotsearch" ## 清空
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    mycursor.execute(sql3)
    mycursor.execute(sql4)
    mycursor.execute(sql5)
    #mycursor.execute(sql6)
    conn.commit()
    conn.close()
    print("清表操作完成......")


if __name__ == "__main__":
    #get_data()
    clean_table()
    update_detailsusa()
    update_globaldata()
    update_details()
    insert_chinahistory()
    insert_globalhistory()
    update_chinahistory()
    update_globalhistory()
    #在服务器端暂时不打开百度热搜，需要单独安装插件
    #update_hotsearch()



