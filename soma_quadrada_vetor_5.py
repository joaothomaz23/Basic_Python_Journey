a = []
for i in range(0,10,1):
    num = int(input('Entre com um valor inteiro: '))
    a.append(num)
soma_quadrada = 0
for i in a:
    soma_quadrada = soma_quadrada + i**2
    print(soma_quadrada)
