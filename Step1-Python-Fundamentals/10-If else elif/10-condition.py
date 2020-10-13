### [Operators] 
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# if condition :
#     ....
# else :
#     ....

### quadratic equation example
 # a=5, b=6, c=1 ---> delta = 16 ---> x1=-0.2, x2=-1
 # a=1, b=2, c=1 ---> delta = 0  ---> x=-1
 # a=4, b=1, c=1 ---> delta = -15 
 
import math
a = int(input('Enter a :'))
b = int(input('Enter b :'))
c = int(input('Enter c :'))
delta = math.pow(b, 2) - (4*a*c)
print('delta is %s for a:%s b:%s c:%s' %(delta,a, b, c))

if delta>0:
    x1 = ( -b+(math.sqrt(delta)) )/ (2*a)
    x2 = ( -b-(math.sqrt(delta)) )/ (2*a)
    print('x1 = %s and x2 = %s' %(x1, x2))
elif delta<0:
    print('The equation has no real answer.')

elif delta==0:
    x = (-b) / (2*a)
    print('x = %s' %x)
