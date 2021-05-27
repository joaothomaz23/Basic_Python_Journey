import random
d = []
print('Este programa roda um dado 100 vezes e conta quantas vezes ele caiu em cada um dos 6 lados')
for i in range(0,100,1):
    dado = random.randint(1,6)
    d.append(dado)
dado1 = d.count(1)
dado2 = d.count(2)
dado3 = d.count(3)
dado4 = d.count(4)
dado5 = d.count(5)
dado6 = d.count(6)
print('Lado 1: {}%'.format(dado1))
print('Lado 2: {}%'.format(dado2))
print('Lado 3: {}%'.format(dado3))
print('Lado 4: {}%'.format(dado4))
print('Lado 5: {}%'.format(dado5))
print('Lado 6: {}%'.format(dado6))
