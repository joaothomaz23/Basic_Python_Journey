print("ESTE PROGRAMA LE SUAS NOTAS E IRFORMA O SEU CONCEITO, MEDIA E EVENTUAL APROVAÇÃO")

nota1 = float(input("Entre com o valor da sua primeira nota: "))
nota2 = float(input("Entre com o valor da sua segunda nota: "))
media = (nota1+nota2)/2

if nota1 <= 10 and nota1 >=0 and nota2 <=10 and nota2 >= 0:   
    if media >= 9 and media <= 10:
        print("Sua primeira nota foi: ",nota1)
        print("Sua segunda nota foi: ",nota2)
        print("Sua media foi: ",media)
        print("Seu conceito foi A e você foi APROVADO")
    elif media >=7.5 and media < 9:
        print("Sua primeira nota foi: ",nota1)
        print("Sua segunda nota foi: ",nota2)
        print("Sua media foi: ",media)
        print("Seu conceito foi B e você foi APROVADO")
    elif media >=6 and media < 7.5:
        print("Sua primeira nota foi: ",nota1)
        print("Sua segunda nota foi: ",nota2)
        print("Sua media foi: ",media)
        print("Seu conceito foi C e você foi APROVADO")
    elif media >= 4 and media < 6:
        print("Sua primeira nota foi: ",nota1)
        print("Sua segunda nota foi: ",nota2)
        print("Sua media foi: ",media)
        print("Seu conceito foi D e você foi REPROVADO")
    elif media < 4 and media >= 0:
        print("Sua primeira nota foi: ",nota1)
        print("Sua segunda nota foi: ",nota2)
        print("Sua media foi: ",media)
        print("Seu conceito foi E e você foi REPROVADO")
else: print("Insira um valor de notas valido!!!")
