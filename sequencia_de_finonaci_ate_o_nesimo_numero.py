print('Este programa gera a sequência de fibonaci até o n-ésino!!!')
n = int(input('Entre com o valor de n-ésimo número: '))
numA = 1
print(numA)
numB = 0
for i in range(1, n+1,1):
    sf = numA + numB
    print(sf)
    numB = numA
    numA = sf

    
