print("DESCUBRA SE UM DETERMINADO ANO É BISSEXTO")
ano = int(input("Entre com um ano aleátorio: "))

resto4 = ano%4
resto100 = ano%100
resto400 = ano%400

if resto100 == 0:
    if resto400 == 0:
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")
else:
    if resto4 == 0:
        print('Esse ano é bissexto')
    else:
        print('Esse ano não é bissexto')
