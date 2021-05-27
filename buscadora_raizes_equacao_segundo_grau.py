import math
print("ESSE PROGRAMA ENCONTRA AS RAIZES DE QUALQUER EQUACAO DO SEGUNDO GRAU: ")

a = float(input("Entre com o valor do coeficiente A: "))
b = float(input("Entre com o valor do coeficiente B: "))
c = float(input("Entre com o valor do coeficiente C: "))

delta = b**2 - (4*a*c)

if a == 0:
    print("Se o coeficiente A é igual a zero, então não se trata de uma equação do segundo grau, informe um coeficiente valido")
else:
    if delta < 0:
        print("A equação em questão não possui raízes")
    elif delta == 0:
        raiz = (-b + math.sqrt(delta))/(2*a)
        print("A equação em questão possui apenas uma raíz, que é: ",raiz)
    elif delta > 0:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        print("A equação em qustão possui duas raizes, que são %f e %f"%(raiz1,raiz2))
