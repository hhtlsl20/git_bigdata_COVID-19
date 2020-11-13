import json
import string
from flask import Flask
from flask import request
from flask import render_template
import ultis
from flask import  jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")
@app.route('/time')
def get_time():
    return ultis.get_time()

@app.route('/c1')
def get_c1_data():
    data = ultis.get_c1_data()
    return jsonify({"sum_confirm":data[0],"heal":data[1],"dead":data[2],"suspect:":data[3]})
@app.route('/c2')
def get_c2_data():
    res = []
    for tup in ultis.get_c2_data():
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route("/l1")
def get_l1_data():
    data = ultis.get_l1_data()
    day,confirm,heal,dead,suspect = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:    #很多卫健委网站前7天都是没有数据的，所以把前7天砍掉了
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm.append(b)
        suspect.append(e)
        heal.append(c)
        dead.append(d)
    return jsonify({"day":day,"confirm": confirm, "heal": heal, "dead": dead, "suspect": suspect})

@app.route("/l2")
def get_l2_data():
    data = ultis.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})



@app.route("/r1")
def get_r1_data():
    data = ultis.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


# @app.route("/r2")
# def get_r2_data():
#     data = ultis.get_r2_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
#     d = []
#     for i in data:
#         d.append(i)
#     return jsonify({"kws": d})

@app.route("/l3")
def get_l3_data():
    data=ultis.get_l3_data()
    heal_add=[]
    dead_add=[]
    for info in data:
        heal_add.append(int(info[0]))
        dead_add.append(int(info[1]))
    return jsonify({"heal_add":heal_add,"dead_add":dead_add})
@app.route('/r3')
def get_r3_data():
    data=ultis.get_r3_data()
    info=data[0]
    info2=[]
    for x in info:
        info2.append(x)
    return jsonify({"info2":info2})
@app.route('/guizhou')
def get_guizhou_data():
    privince=request.args.get('privince','')
    data = ultis.get_guizhou_data(privince)
    citys = []
    confirm = []
    res=[]
    i = 0
    for infos in data:
        citys.append(infos[0])
        confirm.append(infos[1])
    city = []
    if(privince=='贵州'):
        for info in citys:
            if (i == 5):
                info = '黔南布依族苗族自治州'
            elif (i == 7):
                info = '黔东南苗族侗族自治州'
            elif (i == 9):
                info = '黔西南布依族苗族自治州'
            else:
                info = info + '市'
            city.append(info)
            i += 1
        x=0
        for i in city:
            res.append({'name':city[x],'value':confirm[x]})
            x+=1
    elif(privince=='重庆'):
        for info in citys:
            city.append(info)
        x = 0
        for i in city:
            res.append({'name': city[x], 'value': confirm[x]})
            x += 1
    elif (privince == '北京'):
        for info in citys:
            info=info+'区'
            city.append(info)
        x = 0
        for i in city:
            res.append({'name': city[x], 'value': confirm[x]})
            x += 1
    elif (privince == '新疆'):
        for info in citys:
            info = info + '地区'
            city.append(info)
        x = 0
        for i in city:
            res.append({'name': city[x], 'value': confirm[x]})
            x += 1
    elif (privince == '上海'):
        for info in citys:
            if(info=='浦东'):
                info=info+'新区'
            else:
                info = info + '区'
            city.append(info)
        x = 0
        for i in city:
            res.append({'name': city[x], 'value': confirm[x]})
            x += 1
    else:
      for info in citys:
          info=info+'市'
          city.append(info)
      x = 0
      for i in city:
          res.append({'name': city[x], 'value': confirm[x]})
          x += 1
    return jsonify({"data":res})
@app.route('/gz_l1')
def get_gz_l1():
    privince = request.args.get('privince','')
    info = ultis.get_gz_l1(privince)
    confirm = []
    name = []
    for data in info:
        confirm.append(data[0])
        name.append(data[1])
    print(privince)
    return jsonify({'name':name,'confirm':confirm})
@app.route('/gz_all_l2')
def get_all_l2():
    province=request.args.get('privince','')
    info = ultis.get_all_l2(province)
    content = []
    counts = []
    for data in info:
        content.append(data[0])
        counts.append(data[1])
    res=[]
    x=0
    for result in content:
        res.append({'name':content[x],'value':counts[x]})
        x+=1
    return jsonify({'data':res})
@app.route('/xinjiang')
def get_xj_l1_data():
    data = ultis.get_xinjiang_data()
    city = []
    confirm = []
    res = []
    for info in data:
        city.append(info[1])
        confirm.append(info[0])
    x=0
    for i in city:
        res.append({'name':city[x],'confirm':confirm[x]})
        x+=1
    return jsonify({"data":res})
if __name__ == '__main__':
    app.run()
