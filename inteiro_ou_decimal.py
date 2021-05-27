num = float(input('Entre com um numero inteiro ou decimal: '))

num_round = round(num)

if num == num_round:
    print('Esse número é inteiro! ')
else:
    print('Esse número é decimal!')
