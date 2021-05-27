divida = float(input('Entre com a sua divida: '))
print('Quatidade de Parcelas ======= Porcentagem de Juros sobre o Valor Inicial da Dívida')
print('1 ----------------------------------------------------- 0 ')
print('3 ---------------------------------------------------- 10 ')
print('6 ---------------------------------------------------- 15 ')
print('9 ---------------------------------------------------- 20 ')
print('12 --------------------------------------------------- 25 ')

parcela = [1,3,6,9,12]
print('Valor da Divida Valor dos Juros Quantidade de Parcelas Valor da Parcela')
for i in range(0,5,1):
    if parcela[i] == 1:
        juros = 0
        print('R$ {}           {}             {}                      R${}'.format(divida,0,parcela[i],round(divida/parcela[i],2)))
    if parcela[i] == 3:
        juros = 0.1
        print('R$ {}           {}             {}                      R${}'.format(divida,divida*juros,parcela[i],round(divida/parcela[i],2)))
    if parcela[i] == 6:
        juros = 0.15
        print('R$ {}           {}             {}                      R${}'.format(divida,divida*juros,parcela[i],round(divida/parcela[i],2)))
    if parcela[i] == 9:
        juros = 0.20
        print('R$ {}           {}             {}                      R${}'.format(divida,divida*juros,parcela[i],round(divida/parcela[i],2)))
    if parcela[i] == 12:
        juros = 0.25
        print('R$ {}           {}             {}                      R${}'.format(divida,divida*juros,parcela[i],round(divida/parcela[i],2)))
        
        
