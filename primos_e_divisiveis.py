num = int(input('Entre com um número inteiro: '))
aux = 0
if  num == 2 or num == 3 or num == 5 or num == 7:
    print('%i é um número primo!'%(num))
for i in range(1,11,1):
    if num%i != 0:
        aux = aux + 1
    else:
        print('%i é um número divisivel por %i'%(num,i))
if aux == 9:
    print('%i é um número divisivel por %i'%(num,num))
    print('%i é um número primo!'%(num))
