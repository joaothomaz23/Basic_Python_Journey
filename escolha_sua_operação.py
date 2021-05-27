num1 = int(input('Entre com um número real: '))
num2 = int(input('Entre com outro número real: '))

print('\nDigite 1 para verificar de os números são ímpares ou pares',
      '\nDigite 2 para verificar se são negativos ou positivos ',
      '\nDigite 3 para verificar se são inteiros ou decimais',
      '\nDigite qualquer outra coisa para sair do programa')

aux = int(input('Qual operação você deseja realizar: '))

if aux == 1:
    pi1 = num1%2
    if pi1 == 0:
        print("O número %i é par!"%(num1))
    else:
        print('O número %i é impar!'%(num1))
    pi2 = num2%2
    if pi2 == 0:
        print("O número %i é par!"%(num2))
    else:
        print('O número %i é impar!'%(num2))
elif aux == 2:
    if num1 > 0:
        print('O número %i é positivo!'%(num1))
    elif num1 < 0:
        print('O número %i é negativo!'%(num1))
    else:
        print('O número zero')
    if num2 > 0:
        print('O número %i é positivo!'%(num2))
    elif num2 < 0:
        print('O número %i é negativo!'%(num2))
    else:
        print('O número zero')
elif aux == 3:
    if num1 == round(num1):
        print('O número %i é inteiro!'%(num1))
    else:
        print('O número %i é decimal!'%(num1))
    if num2 == round(num2):
        print('O número %i é inteiro!'%(num2))
    else:
        print('O número %i é decimal!'%(num2))
else:
    print('Adeus!!')
    
