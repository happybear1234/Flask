from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    products = ["iphoneX", "MacBook Pro", "Huawei"]
    kwargs = {
        "products": products
    }
    return render_template('base.html', **kwargs)


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')


@app.route('/ex')
def my_test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
