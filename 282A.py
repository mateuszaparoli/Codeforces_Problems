n = int(input())
x = 0
while n > 0:
    line = input().strip('')
    for word in line:
        if word == '-':
            x = x - 1
            break
        elif word == '+':
            x = x + 1
            break
    n = n - 1
print(x)
