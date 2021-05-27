v = []
aux = 1
acima = 0
sete = 0
while aux > 0:
    nota = float(input('Entre com o valor da nota: '))
    aux = nota
    v.append(nota)
v.pop()
print('Número de valores lidos: ',len(v))
print(v)
v.reverse()
print(v)
print('Soma dos valores: ',sum(v))
print('Media dos valores: ',sum(v)/len(v))
for i in v:
    if i > sum(v)/len(v):
        acima += 1
print('Número de valores acima da media: ',acima)
for i in v:
    if i < 7:
        sete += 1
print('Número de valores abaixo de sete: ',sete)
print('Sifude')
