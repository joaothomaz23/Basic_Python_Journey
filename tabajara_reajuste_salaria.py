print("Ente programa ira lhe atualizar a respeito de suas informações salariais!")

sal = int(input("Entre com o valor atual do seu salario: "))
if sal < 280:
    aum = (sal*20)/100
    aump = "20%"
    new_sal = sal+aum
elif sal >= 280 or sal <= 700:
    aum = (sal*15)/100
    aump = "15%"
    new_sal = sal+aum
elif sal > 700 or sal < 1500:
    aum = (sal*10)/100
    aump = "10%"
    new_sal = sal+num
elif sal >= 1500:
    aum = (sal*5)/100
    aump = "5%"
    new_sal = sal+num

print("Seu salário antes do reajuste e de %i Reais"%(sal))
print("Voce recebeu um aumento percentual de: ",aump)
print("O valor do aumento é de %i Reais"%(aum))
print("O novo salário após o aumento é de %i Reais"%(new_sal))
