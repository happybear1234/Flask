from flask import Flask
from flask import render_template, request, redirect
import os
import pymysql, json

from flask import jsonify

app = Flask(__name__)


# 数据库测试
@app.route('/t', methods=['GET', 'POST'])
def t():
    res = []
    for i in get_data():
        res.append({"name": i[0], "value": i[1]})
    return json.dumps(res, ensure_ascii=False)


# 表单测试
@app.route('/getdate', methods=['POST', 'GET'])
def getdate():
    if request.method == "POST":
        date1 = request.form.get('startDate1')
        date2 = request.form.get('endDate1')
        date3 = request.form.get('select1')
        print('post', date1, date2, date3)
    return redirect('/brigade')


# 整体测试
@app.route('/dataurl', methods=['POST', 'GET'])
def dataurl():
    if request.method == "POST":
        date1 = request.form.get('startDate1')
        date2 = request.form.get('endDate1')
        date3 = request.form.get('select1')
        print('post', date1, date2, date3)
        res = []
        for i in get_data():
            res.append({"name": i[0], "value": i[1]})
        return json.dumps(res, ensure_ascii=False)


@app.route('/')
def basic():
    return render_template('calculate.html')


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')


@app.route('/brigade')
def brigade():
    return render_template('brigade.html')


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


# @app.route('/')
# def base():
#     return render_template('base.html')

if __name__ == '__main__':
    app.run()


# def class_list():
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',
#                            charset="utf8")
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute("select count,class_name from Class")
#     class_list = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     class_list = {'人数': [{"一班": 35}, {"二班": 20}, {"三班": 34}]}
#     print(class_list)
#     json_classlist = json.dumps(class_list, ensure_ascii=False)
#     print(type(json_classlist))
#     print(json_classlist)
#     return class_list


def get_conn():
    # 创建连接
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='20051104',
        db='django_StudenManage',
        charset='utf8', )
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组展示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    # 封装通用查询
    #:param sql:
    #:param args:
    #:return:返回查询结果，((),(),)的形式

    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_data():
    sql = "select brigade,availability_sta from system_ste_output where if_average_br = 1"

    res = query(sql)
    # print(res)
    return res

# print(get_data())
