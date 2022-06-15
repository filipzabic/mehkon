from flask import Flask, redirect, request, jsonify, make_response, send_file
from flask import render_template as template
#from waitress import serve
from sympy import symbols, init_printing, latex, Matrix


app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    x = symbols('x')
    x = x**2
    F = Matrix([x, x])
    F = latex(F)
    
    return template('index.html', var=F)


@app.post('/')
def index_post():
    hours_worked = int(request.form['hours_worked'])
    hourly_pay = int(request.form['hourly_pay'])
    date_from = request.form['date_from']
    date_to = request.form['date_to']
    other_fees = int(request.form['other_fees'])

    return template('index.html', var=F)


@app.errorhandler(404)
def error404(e):
    return 'Stranica ne postoji'


if __name__ == '__main__':
    app.run(debug=True)
