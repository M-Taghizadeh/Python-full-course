str_alish = input('')
my_list = []

for char in str_alish:
    my_list.append(char)

i = 0
while i < len(my_list):

    if(my_list[i] == '='):
        del my_list[i] ### delete index of i
        i = i - 1
		flag = 0

        if i >= 0: 
            del my_list[i] ### delete index of i-1
            flag = 1
			
		if flag == 1:
		i -= 1
		
    i = i + 1
        

str_new = ''
for char in my_list:
    str_alish += char
print(str_alish)