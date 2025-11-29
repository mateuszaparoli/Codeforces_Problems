n = int(input())
count = 0
while n > 0:
    user = input().split()
    a = int(user[0])
    b = int(user[1])
    c = int(user[2])
    if a + b + c >= 2:
        count += 1
    n = n - 1
print(count)