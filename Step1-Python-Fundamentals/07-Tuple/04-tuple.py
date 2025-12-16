"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


### [TUPLE]
# tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# len
print(len(my_tuple))

# change tuple values :
x = ("2015", "2016", "2017", "2019")
y = list(x)
y[3] = "2018"
x = tuple(y)
print(x)

# join
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1 = t1+t2
print(t1)