import random
def embaralhaString(a):
    b = []
    for i in range(0,len(a),1):
        b.append(a[i])
    random.shuffle(b)
    c = ''
    for i in range(0,len(b),1):
        c = c + b[i]
    return c
val = input('Entre com uma string aleatoria: ')
aux = embaralhaString(val)
print(aux)
