"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


my_list = [10, 12, 13, 20, 1, 5, 8, 3, 32, 30, 21, 120, 221, 1, 2, 9, 4, 3, 5, 8]

for i in range(1, len(my_list)):
    if(my_list[i]<my_list[i-1]):
            j = i
            if(j == 0):
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                while(my_list[j]<my_list[j-1] and j>0):
                    my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
                    j = j-1
print(my_list)