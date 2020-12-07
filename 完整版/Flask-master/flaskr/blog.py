from flask import Flask
from flask import render_template, request, redirect, jsonify
import os
import json
import utils
app = Flask(__name__)


@app.route('/')
def basic():
    return render_template('calculate.html')


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')


@app.route('/brigade')
def brigade():
    return render_template('brigade.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/experiment')
def experiment():
    return render_template('experiment.html')


@app.route('/mars')
def mars():
    return render_template('mars.html')


@app.route('/MDT')
def MDT():
    return render_template('MDT.html')


@app.route('/MTBF')
def MTBF():
    return render_template('MTBF.html')


@app.route('/MTTR')
def MTTR():
    return render_template('MTTR.html', )


@app.route('/login', methods=["POST"])
def login():
    a = request.form.get("system")
    b = request.form.get("brigade")
    c = request.form.get("start")
    d = request.form.get("end")
    e = request.form.get("cal")
    f = request.form.get("fun")
    filetxt = open('C:/Users/seri_1/Test/input.txt','w')
    txt = a + "|" + b + "|" + c + "|" + d + "|" + e + "|" + f
    filetxt.write(txt)
    filetxt.close()
    return render_template("calculate.html")


@app.route('/process')
def process():
    os.system('python C:/Users/seri_1/Test/SQLDATA.py')
    return render_template("calculate.html")


# 单一舰队使用可用度
@app.route('/brigade1', methods=['POST', 'GET'])
def brigade1():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1 = request.form.get('select1')
        return jsonify({"status":200})
    elif request.method =="GET":
        return json.dumps(utils.t11(date1, date2, date3), ensure_ascii=False)
    else:
        return json.dumps(utils.t11("205大队", "2004-10", "2020-1"), ensure_ascii=False)

# 所有舰队使用可用度
@app.route('/brigade2', methods=['POST', 'GET'])
def brigade2():
    global date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        return jsonify({"status":200})
    if request.method =="GET":
        return json.dumps(utils.t12(date2, date3), ensure_ascii=False)


# 单一舰队年度使用可用度
@app.route('/brigade3', methods=['POST', 'GET'])
def brigade3():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate3')
        date3 = request.form.get('endDate3')
        date1 = request.form.get('select3')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t11(date1, date2, date3))
        return json.dumps(utils.t13(date1, date2, date3), ensure_ascii=False)


# 单一系统使用可用度
@app.route('/system1', methods=['POST', 'GET'])
def system1():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1 = request.form.get('select1')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t11(date1, date2, date3))
        return json.dumps(utils.t21(date1, date2, date3), ensure_ascii=False)


# 所有系统使用可用度
@app.route('/system2', methods=['POST', 'GET'])
def system2():
    global date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        #print(date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t12(date2, date3))
        return json.dumps(utils.t22(date2, date3), ensure_ascii=False)


# 单一系统年度使用可用度
@app.route('/system3', methods=['POST', 'GET'])
def system3():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate3')
        date3 = request.form.get('endDate3')
        date1 = request.form.get('select3')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t11(date1, date2, date3))
        return json.dumps(utils.t23(date1, date2, date3), ensure_ascii=False)


# 单一试验固有可用度
@app.route('/experiment1', methods=['POST', 'GET'])
def experiment1():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1 = request.form.get('select1')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t11(date1, date2, date3))
        return json.dumps(utils.t31(date1, date2, date3), ensure_ascii=False)


# 所有试验固有可用度
@app.route('/experiment2', methods=['POST', 'GET'])
def experiment2():
    global date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        #print(date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t12(date2, date3))
        return json.dumps(utils.t32(date2, date3), ensure_ascii=False)


# 单一试验年度固有可用度
@app.route('/experiment3', methods=['POST', 'GET'])
def experiment3():
    global date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate3')
        date3 = request.form.get('endDate3')
        date1 = request.form.get('select3')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        #print(utils.t11(date1, date2, date3))
        return json.dumps(utils.t33(date1, date2, date3), ensure_ascii=False)


# 单一系统马氏稳态可用度
@app.route('/mars1', methods=['POST', 'GET'])
def mars1():
    global date1_1, date1_2, date1_3, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1_1 = request.form.get('select1_1')
        date1_2 = request.form.get('select1_2')
        date1_3 = request.form.get('select1_3')
        #print(date2,date1_1)
        return jsonify({"status":200})
    if request.method =="GET":
        for i in utils.get_t41_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t411(date1_2, date2, date3), ensure_ascii=False)
        for i in utils.get_t42_data():
            if (i[0] == date1_1 and date1_1 != None):
                #print(utils.t421(date1_1, date2, date3))
                return json.dumps(utils.t421(date1_1, date2, date3), ensure_ascii=False)
        for i in utils.get_t43_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t431(date1_3, date2, date3), ensure_ascii=False)


