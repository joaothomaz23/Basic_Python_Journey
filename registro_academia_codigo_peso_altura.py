cod = []
alt = []
kg = []
aux = 1
maior = 1
menor = 1
while aux != 0:
    codigo = int(input('Entre com seu codigo: '))
    if codigo == 0:
        aux = 0        
    cod.append(codigo)
    altura = float(input('Entre com a sua altura: '))
    alt.append(altura)
    peso = float(input('Entre com o seu peso: '))
    kg.append(peso)
maior_altura = max(alt)
menor_altura = min(alt)
maior_peso = max(kg)
menor_peso = min(kg)
for i in range(0,len(cod),1):
    if maior_altura == alt[i]:
        print('Maior Altura: {} - Cliente: {}'.format(maior_altura,cod[i]))
    if menor_altura == alt[i]:
        print('Menor Altura: {} - Cliente: {}'.format(menor_altura,cod[i]))
    if maior_peso == kg[i]:
        print('Maior Peso: {} - Cliente: {}'.format(maior_peso,cod[i]))
    if menor_peso == kg[i]:
        print('Menor Peso: {} - Cliente: {}'.format(menor_peso,cod[i]))
media_alt = round(sum(alt)/len(alt),2)
media_peso = round(sum(kg)/len(kg),2)
print('Média das Alturas: {}'.format(media_alt))
print('Média dos Pesos: {}'.format(media_peso))
