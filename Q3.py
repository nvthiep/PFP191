import math
# 1
a, b, c, x = map(float, input().split())
print('S1 = ',a*(x**2) + b*x + c)
# 3
if (b**2 - 4*a*c) < 0:
    print('S2 = ', 0)
else:
    print('S2 = ', math.sqrt(b**2 - 4*a*c))
# 4
if a + b < c or a + c < b or b + c < a:
    print('a, b, c not sides of a triangle')
else:
    p = (a + b + c)/2
    print(math.sqrt(p*(p - a)*(p - b)*(p - c)))





