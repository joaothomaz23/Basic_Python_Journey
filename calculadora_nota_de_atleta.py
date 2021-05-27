sis = int(input('Para entrar com o nome do atleta digite 1: '))
while sis == 1:
    atleta = str(input('Entre com o nome do atleta: '))
    s = []
    for i in range(0,5,1):
        salto = float(input('Entre com o valor do salto: '))
        s.append(salto)
    print('Atleta: ',atleta)
    print('Primeiro Salto: ',s[0])
    print('Segundo Salto: ',s[1])
    print('Terceiro Salto: ',s[2])
    print('Quarto Salto: ',s[3])
    print('Quinto Salto: ',s[4])
    print('Melhor Salto: ',max(s))
    print('Pior Salto: ',min(s))
    for i in range(0,5,1):
        if s[i] == max(s):
            s[i] = 0
        elif s[i] == min(s):
            s[i] = 0
    print('Média dos Demais Saltos: ',sum(s)/3)
    print('Resultado Final: ')
    print('{}: {}'.format(atleta,sum(s)/3))
    sis = int(input('Para entrar com o nome de outro atleta digite 1: '))

