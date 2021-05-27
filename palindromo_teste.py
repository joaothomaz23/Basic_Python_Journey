strg = input('Entre com uma frase: ')
aux = strg
cont = 0
n = 0
for i in range(len(strg)-1,-1,-1):
    if strg[i] == aux[n]:
        n += 1
        cont += 1
if cont == len(strg):
    print('A frase é um palindromo! ')
else:
    print('A frase não é um palindromo! ')
