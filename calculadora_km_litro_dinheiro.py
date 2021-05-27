print('Comparativo de Consumo de Combustível')
print(' ')
n = ['Fusca','Gol','Vectra','Uno','Peugeout']
km = [7,10,12.5,9,14.5]
for i in range(0,len(n),1):
    print('Veículo: ',i+1)
    print('Nome: ',n[i])
    print('Km por litro: ',km[i])
    print(' ')
for i in range(0,len(n),1):
    print('Relatório Final')
    print('{} - {} - {} - {} litros - R$ {}'.format(i,n[i],km[i],round(1000/km[i],2),round(2.25*(1000/km[i]),2)))
print(' ')
for i in range(0,len(n),1):
    if km[i] == max(km):
        print('O menor consumo pe do ',n[i])
