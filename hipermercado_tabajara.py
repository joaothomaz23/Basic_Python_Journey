print('Digite 1 para File Duplo',
      '\nDigite 2 para Alcatra',
      '\nDigite 3 para Picanha')
tipo = int(input('Qual tipo de carne vc deseja? '))
kg = int(input('Quantos Kg de carne vc quer? '))
                  #FILE DUPLO
if tipo == 1:
    if kg <= 5:
        preco = round((kg*4.9),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round(preco - desconto,2)
            print('Tipo de carne: File Duplo')
            print('Quantidade de carne: ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: File Duplo')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
    else:
        preco = round((kg*5.8),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round((preco - desconto),2)
            print('Tipo de carne: File Duplo')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: File Duplo')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
                  #ALCATRA
elif tipo == 2:
    if kg <= 5:
        preco = round((kg*5.9),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round((preco - desconto),2)
            print('Tipo de carne: Alcatra')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: Alcatra')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
    else:
        preco = round((kg*6.8),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round((preco - desconto),2)
            print('Tipo de carne: Alcatra')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: Alcatra')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
                  #PICANHA
elif tipo == 3:
    if kg <= 5:
        preco = round((kg*6.9),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round((preco - desconto),2)
            print('Tipo de carne: Picanha')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: Picanha')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
    else:
        preco = round((kg*7.8),2)
        car = str(input('Possui cartão tabajara? Digite "Sim" ou "Não" '))
        if car == 'Sim':
            desconto = round((preco*0.05),2)
            preco_pago = round((preco - desconto),2)
            print('Tipo de carne: Picanha')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: ',desconto)
            print('Valor a ser pago',preco_pago)
        elif car == 'Não':
            print('Tipo de carne: Picanha')
            print('Quantidade de carne(Kg): ',kg)
            print('Preço Total',preco)
            print('Tipo de pagamento: Cartão Tabajara')
            print('Valor do desconto: R$0.00')
            print('Valor a ser pago',preco)
else:
    print('Valor Incorreto')
