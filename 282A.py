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

"""
# time_opt.py
import sys
data = sys.stdin.buffer.read()      # lê tudo como bytes (rápido)
# Conta quantas linhas têm "++" e quantas têm "--"
result = data.count(b'++') - data.count(b'--')
print(result)




# memory_opt.py
import sys
it = iter(sys.stdin.readline, '')   # iterator que lê linha a linha até EOF
n = int(next(it))                   # primeira linha
x = 0
for _ in range(n):
    s = next(it).strip()            # só mantém a linha atual
    # verificar o caractere do meio é a maneira mais rápida/segura
    if s[1] == '+':
        x += 1
    else:
        x -= 1
print(x)




# balanced.py
import sys
input = sys.stdin.readline
n = int(input())
x = 0
for _ in range(n):
    s = input().strip()
    # qualquer uma das formas funciona; s[1] é constante porque todos os enunciados têm 3 chars
    if s[1] == '+':
        x += 1
    else:
        x -= 1
print(x)

"""