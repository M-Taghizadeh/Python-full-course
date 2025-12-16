"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


my_list = [10, 12, 13, 20, 1, 5, 8, 3, 32, 30, 21, 120, 221, 1, 2, 9, 4, 3, 5, 8]

for i in range(0, len(my_list)):
    Min = 10000000
    index = 0
    for j in range(i, len(my_list)):
        if(my_list[j]<Min):
            Min = my_list[j]
            index = j
    my_list[i], my_list[index] = my_list[index], my_list[i]

print(my_list)