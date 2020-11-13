import pymysql
#清空表数据
def clean_table():
    conn = pymysql.connect(host="47.115.148.142", user="root", password="hht*LSL520", db="datafrom_hive", charset="utf8")
    mycursor = conn.cursor()
    print("开始清表操作......")
    sql1 = "truncate table china_new_out" ## 清空
    sql2 = "truncate table china_sunconfirm_l3" ## 清空
    sql3 = "truncate table global_center" ## 清空
    sql4 = "truncate table global_city_top" ## 清空
    sql5 = "truncate table global_coutry_top" ## 清空
    sql6 = "truncate table global_new_out"  ## 清空
    sql7 = "truncate table global_plate"  ## 清空
    sql8 = "truncate table global_sunconfirm_l3"  ## 清空
    sql9 = "truncate table china_c1"  ## 清空
    sql10 = "truncate table china_c2"  ## 清空
    sql11 = "truncate table china_l1"  ## 清空
    sql12 = "truncate table china_l2"  ## 清空
    sql13 = "truncate table china_l3"  ## 清空
    #sql6 = "truncate table hotsearch" ## 清空
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    mycursor.execute(sql3)
    mycursor.execute(sql4)
    mycursor.execute(sql5)
    mycursor.execute(sql6)
    mycursor.execute(sql7)
    mycursor.execute(sql8)
    mycursor.execute(sql9)
    mycursor.execute(sql10)
    mycursor.execute(sql11)
    mycursor.execute(sql12)
    mycursor.execute(sql13)
    #mycursor.execute(sql6)
    conn.commit()
    conn.close()
    print("清表操作完成......")

if __name__ == "__main__":
    clean_table()