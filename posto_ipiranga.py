print('BEM-VINDO AO POSTO IPIRANGA!!')
print('O PREÇO DO LITRO DO ÁLCOOL É R$ 1.90 E DA GALOSINA É R$ 2.50')
combustivel = str(input('Digite "A" se vc quer abastecer com álcool ou "G" se você quer abastecer com gasolina: '))
litros = float(input('Quantos litros você deseja abastecer? '))

if combustivel == 'A':
    if litros <= 20:
        desconto =1.9*(3/100)
    elif litros > 20:
        desconto = 1.9*(5/100)
    preco = litros*(1.9 - desconto)
    print('Você irá pagar R$ ',round(preco,2))
elif combustivel == 'G':
    if litros <= 20:
        desconto = 2.5*(4/100)
    elif litros > 20:
        desconto = 2.5*(6/100)
    preco = litros*(2.5 - desconto)
    print('Você irá pagar R$ ',round(preco,2))
else:
    print('Insira uma valor válido')
