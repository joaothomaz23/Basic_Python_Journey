m3 = []
n=9
m5 = []
if n>=3:
    for i in range(0,n+1,1):
        mult3 = i%3
        if mult3 == 0:
            m3.append(i)
        mult5 = i%5
        if mult5 == 0:
            m5.append(i)  
    if max(m3) > max(m5):
        maior = max(m3)
    elif max(m5) > max(m3):
        maior = max(m5)
    else:
        maior = max(m3)
else:
    maior = 0
print(maior)
