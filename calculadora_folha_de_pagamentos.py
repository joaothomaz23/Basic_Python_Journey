print("Esse programa calcula uma folha de pagamento!")

valor_hora = int(input("Qual o valor da sua hora, em Reais? "))
hora = int(input("Quantas horas voce trabalhou? "))
sal_bru = valor_hora*hora

if sal_bru <= 900:
    irp = 0
    ir = 0
    sind = (sal_bru*3)/100
    inss = (sal_bru*10)/100
    fgts = (sal_bru*11)/100
    total_desc = ir + sind + inss + fgts
    sal_liq = sal_bru - total_desc
elif sal_bru > 900 or sal_bru <= 1500:
    irp = 5
    ir = (sal_bru*5)/100
    sind = (sal_bru*3)/100
    inss = (sal_bru*10)/100
    fgts = (sal_bru*11)/100
    total_desc = ir + sind + inss + fgts
    sal_liq = sal_bru - total_desc
elif sal_bru > 1500 or sal_bru <= 2500:
    irp = 10
    ir = (sal_bru*10)/100
    sind = (sal_bru*3)/100
    inss = (sal_bru*10)/100
    fgts = (sal_bru*11)/100
    total_desc = ir + sind + inss + fgts
    sal_liq = sal_bru - total_desc
else:
    irp = 20
    ir = (sal_bru*20)/100
    sind = (sal_bru*3)/100
    inss = (sal_bru*10)/100
    fgts = (sal_bru*11)/100
    total_desc = ir + sind + inss + fgts
    sal_liq = sal_bru - total_desc

print("Valor/Hora: %i | Horas Trabalhadas: %i | Salário Bruto (VH*HT): %i "%(valor_hora,hora,sal_bru))
print("Imposto de Renda (%i): %i"%(irp,ir))
print("INSS (10%): ",inss)
print("FGTS (11%): ",fgts)
print("Sindicato (3%)",sind)
print("Total de Desontos: ",total_desc)
print("Salário Líquido: ",sal_liq)
