n = int(input('Entre com um inteiro: '))
den = 1
s = 1
for i in range(2,n+1,1):
    den = den + 2    
    s = s + i/den
print(s)
