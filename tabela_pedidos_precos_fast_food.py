print('Especificação   Código   Preço')
print('Cachorro Quente 100      R$ 1.20')
print('Bauru Simples   101      R$ 1.30')
print('Bauru com Ovo   102      R$ 1.50')
print('Hambúrguer      103      R$ 1.30')
print('Cheeseburguer   104      R$ 1.30')
print('Refrigerante    105      R$ 1.00')

cod = []
q = []
aux = 0
while aux == 0:
    codigo = int(input('Entre com o código do seu pedido: '))
    cod.append(codigo)
    quantidade = int(input('Entre com a quantidade da opção escolhida: '))
    q.append(quantidade)
    aux = int(input('Digite 0 para continuar o pedido ou 1 para encerrar: '))
total = 0
print(cod)
print(q)
for i in range(0,len(cod),1):
    if cod[i] == 100:
        preco = 1.20*q[i]
        total = total + preco
    elif cod[i] == 101:
        preco = 1.30*q[i]
        total = total + preco 
    elif cod[i] == 102:
        preco = 1.50*q[i]
        total = total + preco
    elif cod[i] == 103:
        preco = 1.20*q[i]
        total = total + preco
    elif cod[i] == 104:
        preco = 1.30*q[i]
        total = total + preco
    elif cod[i] == 105:
        preco = 1.00*q[i]
        total = total + preco
    print('A')
print('O total a ser pago é R$ ',total)
