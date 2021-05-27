d = []
aux = 1
print('Número de Identificação      Defeito     ')
print('        1                    Necessita de Esfera')
print('        2                    Necessita de Limpeza')
print('        3                    Necessita de Troca De Cabo ou Conector')
print('        4                    Quebrado ou Inutilizado')
print(' ')
while aux != 0:
    defeito = int(input('Qual é o tipo de defeito do mouse: (Precione 0 para sair) '))
    d.append(defeito)
    aux = defeito
d.pop()
def1 = (d.count(1)/len(d))*100 #defeito1
def2 = (d.count(2)/len(d))*100 #defeito2
def3 = (d.count(3)/len(d))*100 #defeito3
def4 = (d.count(4)/len(d))*100 #defeito4
print('  ')
print('Quantidade de Mouses: ',len(d))
print('  ')
print('Situação                                           Quantidade          Percentual')
print('1 - Necessita de Esfera                                {}                  {}%'.format(d.count(1),def1))
print('2 - Necessita de Limpeza                               {}                  {}%'.format(d.count(2),def2))
print('3 - Necessita de Troca de Cabo ou Conector             {}                  {}%'.format(d.count(3),def3))
print('4 - Necessita de Esfera                                {}                  {}%'.format(d.count(4),def4))
