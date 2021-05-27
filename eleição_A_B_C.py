print('Nestas eleições vote no candidato A, B ou C!!!')
n = int(input('Entre com o número total de eleitores: '))
A = 0
B = 0
C = 0
for i in range(1,n+1,1):
    voto = str(input('Em qual candidato você pretende votar? '))
    if  voto == "A":
        A = A + 1
    elif voto == 'B':
        B = B + 1
    elif voto == 'C':
        C = C + 1
print('Houveram %i eleitores'%(n))
print('C = ',C)
print('B = ',B)
print('A = ',A)
