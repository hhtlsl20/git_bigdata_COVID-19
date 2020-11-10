import time
import pymysql


def get_time():
    time_str =  time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")     #因为直接写不支持直接识别中文，才用format写


#return: 连接，游标
def get_conn():
    # 创建连接
    conn = pymysql.connect(host="8.129.42.178",
                           user="hht",
                           password="hhtLSL520!",
                           db="yq",
                           charset="utf8mb4")
    # 创建游标
    cursor = conn.cursor()# 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

###  中英文转换
# 读入一个国家名称的中英映射文件，用于中英转化。
import json
with open('static/json/name_map.json','r',encoding='utf-8') as json_file:
    # json.dump()和json.load()用于读写。 dumps()和loads()用于dict和json的转换
    name_map = json.load(json_file)
# 键值互换,看自己转换方向
name_map = dict(zip(name_map.values(),name_map.keys()))


def get_c1_data():
    """
    :return: 返回大屏的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select sum(confirm),sum(heal),sum(dead),sum(nowConfirm) from globaldata"
    res = query(sql)
    return res

def get_c2_data(country):
    country = name_map.get(country)
    if(country == '日本'):
        country = country+"本土"
    sql1 = "select namemap,confirm from detailsusa where name = " +country +" and namemap != ''"
    res1 = query(sql1)
    return res1

def get_map_data():
    sql = "SELECT name,confirm from globaldata"
    res = query(sql)
    return res

def get_l1_data():
  sql1 = "SELECT name,confirm FROM (select * from globaldata order by confirm desc limit 5) aa ORDER BY name asc"
  res1 = query(sql1)
  sql2 = "SELECT city,confirm FROM (select * from detailsusa order by confirm desc limit 5) aa ORDER BY city asc"
  res2 = query(sql2)
  return res1,res2

def get_l2_data():
  sql1 = "SELECT ds,confirm_add,heal_add,dead_add FROM (select * from chinahistory order by ds desc limit 30) aa ORDER BY ds asc"
  res1 = query(sql1)
  sql2 = "SELECT ds,newAddConfirm,heal_add,dead_add FROM (select * from globalhistory order by ds desc limit 30) aa ORDER BY ds asc"
  res2 = query(sql2)
  return res1,res2

def get_l3_data():
  sql1 = "select confirm,heal,dead from chinahistory  ORDER BY ds desc limit 1"
  res1 = query(sql1)
  sql2 = "select sum(confirm),sum(heal),sum(dead) from globaldata"
  res2 = query(sql2)
  return res1,res2


#返回板块各州统计
def get_r1_data():
    sql = "select continent,sum(confirm) as all_confirm ,sum(heal) as all_heal ,sum(dead) as all_dead from globaldata where continent !='' and continent !='其他' group by continent"
    res = query(sql)
    return res

#历史数据
def get_r2_data():
    sql1 = "SELECT * FROM (SELECT ds,confirm,heal,dead from chinahistory order by ds desc limit 15) aa ORDER BY ds asc"
    res1 = query(sql1)
    sql2 = "SELECT * FROM (SELECT ds,confirm,heal,dead from globalhistory order by ds desc limit 15) aa ORDER BY ds asc;"
    res2 = query(sql2)
    return res1, res2

#返回最近的20条热搜
def get_r3_data():
    sql = 'select content from hotsearch order by id desc limit 14'
    res = query(sql)  # 格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    return res


# if __name__ == "__main__":
# 	print(get_r2_data())


