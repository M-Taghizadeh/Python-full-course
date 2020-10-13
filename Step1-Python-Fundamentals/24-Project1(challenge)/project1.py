n = int(input(''))
weight = []
for i in range(0, n):
    weight.append(int(input('')))

max = 0
index_of_max = 0
for i in range(0, n):
    if(weight[i]>=max):
        index_of_max = i
        max = weight[i]

print(index_of_max+1)