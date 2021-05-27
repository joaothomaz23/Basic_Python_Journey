aux = 0
arq = open('alice.txt')
for linha in arq:
    for i in linha:
        if i == str:
            aux += 1
print(aux)
