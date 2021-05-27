nome = input('Entre com o seu nome: ')
s = ''
for i in range(len(nome)-1,-1,-1):
    s = s + nome[i]
    print(s)
print(s)
