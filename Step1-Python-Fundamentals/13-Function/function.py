# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# def ---> create function
def say_hello(name):
    print('hello ' + name)
say_hello('reza')


# default Arguments
def show_user_info(name, last_name, age, email, country='iran'):
    print('name :', name)
    print('last name :', last_name)
    print('age :', age)
    print('email :', email)
    print('country :', country)
show_user_info('mohammad', 'taghizadeh', '22', 'taghizadeh@gmail.com')
show_user_info('mahsan', 'motahari', '21', 'mahsan@gmail.com', 'germany')


# *args : If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def show_product(*arg):
    print(arg[1])
show_product('mobile', 'laptop', 'car')

# return value:
def get_avg(sum_numbers, sum_unit):
    avg = sum_numbers / sum_unit
    return avg
my_avg = get_avg(390, 20)
print("AVG :", my_avg)

 
#  Recursion ---> exp) Fibo Func : [0  1  1  2  3  5  8  13 …]
def fibo(number):
    if(number == 0 or number == 1):
        return number
    else:
        return fibo(number - 1) + fibo(number - 2)

number = int(input('Enter number :'))
for i in range(0, number):
    print(fibo(i))
