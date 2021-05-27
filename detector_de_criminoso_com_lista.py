respostas = []
sim = 0
nao = 0
r1 = str(input('Telefonou para a vitima? '))
respostas.append(r1)
r2 = str(input('Esteve no local do crime? '))
respostas.append(r2)
r3 = str(input('Mora perto da vítima? '))
respostas.append(r3)
r4 = str(input('Devia para a vítima? '))
respostas.append(r4)
r5 = str(input('Já trabalhou com a vítima? '))
respostas.append(r5)
for i in respostas:
    if i == 'sim':
        sim += 1
if sim == 2:
    print('Suspeita')
elif sim >= 3 and sim <=4:
    print('Cumplice')
elif sim == 5:
    print('Assassino')
else:
    print('Inocente')
