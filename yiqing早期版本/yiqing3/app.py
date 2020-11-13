from flask import Flask
from flask import render_template
from flask import jsonify
import utils
import string



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    confirm,heal,dead,nowConfirm = [], [], [],[]
    for a,b,c,d in data:
        confirm.append(int(a))
        heal.append(int(b))
        dead.append(int(c))
        nowConfirm.append(int(d))
    return jsonify({"confirm": confirm, "heal": heal, "dead": dead ,"nowConfirm": nowConfirm})


#国家及城市排行
@app.route("/l1")
def get_l1_data():
    data1,data2 = utils.get_l1_data()
    name,name_confirm,city,city_confirm = [],[],[],[]
    for a,b in data1:
        name.append(a)
        name_confirm.append(int(b))
    for c,d in data2:
        city.append(c)
        city_confirm.append(int(d))
    return jsonify({"name":name,"name_confirm": name_confirm, "city": city, "city_confirm": city_confirm})

#每日新增
@app.route("/l2")
def get_l2_data():
    data1,data2 = utils.get_l2_data()
    days1, days2, china_confirm_add, china_heal_add, china_dead_add, global_confirm_add, global_heal_add, global_dead_add = [], [], [], [], [], [], [], []
    for a, b, c, d in data1:
        days1.append(a.strftime("%m-%d"))  # 时间格式截取
        china_confirm_add.append(int(b))
        china_heal_add.append(int(c))
        china_dead_add.append(int(d))
    for i in range(len(data2)):
        if i < len(data2) - 1:
            days2.append(data2[i + 1][0].strftime("%m-%d"))  # 时间格式截取
            global_confirm_add.append(int(data2[i + 1][1]))
            global_heal_add.append(int(data2[i + 1][2] - data2[i][2]))
            global_dead_add.append(int(data2[i + 1][3] - data2[i][3]))
    #print(days1[4:])
    #print(len(days1[4:]))
    #print("----" * 10)
    #print(china_confirm_add[4:])
    #print(china_heal_add[4:])
    #print(china_dead_add[4:])
    #print("----" * 10)
    #print(days2[:-1])
    #print(len(days2[:-1]))
    #print(global_confirm_add[:-1])
    #print(global_heal_add[:-1])
    #print(global_dead_add[:-1])
    return jsonify({"c_day": days1[4:], "c_confirm_add": china_confirm_add[4:], "c_heal_add": china_heal_add[4:],"c_dead_add": china_dead_add[4:],"g_day": days2[:-2], "g_confirm_add": global_confirm_add[:-2], "g_heal_add": global_heal_add[:-2],"g_dead_add": global_dead_add[:-2]})

#病例指数
@app.route("/l3")
def get_l3_data():
    data1,data2 = utils.get_l3_data()
    china_confirm, china_heal ,china_dead = [], [], []
    global_confirm, global_heal, global_dead = [], [], []
    for a, b, c in data1:
        china_confirm.append(int(a))
        china_heal.append(int(b))
        china_dead.append(int(c))
    for a, b, c in data2:
        global_confirm.append(int(a))
        global_heal.append(int(b))
        global_dead.append(int(c))
    return jsonify({"china_confirm": china_confirm, "china_heal": china_heal,"china_dead": china_dead, "global_confirm": global_confirm,"global_heal": global_heal, "global_dead": global_dead})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    heal =[]
    head =[]
    for a,b,c,d in data[:-1]:
        city.append(a)
        confirm.append(int(b))
        heal.append(int(c))
        head.append(int(d))
    return jsonify({"city_r1": city, "confirm_r1": confirm,"heal_r1": heal,"head_r1": head})


@app.route("/r2")
def get_r2_data():
    data1, data2 = utils.get_r2_data()
    days1, days2, china_confirm, china_heal, china_dead, global_confirm, global_heal, global_dead = [], [], [], [], [], [], [], []
    for i in range(len(data1)):
        if i < len(data1):
            days1.append(data1[i][0].strftime("%m-%d"))  # 时间格式截取
            china_confirm.append(int(data1[i][1] - data1[i][2] - data1[i][3]))
            china_heal.append(int(data1[i][2]))
            china_dead.append(int(data1[i][3]))
    for a, b, c, d in data2:
        days2.append(a.strftime("%m-%d"))  # 时间格式截取
        global_confirm.append(int(b))
        global_heal.append(int(c))
        global_dead.append(int(d))
    return jsonify({"c_day": days1, "c_confirm_add": china_confirm, "c_heal_add": china_heal,
                    "c_dead_add": china_dead, "g_day": days2[:-1], "g_confirm_add": global_confirm[:-1],
                    "g_heal_add": global_heal[:-1], "g_dead_add": global_dead[:-1]})

@app.route("/r3")
def get_r3_data():
    data = utils.get_r3_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜数字
        d.append(k)
    return jsonify({"d": d})


if __name__ == '__main__':
    app.run()
