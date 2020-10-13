n = int(input("n:"))
w = int(input("w:"))
list_shirini = []
for i in range(0, n):
    list_shirini.append(int(input("")))

max = 0
check = 0
for i in range(0, n):
    for j in range(i, n):
        start = i
        end = j

        sum = 0
        for s in range(start, end+1):
            sum += list_shirini[s]
            if(sum == w):
                check = 1
                max = sum
                break
        if sum>=max and sum<=w and sum>=0:
            max = sum 

print(max)
        