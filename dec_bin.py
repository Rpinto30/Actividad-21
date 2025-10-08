from collections import deque
try:
    num = int(input("Ingresa un número en decimal: "))
    n = num
    if num < 0: raise ValueError
    res = deque()
    r_ = ''
    while num != 0:
        res.append(num%2)
        num//=2
    while len(res) > 0: r_ += str(res.pop())
    print(f'Número {n} a binario: {r_}')
except ValueError: print('Error de entrada...')