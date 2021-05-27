cod = []
numV = []
numA = []
for i in range(0,5,1):
    codigo = str(input('Entre com o codigo da cidade: '))
    cod.append(codigo)
    numero_veiculos = int(input('Entre com o numero de veiculos de passeio: '))
    numV.append(numero_veiculos)
    numero_acidentes = int(input('Entre com o numero de acidentes com vitimas: '))
    numA.append(numero_acidentes)

maior_media_acidentes = max(numA)
menor_media_acidentes = min(numA)

for j in range(0,5,1):
    if maior_media_acidentes == numA[j]:
        print('A cidade {} tem o maior indice de acidentes de transito; {}'.format(cod[j],maior_media_acidentes))
    if menor_media_acidentes == numA[j]:
        print('A cidade {} tem o menor indice de acidentes de transito; {}'.format(cod[j],menor_media_acidentes))
soma = 0
for i in range(0,5,1):
    soma = soma + numV[i]
media = soma/5
print('A media de veiculos nas cidades é igual a ',media)
soma = 0
aux = 0
for i in range(0,5,1):
    if numV[i] < 2000:
        soma = soma + numA[i]
        aux = aux + 1 
media = soma/aux
print("A media de acidentes em cidades com menos de 2000 veiculos de passieo é igual à ",media)