# 所有系统马氏稳态可用度
@app.route('/mars2', methods=['POST', 'GET'])
def mars2():
    global date1_1, date1_2, date1_3, date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        date1_1 = request.form.get('select2_1')
        date1_2 = request.form.get('select2_2')
        date1_3 = request.form.get('select2_3')
        #print(date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        if ("舰队" == date1_2):
            return json.dumps(utils.t412(date2, date3), ensure_ascii=False)
        if ("系统" == date1_1):
            return json.dumps(utils.t422(date2, date3), ensure_ascii=False)
        if ("试验" == date1_3):
            return json.dumps(utils.t432(date2, date3), ensure_ascii=False)

# 单一系统瞬时可用度
@app.route('/mars3', methods=['POST', 'GET'])
def mars3():
    global date1_1, date1_2, date1_3, date1, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate3')
        date3 = request.form.get('endDate3')
        date1_1 = request.form.get('select3_1')
        date1_2 = request.form.get('select3_2')
        date1_3 = request.form.get('select3_3')
        #print(date1, date2.split("-")[0], date3)
        return jsonify({"status":200})
    if request.method =="GET":
        for i in utils.get_t44_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t441(date2, date3), ensure_ascii=False)
        for i in utils.get_t45_data():
            if (i[0] == date1_1 and date1_1 != None):
                print(utils.t451(date2, date3))
                return json.dumps(utils.t451(date2, date3), ensure_ascii=False)
        for i in utils.get_t46_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t461(date2, date3), ensure_ascii=False)
# 单一系统所有设备MTBF
@app.route('/MTBF1', methods=['POST', 'GET'])
def MTBF1():
    global date1_1, date1_2, date1_3, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1_1 = request.form.get('select1_1')
        date1_2 = request.form.get('select1_2')
        date1_3 = request.form.get('select1_3')
        return jsonify({"status":200})
    if request.method =="GET":
        for i in utils.get_t51_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t511(date1_2, date2, date3), ensure_ascii=False)
        for i in utils.get_t52_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t521(date1_1, date2, date3), ensure_ascii=False)
        for i in utils.get_t53_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t531(date1_3, date2, date3), ensure_ascii=False)

# 单一系统单一设备年度MTBF
@app.route('/MTBF2', methods=['POST', 'GET'])
def MTBF2():
    global date1_1, date1_2, date1_3, date1_4, date2, date3
    if request.method =="POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        date1_1 = request.form.get('select2_1')
        date1_2 = request.form.get('select2_2')
        date1_3 = request.form.get('select2_3')
        date1_4 = request.form.get('select2_4')
        return jsonify({"status":200})
    if request.method =="GET":
        for i in utils.get_t61_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t611(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t62_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t621(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t63_data():
            if (i[0] == date1_3 and date1_3 != None):

                return json.dumps(utils.t631(date1_4, date2, date3), ensure_ascii=False)

# 单一系统所有设备MTTR
@app.route('/MTTR1', methods=['POST', 'GET'])
def MTTR1():
    global date1_1, date1_2, date1_3, date2, date3
    if request.method == "POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1_1 = request.form.get('select1_1')
        date1_2 = request.form.get('select1_2')
        date1_3 = request.form.get('select1_3')
        return jsonify({"status": 200})
    if request.method == "GET":
        for i in utils.get_t51_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t711(date1_2, date2, date3), ensure_ascii=False)
        for i in utils.get_t52_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t721(date1_1, date2, date3), ensure_ascii=False)
        for i in utils.get_t53_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t731(date1_3, date2, date3), ensure_ascii=False)

# 单一系统单一设备年度MTTR
@app.route('/MTTR2', methods=['POST', 'GET'])
def MTTR2():
    global date1_1, date1_2, date1_3, date1_4, date2, date3
    if request.method == "POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        date1_1 = request.form.get('select2_1')
        date1_2 = request.form.get('select2_2')
        date1_3 = request.form.get('select2_3')
        date1_4 = request.form.get('select2_4')
        return jsonify({"status": 200})
    if request.method == "GET":
        for i in utils.get_t61_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t811(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t62_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t821(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t63_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t831(date1_4, date2, date3), ensure_ascii=False)

# 单一系统所有设备MDT
@app.route('/MDT1', methods=['POST', 'GET'])
def MDT1():
    global date1_1, date1_2, date1_3, date2, date3
    if request.method == "POST":
        date2 = request.form.get('startDate1')
        date3 = request.form.get('endDate1')
        date1_1 = request.form.get('select1_1')
        date1_2 = request.form.get('select1_2')
        date1_3 = request.form.get('select1_3')
        return jsonify({"status": 200})
    if request.method == "GET":
        for i in utils.get_t51_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t911(date1_2, date2, date3), ensure_ascii=False)
        for i in utils.get_t52_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t921(date1_1, date2, date3), ensure_ascii=False)
        for i in utils.get_t53_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t931(date1_3, date2, date3), ensure_ascii=False)

