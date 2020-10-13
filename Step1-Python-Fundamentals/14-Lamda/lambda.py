# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax ---> lambda arguments : expression
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print(type(x)) # --> is function

# Why use lambda:
# The power of lambda is better shown when you use them as an anonymous function inside another function..
def myfunc(n):
    return lambda a : a * n
f1 = myfunc(10)
print(f1(5))
print(type(f1)) # --> is function

