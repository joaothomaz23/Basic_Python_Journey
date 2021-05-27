s = []
aux = 1
a = []
while aux != 0:
    salario = float(input('Entre com seu salário bruto de Dezembro: (Aperte 0 para sair)'))
    s.append(salario)
    aux = salario
s.pop()
print('Salário       Abono')
m = 0
for i in s:
    if i < 1000:
        abono = 100
        a.append(abono)
        m += 1
        print('R$ {}     R$ {}'.format(i,abono))
    else:
        abono = i*0.2
        a.append(abono)
        print('R$ {}     R$ {}'.format(i,abono))
print('Foram processados {} colaboradores'.format(len(s)))
print('Total gasto em abonos: R$ ',sum(a))
print('Valor mínimo pago a {} colaboradores'.format(m))
print('Maior valor de abono pago: R$ ',max(a))
