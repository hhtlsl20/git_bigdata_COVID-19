import time
import pymysql
import traceback

def get_time():
    time_str =time.strftime("%Y {}%m{}%d{} %X")
    return  time_str.format("年","月","日")

def connection():
    cursor=None
    connect = None
    #连接服务器数据库:
    connect = pymysql.connect(host="8.129.42.178", user="hht", password="hhtLSL520!", db="yq")
    cursor = connect.cursor()
    return connect,cursor
def close(connect,cursor):
    if cursor:
        cursor.close()
    elif connect:
        connect.close()
def get(sql,*args):
    try:
        connect,cursor=connection()
        cursor.execute(sql,args)
        row = cursor.fetchall()
    except:
        traceback.print_exc()
    finally:
        close(connect, cursor)
    return row



def get_c1_data():
    sql="select confirm," \
          "heal, " \
          "dead," \
          "suspect " \
          "from chinahistory "\
          "where ds=(select ds from chinahistory order by ds desc limit 1)"
    row = get(sql)
    return row[0]

def get_c2_data():
    sql = "SELECT province ,SUM(confirm-heal) from details group by province"
    row = get(sql)
    return row


def get_l1_data():
  sql = "select ds,confirm,heal,dead,suspect from chinahistory"
  row = get(sql)
  return row

def get_l2_data():

  sql = "select ds,confirm_add,suspect_add from chinahistory"
  row = get(sql)
  return row

#返回非湖北地区城市确诊人数前5名
def get_r1_data():

    sql = 'SELECT city,confirm FROM ' \
          '(select city,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆","香港","台湾") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆","香港","台湾") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = get(sql)
    return res

#返回疫情数据播报信息
# def get_r2_data():
#     sql = 'SELECT tip FROM details WHERE tip !='' GROUP BY tip;'
#     res = get(sql)
#     return res


def get_test_data():
    sql="select confirm,heal,dead from chinahistory  where ds=(select ds from chinahistory order by ds desc limit 1) "
    row = get(sql)
    return row[0]
def get_l3_data():
    sql="select sum(heal_add),sum(dead_add) from chinahistory group by MONTH (ds)"
    row = get(sql)
    return row
def get_r3_data():
    sql="select heal_add,dead_add,confirm_add from chinahistory where ds=(select ds from chinahistory order by ds desc limit 1)"
    row=get(sql)
    return row
def get_guizhou_data(privince):
    base_sql='select city,confirm from details where province ='+'"'+privince+'"'
    sql=base_sql
    # row=get(sql)
    # sql="select city,confirm from details where province ='贵州'"
    row=get(sql)
    return row

def get_gz_l1(privince):
    # sql='SELECT confirm,city FROM details WHERE province ="贵州"'
    base_sql='SELECT confirm,city FROM details WHERE province ='+'"'+privince+'"'
    sql = base_sql
    row=get(sql)
    return  row[0:10]
def get_all_l2(province):
    base_sql='SELECT content,counts FROM hotissues WHERE province='+'"'+province+'"'
    sql=base_sql
    row=get(sql)
    return row
# def get_xinjiang_data():
#     sql='SELECT confirm,city FROM details WHERE province="新疆"'
#     row=get(sql)
#     return row
# if __name__ == "__main__":
#     print(get_test_data())
