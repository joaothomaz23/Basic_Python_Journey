import random
r = ['caneca','caneta','farofa','jurado']
plv = '_'
i = random.randint(0,3)
val = r[i]
erro = 1
while erro <= 6:
    letra = input('Digite uma letra: ')
    cont = 0
    for j in range(0,len(val),1):
        if val[j] == letra:
            plv = plv + letra
            cont += 1
        else:
            plv = plv + '_'
    print('A palavra é: ',r)    
    if cont == 0:
        print('Você errou a {}ª vez. Tente de novo!'.format(erro))
        erro += 1
    
