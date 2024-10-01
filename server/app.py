#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print (param)
    return param

@app.route('/count/<int:param>')
def count(param):
    numbers = ''.join(f'{i}\n' for i in range(0, param))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation== '+':
        result= num1+num2
    elif operation== '-':
        result= num1-num2
    elif operation== '*':
        result= num1*num2
    elif operation== '%':
        result=num1%num2
    elif operation== 'div':
        result= num1/num2
    else:
        return "invalid"
    
    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
