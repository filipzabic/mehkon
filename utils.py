import numpy as np
from sympy import symbols, diff, Matrix


def calculate_cube_side(volume, a1, a2):
    return volume/(a1*a2)

a = 10
alpha = 1.2
beta = 1.3
gamma = 0.1
volume = a**3

X1, X2, X3 = symbols('X1 X2 X3')
x1, x2, x3 = symbols('x1 x2 x3')

#vlak x1
u1 = alpha*a
u2 = 0


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

print(F)
