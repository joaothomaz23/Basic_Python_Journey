n = int(input('Entre com o número de produtos: '))
preco = 0
print('Lojas Quase Dois - Tabela de Preços')
for i in range(1,n+1,1):
    preco = preco + 1.99
    aux = str(round(preco,2))
    print('%i - R$ %s'%(i,aux))
