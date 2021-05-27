print('Este programa é uma calculadora de fatoriais!')
n = int(input('Informe o valor do faltorial a ser calculado: '))
fat = 1
for i in range(n,0,-1):
    fat = fat*i
print(fat)
    
