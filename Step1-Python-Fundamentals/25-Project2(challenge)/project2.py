import math

number_of_house = int(input(''))
str_house = input('')
s = int(input(''))
t = int(input(''))

if s>t:
    start = t
    end = s - 2
else:
    start = s
    end = t - 2

operation = 0
list_H = []
index = 0

i = start
while i <= end:
    count = 0
    while(str_house[i] == 'H' and i<=end):
        count = count+1
        i = i+1
        if str_house[i] == 'P':
            list_H.append(count)
            index = index + 1
    i = i+1

for j in range(0, index):
    degree = math.log2(list_H[j])
    print(degree)
    fix = int(math.pow(2, degree))
    remain = list_H[j] - fix

    if(remain == 0):
        operation += 1
    else:
        operation += 1

        while(remain != 0):
            degree = math.log2(remain)
            print(degree)
            fix = int(math.pow(2, degree))
            remain = remain - fix
            operation += 1

            if(remain==0):
                break
print("number of operation is :", operation)