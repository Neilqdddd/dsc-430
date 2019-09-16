'''
Yili Lin
1/26/2019
I have not given or received any unauthorized assistance on this assignment.
'''
import random
import math

def inEllipse(x,y,a,b):
    'determin the point is in or outside the ellipse'
    if x**2/(a**2)+y**2/(b**2)>1:
        return False
    else:
        return True

def EllipseArea():
    'calculate the area of ellipse using Monte Carlo method'
    print('Welcome!')
    print('This program will use random numbers to compute the area of an ellipse.')
    F1x, F1y = map(eval, input('Enter the position of F1 (format: x y):').split())
    F2x, F2y = map(eval, input('Enter the position of F2 (format: x y):').split())
    longside = eval(input('Enter the length of the major axis (format: l):'))
    n = eval(input('Enter the number of random points (format: n):'))
    print('Thinking…')

    # half distance between F1 and F2
    d = math.sqrt((F2y - F1y) ** 2 + (F2x - F1x) ** 2) / 2

    # longside
    l = longside / 2

    # determine whether it is a ellipse
    if l < d:
        print('It is not a Ellipse.')
        return

    # shortside
    s = math.sqrt(l ** 2 - d ** 2)

    # calculate the area of ellipse
    count = 0
    for i in range(1, n):
        X = random.uniform(-l, l)
        Y = random.uniform(-s, s)
        if inEllipse(X, Y, l, s) == True: #if in the ellipse
            count += 1
    area = (count / n) * (4 * l * s)#area of ellipse

    # output the area of ellipse
    print(f'The area of the ellipse is approximately {area}.')





