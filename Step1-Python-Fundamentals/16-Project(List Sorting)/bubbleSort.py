my_list = [10, 12, 13, 20, 1, 5, 8, 3, 32, 30, 21, 120, 221, 1, 2, 9, 4, 3, 5, 8]

for i in range(0, len(my_list)):
    for j in range(0, len(my_list)-i):
        if(j<= len(my_list)-2):
            if(my_list[j]>=my_list[j+1]):
                #swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)