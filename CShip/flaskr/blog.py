from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')
@app.route('/calculate')
def calculate():
    return render_template('/blog/calculate.html')



if __name__ == '__main__':
    app.run()
