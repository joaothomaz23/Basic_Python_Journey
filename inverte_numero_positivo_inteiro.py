num = str(input('Entre com um numero inteiro positivo: '))
aux = len(num)-1
n = ''
for i in range(aux,-1,-1):
    n = n + num[i]
print(n)
