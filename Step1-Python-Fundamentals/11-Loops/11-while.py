"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# Python has two primitive loop commands:
# 1) while loops --> With the while loop we can execute a set of statements as long as a condition is true.
# 2) for loops   --> A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

i = 0
while i < 10:
    print(i)
    i = i+3 # counter
else:
    print('end of while')

i = 0
list_name = ['mohammad', 'reza', 'sara', 'mahsan']
while i<len(list_name):
    print(list_name[i])
    i=i+1


# break and continue
i = 0
while i<10:
    if(i == 6):
        break
    if(i == 3):
        i = i+1
        continue
    print(i)
    i = i+1

