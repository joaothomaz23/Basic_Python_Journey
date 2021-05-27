print('CAIXA REGISTRADORA 1.0')
produto = 1
v = []
aux = 0
total = 0
while produto != 0:
    produto = float(input('Entre com o valor do produto: '))
    v.append(round(produto,2))
print('Lojas Tabajara')
for i in range(0,len(v),1):
    print('Produto {}: R$ {}'.format(i+1,v[i]))
    total = total + v[i]
dinheiro = float(input('Com quanto dinheiro cliente pagou? '))
print('Total: R$',total)
print('Dinheiro: R$',dinheiro)
troco = dinheiro - total 
print('Troco: R$', troco)
