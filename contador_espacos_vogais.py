strg = input('Entre com umas string: ')
vog = 0
blank = 0
for i in strg:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vog += 1
    if i == ' ':
        blank += 1
print('Espaços em brnco: ',blank)
print('Vogais: ',vog)
    
