num1 = float(input('Entre com um número real: '))
num2 = float(input('Entre com um número real: '))
num3 = float(input('Entre com um número real: '))
num4 = float(input('Entre com um número real: '))
num5 = float(input('Entre com um número real: '))
num =[num1, num2, num3, num4, num5]
aux = [0,1,2,3,4]
soma = 0
for i in aux:
    soma = soma + num[i]

media = soma/5
print('A soma é ',soma)
print('A media é ', media)
