print('Este programa imprime todos os valores inteiros compreendidos dentro do intervalo dado')
num1 = int(input('Entre com o primeiro valor do intervalo: '))
num2 = int(input('Entre com o último  valor do intervalo: '))
soma = 0
for i in range(num1,num2+1,1):
    print(i)
    soma = soma + i
print(soma)