# 单一系统单一设备年度MDT
@app.route('/MDT2', methods=['POST', 'GET'])
def MDT2():
    global date1_1, date1_2, date1_3, date1_4, date2, date3
    if request.method == "POST":
        date2 = request.form.get('startDate2')
        date3 = request.form.get('endDate2')
        date1_1 = request.form.get('select2_1')
        date1_2 = request.form.get('select2_2')
        date1_3 = request.form.get('select2_3')
        date1_4 = request.form.get('select2_4')
        return jsonify({"status": 200})
    if request.method == "GET":
        for i in utils.get_t61_data():
            if (i[0] == date1_2 and date1_2 != None):
                return json.dumps(utils.t1011(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t62_data():
            if (i[0] == date1_1 and date1_1 != None):
                return json.dumps(utils.t1021(date1_4, date2, date3), ensure_ascii=False)
        for i in utils.get_t63_data():
            if (i[0] == date1_3 and date1_3 != None):
                return json.dumps(utils.t1031(date1_4, date2, date3), ensure_ascii=False)

# 初始化界面
# 单一舰队使用可用度
@app.route('/br1', methods=["GET", "POST"])
def br1():
    return json.dumps(utils.t11("205大队", "2004", "2020"), ensure_ascii=False)

# 所有舰队使用可用度
@app.route('/br2', methods=["GET", "POST"])
def br2():
    return json.dumps(utils.t12("2004", "2020"), ensure_ascii=False)

# 单一舰队年度使用可用度
@app.route('/br3', methods=["GET", "POST"])
def br3():
    return json.dumps(utils.t13("205大队", "2004", "2020"), ensure_ascii=False)

# 单一系统使用可用度
@app.route('/sy1', methods=["GET", "POST"])
def sy1():
    return json.dumps(utils.t21("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)

# 所有系统使用可用度
@app.route('/sy2', methods=["GET", "POST"])
def sy2():
    return json.dumps(utils.t22("2004", "2020"), ensure_ascii=False)

# 单一系统年度使用可用度
@app.route('/sy3', methods=["GET", "POST"])
def sy3():
    return json.dumps(utils.t23("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)

# 单一试验固有可用度
@app.route('/ex1', methods=["GET", "POST"])
def ex1():
    return json.dumps(utils.t31("4A系泊航行", "2004", "2020"), ensure_ascii=False)

# 所有试验固有可用度
@app.route('/ex2', methods=["GET", "POST"])
def ex2():
    return json.dumps(utils.t32("2004", "2020"), ensure_ascii=False)

# 单一试验年度固有可用度
@app.route('/ex3', methods=["GET", "POST"])
def ex3():
    return json.dumps(utils.t33("4A系泊航行", "2004", "2020"), ensure_ascii=False)

# 单一系统马氏稳态可用度
@app.route('/ma1', methods=["GET", "POST"])
def ma1():
    return json.dumps(utils.t421("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)

# 所有系统马氏稳态可用度
@app.route('/ma2', methods=["GET", "POST"])
def ma2():
    return json.dumps(utils.t422("2004", "2020"), ensure_ascii=False)

# 单一系统瞬时可用度
@app.route('/ma3', methods=["GET", "POST"])
def ma3():
    return json.dumps(utils.t451("2004", "2020"), ensure_ascii=False)

# 单一系统所有设备MTBF
@app.route('/mtb1', methods=["GET", "POST"])
def mtb1():
    return json.dumps(utils.t521("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)
# 单一系统单一设备年度MTBF
@app.route('/mtb2', methods=["GET", "POST"])
def mtb2():
    return json.dumps(utils.t621("H/PJ13型6管30mm舰炮", "2004", "2020"), ensure_ascii=False)

# 单一系统所有设备MTTR
@app.route('/mtt1', methods=["GET", "POST"])
def mtt1():
    return json.dumps(utils.t721("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)

# 单一系统单一设备年度MTTR
@app.route('/mtt2', methods=["GET", "POST"])
def mtt2():
    return json.dumps(utils.t821("H/PJ13型6管30mm舰炮", "2004", "2020"), ensure_ascii=False)

# 单一系统所有设备MDT
@app.route('/mdt1', methods=["GET", "POST"])
def mdt1():
    return json.dumps(utils.t921("6管30mm舰炮系统", "2004", "2020"), ensure_ascii=False)

# 单一系统单一设备年度MDT
@app.route('/mdt2', methods=["GET", "POST"])
def mdt2():
    return json.dumps(utils.t821("H/PJ13型6管30mm舰炮", "2004", "2020"), ensure_ascii=False)


if __name__ == '__main__':
    app.run()
