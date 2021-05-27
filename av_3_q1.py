n = 21
soma = 0
s = []
for i in range(1,n,1):
    if n%i == 0:
        print(i)
        print(i%n)
        soma += i

print(soma)
