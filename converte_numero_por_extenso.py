num = input('Entre com um numero de 0 a 99: ')
v1 = ['Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove']
v2 = ['Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove']
v3 = ['Vinte','Trinta','Quarenta','Cinquenta','Sessenta','Setenta','Oitenta','Noventa']
if len(num) == 1:
    for i in range(0,len(v1)+1,1):
        if int(num) == i:
            print(v1[i-1])
else:
    if num[0] == '1':
        for i in range(0,len(v2),1):
           if int(num[1]) == i:
               print(v2[i])
    else:
        a = int(num[0])
        b = int(num[1])
        strg = v3[a-2] + ' e ' + v1[b-1]
        print(strg)
