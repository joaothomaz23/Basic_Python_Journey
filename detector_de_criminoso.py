print('Responda EXATAMENTE "Sim" ou "Não" para as perguntas abaixo')
p1 = str(input('Telefonou para a vítima? '))
p2 = str(input('Esteve no local do crime? '))
p3 = str(input('Mora perto da vítima? '))
p4 = str(input('Devia para a vítima? '))
p5 = str(input('Já trabalhou com a vítima? '))

if p1 == 'Sim':
    p1 = 1
elif p1 == 'Não':
    p1 = 0
    
if p2 == 'Sim':
    p2 = 1
elif p2 == 'Não':
    p2 = 0

if p3 == 'Sim':
    p3 = 1
elif p3 == 'Não':
    p3 = 0

if p4 == 'Sim':
    p4 = 1
elif p4 == 'Não':
    p4 = 0

if p5 == 'Sim':
    p5 = 1
elif p5 == 'Não':
    p5 = 0

p = p1 + p2 + p3 + p4 + p5

if  p == 2:
    print('Supeita!')
elif p > 2 and p <= 4:
    print('Cúmplice!')
elif p == 5:
    print('Assassino!')
else:
    print('Inocente!')
