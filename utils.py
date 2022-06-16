import numpy as np
from sympy import symbols, diff, Matrix, Identity, eye


def calculate_cube_side(volume, a1, a2, base):
    return volume/(a1*a2*base)


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
    return 0.5*(eye(3)-b.inv())


def calculate_left_green_cauchy_tensor(F):
    return F*F.T


def calculate_right_green_cauchy_tensor(F):
    return F.T*F