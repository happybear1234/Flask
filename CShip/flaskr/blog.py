from flask import Flask
from flask import render_template, request
import os

app = Flask(__name__)


@app.route('/')
def basic():
    return render_template('basic.html')


@app.route('/calculate')
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')

@app.route('/brigade')
def brigade():
    if request.method == 'GET':
        return render_template('brigade.html')

@app.route('/experiment')
def experiment():
    if request.method == 'GET':
        return render_template('experiment.html')

@app.route('/mars')
def mars():
    if request.method == 'GET':
        return render_template('mars.html')

@app.route('/MDT')
def MDT():
    if request.method == 'GET':
        return render_template('MDT.html')

@app.route('/MTBF')
def MTBF():
    if request.method == 'GET':
        return render_template('MTBF.html')

@app.route('/MTTR')
def MTTR():
    if request.method == 'GET':
        return render_template('MTTR.html')

# @app.route('/')
# def base():
#     return render_template('base.html')

if __name__ == '__main__':
    app.run()
