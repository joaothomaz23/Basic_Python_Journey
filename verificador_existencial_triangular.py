print("ESSE PROGRAMA VERIFICA SE UM TRIANGULO EXISTE DE ACORDO COM O COMPRIMENTO DE SEUS LADOS")

a = float(input("Entre com o primeiro lado: "))
b = float(input("Entre com o segundo lado: "))
c = float(input("Entre com o terceiro lado: "))

modA = abs(b - c)
modB = abs(a - c)
modC = abs(a - b)

somaA = b + c
somaB = a + c
somaC = a + b

if a > modA and a < somaA and b > modB and b < somaB and c > modC and c < somaC:
    print("O TRIANGULO EXISTE")
    if a == b and b == c:
        print("O TRIANGULO E EQUILATERO")
    elif a != b and b != c:
        print("O TRIANGULO E ESCALENO")
    else:
        print("O TRIANGULO E ISOCELES")
else:
    print("O TRIANGULO NÃO EXISTE")
