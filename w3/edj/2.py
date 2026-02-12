n = int(input())
p = [2,3,5]

if n < 1:
    print("No")
else:
    for i in p:
        while n % i == 0:
            n //= i
    if (n == 1):
        print("Yes")
    else:
        print("No")