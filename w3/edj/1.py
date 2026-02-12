def hz(n):
    neznau = str(n)
    for digit in neznau:
        if int(digit) % 2 != 0:
            print("Not valid")
            return
    print("Valid")
num = int(input())
hz(num)