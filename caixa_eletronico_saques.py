print("Este é o sistema operacional de um caixa eletronico")

valor = int(input('Entre com o valor que deseja sacar (Somente valor entre R$ 10.00 e R$ 600.00)'))

if valor >= 10 and valor <= 600:
    if valor >= 100 and valor <= 600:
        centenas_valor = int(valor/100)
        print('Serão %i notas de 100'%(centenas_valor))
        valor = valor - (centenas_valor*100)
        if valor >= 50:
            cinquentas_valor = int(valor/50)
            valor = valor - 50
            print('Serão %i notas de 50'%(cinquentas_valor))
            if valor >= 10:
                dez_valor = int(valor/10)
                valor = valor - (dez_valor*10)
                print('Serão %i notas de 10'%(dez_valor))
                if valor >= 5:
                    cinco_valor = int(valor/5)
                    valor = valor - 5
                    print('Serão %i notas de 5'%(cinco_valor))
                    print('Serão %i notas de 1'%(valor))
                elif valor < 5:
                    print('Serão %i notas de 1'%(valor))
                    if valor >= 5:
                        cinco_valor = int(valor/5)
                        valor = valor - 5
                        print('Serão %i notas de 5'%(cinco_valor))
                        print('Serão %i notas de 1'%(valor))
                    elif valor < 5:
                       print('Serão %i notas de 1'%(valor))
        elif valor < 50:
            dez_valor = int(valor/10)
            valor = valor - (dez_valor*10)
            print('Serão %i notas de 10'%(dez_valor))
            if valor >= 5:
                cinco_valor = int(valor/5)
                valor = valor - cinco_valor
                print('Serão %i notas de 5'%(cinco_valor))
                print('Serão %i notas de 1'%(valor))
            elif valor < 5:
                print('Serão %i notas de 1'%(valor))
    elif valor < 100:
        if valor >= 50:
            cinquentas_valor = int(valor/50)
            valor = valor - 50
            print('Serão %i notas de 50'%(cinquentas_valor))
            if valor >= 10:
                dez_valor = int(valor/10)
                valor = valor - (dez_valor*10)
                print('Serão %i notas de 10'%(dez_valor))
                if valor >= 5:
                    cinco_valor = int(valor/5)
                    valor = valor - 5
                    print('Serão %i notas de 5'%(cinco_valor))
                    print('Serão %i notas de 1'%(valor))
                elif valor < 5:
                    print('Serão %i notas de 1'%(valor))
                    if valor >= 5:
                        cinco_valor = int(valor/5)
                        valor = valor - 5
                        print('Serão %i notas de 5'%(cinco_valor))
                        print('Serão %i notas de 1'%(valor))
                    elif valor < 5:
                       print('Serão %i notas de 1'%(valor))
        elif valor < 50:
            dez_valor = int(valor/10)
            valor = valor - (dez_valor*10)
            print('Serão %i notas de 10'%(dez_valor))
            if valor >= 5:
                cinco_valor = int(valor/5)
                valor = valor - cinco_valor
                print('Serão %i notas de 5'%(cinco_valor))
                print('Serão %i notas de 1'%(valor))
            elif valor < 5:
                print('Serão %i notas de 1'%(valor))
else:
    print("Entre com um valor de saque válido!!!!!")
