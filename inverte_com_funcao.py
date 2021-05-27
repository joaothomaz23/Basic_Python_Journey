num = input('Entre com um número inteiro: ')
def inverteNumero(num):
    aux = len(num)
    n = ''
    for i in range(aux-1,-1,-1):
        n = n + num[i]
    return n
nam = inverteNumero(num)
print(nam)
