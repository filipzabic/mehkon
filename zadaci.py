from utils import calculate_cube_side, calculate_gradient
from sympy import symbols


a = 10
alpha = 1.2
beta = 1.3
gamma = 0.1
volume = a**3

X1, X2, X3 = symbols('X1 X2 X3')
x1, x2, x3 = symbols('x1 x2 x3')

# vlak x1
x = calculate_cube_side(volume, a*alpha, a, 10)

u1 = alpha*a
u2 = 0
u3 = x*a

x1 = X1 + u1
x2 = X2 + u2
x3 = X3 + u3

F1 = calculate_gradient(x1, x2, x3, X1, X2, X3)

# vlak x2
x = calculate_cube_side(volume, a*alpha, a*beta, 10)

u1 = 0
u2 = beta*a
u3 = x*a

x1 = X1 + u1
x2 = X2 + u2
x3 = X3 + u3

F1 = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)


# trapez
x = calculate_cube_side(volume, a*alpha, a*beta, 10)

u1 = 0
u2 = beta*a
u3 = x*a

x1 = X1 + u1
x2 = X2 + u2
x3 = X3 + u3

F1 = calculate_gradient_tensor(x1, x2, x3, X1, X2, X3)

print(F1)
