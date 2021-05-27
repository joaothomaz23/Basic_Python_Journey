print('Enquete: Quem foi o melhor jogador? Escolha um número de 1 a 23')
aux = 1
x_all = []
v = []
while aux != 0:
   voto = int(input('Numero do Jogador (Aperte 0 para sair) : '))
   aux = voto
   if voto >= 1 and voto <= 23:
       v.append(voto)
   else:
       print('Informe um valor entre 1 e 23 ou 0 para sair!')
print('Foram computados {} votos'.format(len(v)))
for i in range(1,24,1):
    x = v.count(i)
    x_all.append(x)
    if x != 0:
        print('O jogador camisa {}, recebeu {} votos, ou seja, {}% do total de votos!'.format(i,x,round((x/len(v))*100,2)))
for i in range(1,24,1):
    if v.count(i) == max(x_all):
        print('O melhor jogador foi o número {}, com {} votos, ou seja, {}% do total de votos!'.format(i,max(x_all),round((v.count(i)/len(v))*100,2)))
