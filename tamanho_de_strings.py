str1 = input('Entre com uma frase: ')
str2 = input('Entre com uma frase: ')
print('Compara duas strings')
print('String 1: ',str1)
print('String 2: ',str2)
print('Tamanho de {}: {} caracteres'.format(str1,len(str1)))
print('Tamanho de {}: {} caracteres'.format(str2,len(str2)))
if len(str1) == len(str2):
    print('As duas strings tem o mesmo tamanho')
    aux = 0
    for i in range(0,len(str1),1):
        if str1[i] == str2[i]:
            aux += 1
    if aux == len(str1):
        print('As duas strings possuem conteúdos iguais')
    else:
        print('As duas strings possuem conteúdos diferentes')
else:
    print('As duas strings tem tamanho diferentes')


