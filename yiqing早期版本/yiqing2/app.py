import string
from flask import Flask
#from flask import request
from flask import render_template
#from jieba.analyse import extract_tags
import ultis
from flask import  jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/main')
def hello():
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


@app.route("/r2")
def get_r2_data():
    data = ultis.get_r2_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    d = []
    for i in data:
        d.append(i)
    return jsonify({"kws": d})

@app.route("/l3")
def get_l3_data():
    data=ultis.get_l3_data()
    confirm_add=[]
    heal_add=[]
    dead_add=[]
    for info in data:
        confirm_add.append(info[0])
        heal_add.append(info[1])
        dead_add.append(info[2])
    return jsonify({"confirm_add":confirm_add,"heal_add":heal_add,"dead_add":dead_add})
@app.route('/r3')
def get_r3_data():
    data=ultis.get_r3_data()
    info=data[0]
    info2=[]
    for x in info:
        info2.append(x)
    return jsonify({"info2":info2})

if __name__ == '__main__':
    app.run()
