"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# for syntax
list_product = ['camera', 'mobile', 'car', 'laptop']
for product in list_product:
    if(product == 'car'):
        break
    print(product)

# range() 
for i in range(2, 10):
    if i == 5 :
        continue
    print(i)

# step of loop
for i in range(20, 100, 2):
    print(i)