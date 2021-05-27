print("Este programa informa as centenas, dezenas e unidades de um numero inteiro menor que mil")

num = str(input("Entre com um numero inteiro menor que mil: "))

if len(num) <= 3:
    if len(num) == 3: #100 ate 900
        if num[0] == '1' or num[1] == '1' or num[2] == '1':
            if num[0] == '1' and num[1] != '1' and num[2] == '1':
                print("%s = %s centena, %s dezenas e %s unidade"%(num,num[0],num[1],num[2]))
            elif num[0] == '1' and num[1] == '1' and num[2] != '1':
                print("%s = %s centena, %s dezena e %s unidades"%(num,num[0],num[1],num[2]))
            elif num[0] != '1' and num[1] == '1' and num[2] == '1':
                print("%s = %s centenas, %s dezena e %s unidade"%(num,num[0],num[1],num[2]))
            elif num[0] == '1' and num[1] == '1' and num[2] == '1':
                print("%s = %s centena, %s dezena e %s unidade"%(num,num[0],num[1],num[2]))
            elif num[1] == '1' and num[2] == '1':
                print("%s = %s centenas, %s dezenas e %s unidade"%(num,num[0],num[1],num[2]))
            elif num[1] == '1':
                print("%s = %s centenas, %s dezena e %s unidades"%(num,num[0],num[1],num[2]))
            elif num[0] == '1':
                print("%s = %s centena, %s dezenas e %s unidades"%(num,num[0],num[1],num[2]))
        else:
            print("%s = %s centenas, %s dezenas e %s unidades"%(num,num[0],num[1],num[2]))
    elif len(num) == 2 and num[0] == "1": #10 ate 19
        if num[1]== '1':
            print("%s = %s dezena e %s unidade"%(num,num[0],num[1]))
        else:
            print("%s = %s dezena e %s unidades"%(num,num[0],num[1]))            
    elif len(num) == 2 and num[0] != "1": #20 ate 99
        if num[1] == '1':
            print("%s = %s dezenas e %s unidade"%(num,num[0],num[1]))
        else:
            print("%s = %s dezenas e %s unidades"%(num,num[0],num[1]))
    elif len(num) == 1: #0 ate 9
        if num == "1":
            print("%s = %s unidade"%(num,num))
        else:
            print("%s = %s unidades"%(num,num))
else:
    print("Número inválido")
