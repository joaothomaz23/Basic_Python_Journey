print('Este programa gera a sequência de fibonaci até o n-ésino!!!')
sf = 0
numA = 1
print(numA)
numB = 0
while sf <= 500:
    sf = numA + numB
    print(sf)
    numB = numA
    numA = sf
    
