aux = 0
m = []
while aux <= 10:
    aux += 1
    n = []
    print('====================================')
    for i in range(0,4,1):
        nota = float(input('Entre com o valor da nota: '))
        n.append(nota)
    media = sum(n)/4
    m.append(media)
aux = 0
for i in m:
    if i >= 7:
        aux += 1
print('O número de alunos com média maior ou igual a 7 é: ',aux)
        



    
