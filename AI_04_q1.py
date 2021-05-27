lista1 = [1,2,3,4]
lista2 = [8,1,4,1]
lista3 = []
for i in lista1:
    aux = i in lista2
    if aux == True:
        lista3.append(i)
        lista3.sort()
print(lista3)
