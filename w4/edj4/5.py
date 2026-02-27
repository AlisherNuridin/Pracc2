def func(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
for j in func(n):
    print(j)