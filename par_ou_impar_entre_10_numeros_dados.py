v = []
for i in range(10):
    num = int(input('Entre com um numero inteiro: '))
    v.append(num)
n_imp = 0
n_par = 0
for j in v:
    if j%2 != 0:
        n_imp = n_imp + 1
    else:
        n_par = n_par + 1
print('Existem %i números pares'%(n_par))
print('Existem %i números ímpares'%(n_imp))
