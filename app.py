from flask import Flask, redirect, request, jsonify, make_response, send_file
from flask import render_template as template
from sympy import symbols, init_printing, latex, Matrix, tan, diff, zeros
from utils import calculate_cube_side, calculate_gradient_tensor, \
                  calculate_left_green_cauchy_tensor, \
                  calculate_right_green_cauchy_tensor, \
                  calculate_euler_tensor, \
                  calculate_lagrange_tensor


app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():

    F = zeros(3)
    b = zeros(3)
    e = zeros(3)
    C = zeros(3)
    E = zeros(3)

    F = latex(F)
    b = latex(b)
    e = latex(e)
    C = latex(C)
    E = latex(E)

    return template('index.html', F=F, b=b, C=C, e=e, E=E)


@app.post('/')
def index_post():
    a = float(request.form['a'])

    alpha = float(request.form['alpha'])
    beta = float(request.form['beta'])
    gamma = float(request.form['gamma'])

    volume = a**3

    #selection = int(request.form['selection'])

    X1, X2, X3 = symbols('X1 X2 X3')
    x1, x2, x3 = symbols('x1 x2 x3')

    #vlak x1
    x = calculate_cube_side(volume, a*alpha, a*beta, 10)

    u1 = tan(gamma)*X2
    u2 = 0
    u3 = 0

    x1 = X1 + u1
    x2 = X2 + u2
    x3 = X3 + u3

    F = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)
    b = calculate_left_green_cauchy_tensor(F)
    C = calculate_right_green_cauchy_tensor(F)
    e = calculate_euler_tensor(b)
    E = calculate_lagrange_tensor(C)

    F = latex(F)
    b = latex(b)
    e = latex(e)
    C = latex(C)
    E = latex(E)



    return template('index.html', F=F, b=b, C=C, e=e, E=E)


@app.errorhandler(404)
def error404(e):
    return 'Stranica ne postoji'
