from line import Line
from point import Point
from sympy import symbols, Eq, solve

def line_intersection(line1, line2):
    if line1.slope() == line2.slope():
        print("Lines are parallel, they do not intersect!")
        return False

    I1 = [min(line1.p1.x, line1.p2.x), max(line1.p1.x, line1.p2.x)]
    I2 = [min(line2.p1.x, line2.p2.x), max(line2.p1.x, line2.p2.x)]

    if max(line1.p1.x, line1.p2.x) < min(line2.p1.x, line2.p2.x):
        print("Lines do not intersect!")
        return False
    else:
        x = symbols('x')
        expr = line1.slope()*x + line1.intercept() - (line2.slope()*x + line2.intercept())
        sol = solve(expr)
        y = float(line1.slope()) * sol[0].evalf() + line1.intercept()
        return sol[0].evalf(), y
    
    

    