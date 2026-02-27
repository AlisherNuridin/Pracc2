def x(lst, k):
    for i in range(k):
        for item in lst:
            yield item

lst = input().split()
k = int(input())

print(*x(lst, k))