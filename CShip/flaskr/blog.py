from flask import Flask
from flask import render_template, request
import os
import pymysql

app = Flask(__name__)


# from .settings import ProductionConfig
# # 配置文件
# app.config.from_object(ProductionConfig())


@app.route('/')
def basic():
    return render_template('calculate.html')


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')


@app.route('/brigade')
def brigade():
    class_list={'id': 11, 'class_name': '一班'}, {'id': 22, 'class_name': '二班'}, {'id': 33, 'class_name': '三班'}
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
    return render_template('MTTR.html',)


# @app.route('/')
# def base():
#     return render_template('base.html')

if __name__ == '__main__':
    app.run()


def class_list():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',
                           charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,class_name from Class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(class_list)
    return class_list
class_list()