print('Este programa é uma calculadora de potências: ')
base =  int(input('Entre com a base da sua potência: '))
exp = int(input('Entre com o expoente da sua potência '))
pot = base
for i in range(1,exp,1):
    pot = pot*base
print('O valor da potência é: ', pot)
