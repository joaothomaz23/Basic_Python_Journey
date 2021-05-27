sal = int(input('Insira o valor do seu salário inicial: '))
ano = int(input('Insira o ano em que você entrou na empresa: '))

delta_t = 2020 - ano
aumento = 0.015

for i in range(1,delta_t+1 , 1):
    print('O valor do salário em {} é igual à: {}'.format(ano+(i-1),sal))
    sal = sal + (sal*aumento)
    aumento = aumento*2
