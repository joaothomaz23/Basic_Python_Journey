print('Bem-Vindo a minha barraquinha de frutas!!')
print('Morango: Até 5 Kg ==> R$ 2.50 por Kg | Acima de 5 Kg ==> R$ 2.20 por Kg')
print('Maçâ: Até 5 Kg ==> R$ 1.80 por Kg | Acima de 5 Kg ==> R$ 1.50 por Kg')
print('Mais de 8 kilos ou R$ 25.00 em compras e vc ganha 10% de desconto sobre o preço total a ser pago')

morango = float(input('Entre com a quantidade em quilos de morangos comprados: '))
maca = float(input('Entre com a quantidade em quilos de maçãs comprados: '))

if morango <= 5:
    preco_morango = morango*2.50
elif morango > 5:
    preco_morango = morango*2.20
if maca <= 5:
    preco_maca = maca*1.80
elif maca > 5:
    preco_maca = maca*1.50

preco_total = preco_morango + preco_maca
kg_total = morango + maca

if kg_total > 8 or preco_total > 25:
     preco_total = preco_total - (preco_total*(10/100))
     print('O preço total a ser pago é: R$ ',round(preco_total,2))
else:
    print('O preço total a ser pago é: R$ ',round(preco_total,2))
    
