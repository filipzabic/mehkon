from flask import Flask, redirect, request, jsonify, make_response, send_file
from flask import render_template as template
from sympy import symbols, latex, zeros, Matrix, N
from utils import calculate_cube_side, calculate_gradient_tensor, \
                  calculate_left_green_cauchy_tensor, \
                  calculate_right_green_cauchy_tensor, \
                  calculate_euler_tensor, \
                  calculate_lagrange_tensor, \
                  calculate_parallelepiped_diagonal, \
                  calculate_cube_side, \
                  step_one, step_two, step_three, step_four


app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():

    Fs = zeros(3)
    bs = zeros(3)
    es = zeros(3)
    Cs = zeros(3)
    Es = zeros(3)
    Ds = zeros(3,1)

    F = zeros(3)
    b = zeros(3)
    e = zeros(3)
    C = zeros(3)
    E = zeros(3)
    D = zeros(3,1)

    Fs = latex(Fs)
    bs = latex(bs)
    es = latex(es)
    Cs = latex(Cs)
    Es = latex(Es)
    Ds = latex(Ds)

    F = latex(F)
    b = latex(b)
    e = latex(e)
    C = latex(C)
    E = latex(E)
    D = latex(D)

    return template('index.html',
                    F=F, b=b, C=C, e=e, E=E, D=D,
                    Fs=Fs, bs=bs, Cs=Cs, es=es, Es=Es, Ds=D)


@app.post('/')
def index_post():
    a_val = float(request.form['a'])

    alpha_val = float(request.form['alpha'])
    beta_val = float(request.form['beta'])
    gamma_val = float(request.form['gamma'])

    selection = int(request.form['selection'])

    if selection == 1:
        Fs = step_one()

    elif selection == 2:
        Fs = step_two()

    elif selection == 3:
        Fs = step_three()

    elif selection == 4:
        F1s = step_one()
        F2s = step_two()
        F3s = step_three()
        Fs = step_four(F1s,F2s,F3s)

    alpha, beta, gamma, y, z = symbols('alpha beta gamma y z')
    a = symbols('a')

    bs = calculate_left_green_cauchy_tensor(Fs)
    Cs = calculate_right_green_cauchy_tensor(Fs)
    es = calculate_euler_tensor(bs)
    Es = calculate_lagrange_tensor(Cs)
    ds = Matrix([[a],[a],[a]])
    Ds = calculate_parallelepiped_diagonal(Fs, ds)

    ys = calculate_cube_side(a**3, alpha*a, a, y*a, y)[0]
    zs = calculate_cube_side(a**3, alpha*a, beta*a, z*a, z)[0]

    y_val = ys.subs([(alpha, alpha_val)])
    z_val = zs.subs([(alpha, alpha_val), (beta, beta_val)])

    substitutions = [(alpha, alpha_val), (beta, beta_val), (gamma, gamma_val), 
                     (y, y_val), (z, z_val)]

    F = Fs.subs(substitutions)
    b = calculate_left_green_cauchy_tensor(F)
    C = calculate_right_green_cauchy_tensor(F)
    e = calculate_euler_tensor(b)
    E = calculate_lagrange_tensor(C)
    d = Matrix([[a_val],[a_val],[a_val]])
    D = calculate_parallelepiped_diagonal(F, d)

    F = latex(N(F, 3))
    b = latex(N(b, 3))
    e = latex(N(e, 3))
    C = latex(N(C, 3))
    E = latex(N(E, 3))
    D = latex(N(D, 3))

    Fs = latex(Fs)
    bs = latex(bs)
    es = latex(es)
    Cs = latex(Cs)
    Es = latex(Es)
    Ds = latex(Ds)

    return template('index.html',
                    F=F, b=b, C=C, e=e, E=E, D=D,
                    Fs=Fs, bs=bs, Cs=Cs, es=es, Es=Es, Ds=Ds)


@app.route('/postupak')
def postupak():
    return send_file('postupak.pdf', as_attachment=False, attachment_filename="postupak.pdf")


@app.errorhandler(404)
def error404(e):
    return 'Stranica ne postoji'
