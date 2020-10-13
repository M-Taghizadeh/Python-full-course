# why generator used?
# 1)Increasing speed
# 2)Reduce memory usage
# 3)used in iterators(for while)

# exp 1
def first_list():
    yield 'laptop'
    yield 'computer'
    yield 'watch'

for i in first_list():
    print(i)

# exp 2 
def first(n):
    num = 0
    while(num<n):
        yield num
        num = num + 1

for i in first(10):
    print(i)