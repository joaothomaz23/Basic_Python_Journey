i = []
a = []
for n in range(0,5,1):
    idade = int(input('Entre com a sua idade: '))
    i.append(idade)
    altura = float(input('Entre com a sua altura, em CM:'))
    a.append(altura)
print('Idade na ordem lida: ')
print(i)
print('Altura na ordem lida:')
print(a)
i.reverse()
a.reverse()
print('Idade com a ordem invertida: ')
print(i)
print('Altura com a ordem invertida: ')
print(a)
