from math import *

for x in range (0,361,1):
    y = sin(radians(x))
    z = cos(radians(x))
    a = y*y
    b = z*z
    e = a+b
    print (x, '\t', '%0.3f' % y, '%0.3f' % a, '%0.3f' % b, '%0.3f' % e)
