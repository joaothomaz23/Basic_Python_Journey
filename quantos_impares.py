n = int(input('N: '))
m = int(input('M: '))
cont = 0
for i in range(n+1,m,1):
    if i%2 != 0:
        cont += 1
print(cont)
