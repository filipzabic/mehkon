from sympy import symbols, diff, Matrix, Identity, eye, solve, tan, sqrt

x1, x2, x3 = symbols('x1 x2 x3')
X1, X2, X3 = symbols('X1 X2 X3')

alpha, beta, gamma, y, z = symbols('alpha beta gamma y z')


def calculate_cube_side(V,a1,a2,a3,unknown):
    return solve(V-a1*a2*a3, unknown)


def calculate_gradient_tensor(x1, x2, x3, X1, X2, X3):

    F1_1 = diff(x1, X1)
    F1_2 = diff(x1, X2)
    F1_3 = diff(x1, X3)

    F2_1 = diff(x2, X1)
    F2_2 = diff(x2, X2)
    F2_3 = diff(x2, X3)

    F3_1 = diff(x3, X1)
    F3_2 = diff(x3, X2)
    F3_3 = diff(x3, X3)

    F = Matrix([[F1_1, F1_2, F1_3],
                [F2_1, F2_2, F2_3],
                [F3_1, F3_2, F3_3]])
    
    return F


def calculate_lagrange_tensor(C):
    return 0.5*(C-eye(3))


def calculate_euler_tensor(b):
    return 0.5*(eye(3)-b**-1)


def calculate_left_green_cauchy_tensor(F):
    return F*F.T


def calculate_right_green_cauchy_tensor(F):
    return F.T*F


def calculate_parallelepiped_diagonal(F, d):
    D = F*d
    return sqrt(D[0]**2 + D[1]**2 + D[2]**2)


def step_one():
    x1 = alpha*X1
    x2 = X2
    x3 = y*X3

    F1 = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)

    return F1


def step_two():
    x1 = X1
    x2 = beta*X2
    x3 = z*X3

    F2 = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)

    return F2


def step_three():
    x1 = X1+tan(gamma)*X2
    x2 = X2
    x3 = X3

    F3 = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)

    return F3


def step_four(F1,F2,F3):
    F = F3*F2*F1

    return F
