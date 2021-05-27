import random
v = ['azeite','goiaba','nóz','futebol','beteraba']
j = random.randint(0,4)
a = v[j]
b = []
for i in range(0,len(a),1):
    b.append(a[i])
random.shuffle(b)
c = ''
for i in range(0,len(b),1):
    c = c + b[i]
aux = 0
print('A palavra é: ',c)
while aux <=6:
    plv = input('Qual é a palavra? ')
    if plv == a:
        print('Voce acertou')
        aux = 7
    else:
        aux +=1
        print('Voce Errou!!!')
