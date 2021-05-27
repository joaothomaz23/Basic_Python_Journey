aux = 0
while aux == 0:
    nome = str(input('Entre com o seu nome maior que 3 caracteres: '))
    if len(nome) > 3:
        aux = 1
    else:
        print('Nome Invalido!')
aux = 0
while aux == 0:
    idade = int(input('Entre com a sua idade, entre 0 e 150 anos: '))
    if idade >= 0 and idade <= 150:
        aux = 1
    else:
        print('Idade Invalida!')
aux = 0
while aux == 0:
    salario = int(input('Qual o seu salário? [Digite somente valores maiores do que zero] '))
    if salario > 0:
        aux = 1
    else:
        print('Salário Invalido!')
aux = 0
while aux == 0:
    sexo = str(input('Qual o seu sexo? [f ou m] '))
    if sexo == 'f' or sexo == 'm':
        aux = 1
    else:
        print('Sexo Inválido')
aux = 0
while aux == 0:
    EC = str(input('Qual o seu estado civil? [s,c,v ou d] '))
    if EC == 's' or EC == 'c' or EC == 'v' or EC == 'd':
        aux = 1
    else:
        print('Estado Civil Inválido')
