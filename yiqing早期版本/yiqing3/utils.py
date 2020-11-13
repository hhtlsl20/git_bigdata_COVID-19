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
                           charset="utf8")
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


def get_c1_data():
    """
    :return: 返回大屏的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select * from global_center"
    res = query(sql)
    return res

def get_l1_data():
  sql1 = "select * from global_coutry_top"
  res1 = query(sql1)
  sql2 = "select * from global_city_top"
  res2 = query(sql2)
  return res1,res2

def get_l2_data():
  sql1 = "select * from china_new_out"
  res1 = query(sql1)
  sql2 = "select * from global_new_out"
  res2 = query(sql2)
  return res1,res2

def get_l3_data():
  sql1 = "select confirm,heal,dead from china_sunconfirm_l3"
  res1 = query(sql1)
  sql2 = "select confirm,heal,dead from global_sunconfirm_l3"
  res2 = query(sql2)
  return res1,res2


#返回板块各州统计
def get_r1_data():
    sql = "select * from global_plate"
    res = query(sql)
    return res

#历史数据
def get_r2_data():
    sql1 = "SELECT ds,confirm,heal,dead from chinahistory"
    res1 = query(sql1)
    sql2 = "select ds,confirm,heal,dead from globalhistory"
    res2 = query(sql2)
    return res1, res2

#返回最近的20条热搜
def get_r3_data():
    sql = 'select content from hotsearch order by id desc limit 14'
    res = query(sql)  # 格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    return res


# if __name__ == "__main__":
# 	print(get_r2_data())


