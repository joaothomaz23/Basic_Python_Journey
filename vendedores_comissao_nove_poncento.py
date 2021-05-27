v = []
s = []
j = [200,299,300,399,400,499,500,599,600,699,700,799,800,899,900,999,1000]
n = int(input('Entre com o número de vendedores da loja: '))
for i in range(0,n,1):
    vendas = float(input('Entre com o valor em dinheiro das suas vendas na semana: '))
    v.append(vendas)
    salario = 200 + (vendas*0.09)
    s.append(salario)
for k in range(0,len(s),1):
    for i in range(0,17,2):
        if i != 16:
            if s[k] >= j[i] and s[k] <= j[i+1]:
                print('Um vendedor, recebeu entre {} e {} reais de comissão nessa semana! '.format(j[i],j[i+1]))        
        elif i == 16:
            if s[k] > 1000:
                print('Um vendedor, recebeu entre {} e {] reais de comissão nessa semana! '.format(j[i],j[i+1]))
   

    
