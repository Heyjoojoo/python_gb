# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью математических формул нахождения корней квадратного уравнения

#D = b*b - 4ac

# 3*x**2  + 5*x - 6 = 0

import math

equation = '3 *x * *2  + 5*x - 6 = 0'

def create_koef(eq: str):
    new_equation = eq\
        .replace(' ', '')\
        .replace('=0', '')\
        .replace('+', ' ')\
        .replace('-', ' -')

    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_equation.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x')[0])
    return new_list


def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2]),
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b - math.sqrt(disc)) / (2 * a)
        x2 = (-b + math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = (-b - math.sqrt(disc)) / (2 * a)
        return round(x, 2)
    else:
        return None

print(solve_equation(create_koef(equation)))
