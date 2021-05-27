n = 15
p = 3
auxN = 1
for i in range(n,0,-1):
    auxN = auxN*i
    auxP = 1
for i in range(p,0,-1):
    auxP = auxP*i
    auxNP = 1
for i in range(n-p,0,-1):
    auxNP = auxNP*i
c = auxN/(auxP*auxNP)
print(c)
