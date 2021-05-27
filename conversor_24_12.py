aux = 0
def conversor(h,m):
    if h>12:
        h = h - 12
        print('{}:{} P.M.'.format(h,m))
    else:
        print('{}:{} A.M.'.format(h,m))
while aux == 0:
    horas = int(input('Entre com o valor das horas: '))
    minutos = int(input('Entre com o valor dos minutos: '))
    conversor(horas,minutos)
    aux = int(input('Digite 0 para continuar a conversão ou 1 para sair: '))
    
