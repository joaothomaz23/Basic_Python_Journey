num = 1
so = []
print('Qual é o melhor sistema operacional para uso em servidores? ')
print('As possível respostas são: ')
print('1 - Windows Server')
print('2 - Unix')
print('3 - Linux')
print('4 - Netware')
print('5 - Mac OS')
print('6 - Outro')
while num != 0:
    num = int(input('Qual é o melhor sistema operacional? (Aperte 0 para sair) '))
    if num > 0 and num <= 6:
        so.append(num)
    else:
        print('Informe um valor valido, de 1 a 6, ou então 0 para sair!')
total = len(so)
windows = so.count(1)
wp = round((windows/total)*100,2)
unix = so.count(2)
up = round((unix/total)*100,2)
linux = so.count(3)
lp = round((linux/total)*100,2)
netware = so.count(4)
np = round((netware/total)*100,2)
mac = so.count(5)
mp = round((mac/total)*100,2)
outro = so.count(6)
op = round((outro/total)*100,2)
print('Sistema Operacional         Votos      %')
print('Windows Server                         {}        {}%'.format(windows,wp))
print('Linux                        {}        {}%'.format(unix,up))
print('Unix                         {}        {}%'.format(linux,lp))
print('Netware                      {}        {}%'.format(netware,np))
print('Mac Os                       {}        {}%'.format(mac,mp))
print('Outro                        {}        {}%'.format(outro,op))
print('Total                        {}       100%'.format(total))
so_all = [windows, unix, linux, netware, mac, outro] #Vetor que contem a quantidade de votos de cada SO
maior = max(so_all)
so_str = ['Windows Server','Unix','Linux','Netware','Mac Os','Outro']
for i in range(0,6,1):
    if maior == so_all[i]:
        print('O sistema operacional mais bem votados foi o {} com {} votos, que representam {}% do total'.format(so_str[i],maior,round((maior/total)*100,2)))
