n = int(input('Entre com um número inteiro: '))

def imprimir_piramide(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(j, end='\t')
        print('\n')
imprimir_piramide(n)
