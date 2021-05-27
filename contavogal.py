str = 'psaajjeepzxpiiiipp'
n = 2
ans = 0
aux = 0
for j in str:
    print()
    for i in range(0,n,1):
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            aux += 1
            print(aux)
            if aux == n:
                aux = 0
                ans += 1
            print('ans = ',ans)

print(ans)
