n = int(input('Entre com o numero N, até o onde remos caçar números primos: '))
for num in range(1,n+1,1):
    aux = 0
    if  num == 2 or num == 3 or num == 5 or num == 7:
        print('%i é um número primo!'%(num))
    for i in range(1,11,1):
        if num%i != 0:
            aux = aux + 1
    if aux == 9:
        print('%i é um número primo!'%(num))
