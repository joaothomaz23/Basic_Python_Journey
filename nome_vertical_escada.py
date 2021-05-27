nome = input('Entre com o seu nome: ')
for i in range(0,len(nome),1):
    s = ''
    for j in range(0,len(nome)-i,1):
        s = s + nome[j]   
    print(s)
