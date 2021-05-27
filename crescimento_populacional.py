aux = 0
i = 0
a = int(input('Qual a população da primeira cidade? '))
b = int(input('Qual a população da segunda cidade? '))
taxA = float(input('Qual o valor, em decimal, da taxa de crescimento anual da primeira cidade?'))
taxB = float(input('Qual o valor, em decimal, da taxa de crescimento anual da segunda viagem?'))
while aux == 0:
    a = (a*taxA) + a
    b = (b*taxB) + b
    print(a)
    print(b)
    print(i)
    i += 1
    if a == b:
        aux = 1
else:
    print('A população das duas cidades demorou %i para se igualar!'%(i))
