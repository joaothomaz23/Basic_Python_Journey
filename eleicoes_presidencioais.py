voto = 1
print('ELEIÇÕES PRESIDENCIAIS!!')
print('Digite: ')
print('1 - João')
print('2 - José')
print('3 - Dilma')
print('4 - Lúcia')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('0 - Encerrar a Votação')
v = []
while voto != 0:
    voto = int(input('Entre com o seu voto: '))
    v.append(voto)
joao = 0
jose = 0
dilma = 0
lucia = 0
nulo = 0
branco = 0
for i in range(0,len(v),1):
    if v[i] == 1:
        joao = joao + 1
    elif v[i] == 2:
        jose = jose + 1
    elif v[i] == 3:
        dilma = dilma + 1
    elif v[i] == 4:
        lucia = lucia + 1
    elif v[i] == 5:
        nulo = nulo + 1
    elif v[i] == 6:
        branco = branco + 1
votos_totais = len(v)
nulos_100 = (nulo/votos_totais)*100
brancos_100 = (branco/votos_totais)*100
print('Joao: {} votos'.format(joao))
print('José: {} votos'.format(jose))
print('Dilma: {} votos'.format(dilma))
print('Lúcia: {} votos'.format(lucia))
print('Nulos: {} votos'.format(nulo))
print('Brancos: {} votos'.format(branco))
print('Percentual de Nulos: {}%'.format(round(nulos_100,2)))
print('Percentual de Brancos: {}%'.format(round(brancos_100,2)))
