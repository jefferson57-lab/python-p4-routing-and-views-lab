from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param  


@app.route('/count/<int:param>')
@app.route('/count/<int:param>')
def count(param):
    numbers = [str(i) for i in range(param)]
    return '\n'.join(numbers) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero is not allowed.', 400
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero is not allowed.', 400
        result = num1 % num2
    else:
        return 'Invalid operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
