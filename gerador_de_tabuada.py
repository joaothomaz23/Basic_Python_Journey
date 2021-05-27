print('Gerador de Tabuada!!!!')
num = int(input('Entre com o número, de 1 à 10, cuja a tabuada você deseja saber: '))
print('Tabuada do %i'%(num))
for i in range(1,11,1):
    print('%i X %i = %i'%(num,i,num*i))
