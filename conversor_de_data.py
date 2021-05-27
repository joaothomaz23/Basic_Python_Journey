data = input('Entre com a data no formato DD/MM/AAAA: ')
def converteData(data,mes):
    a = 'A data posta foi: '+data[0]+data[1]+' de '+mes+' de '+data[6]+data[7]+data[8]+data[9]
    return a
if data[3] == '0' and data[4] == '1':
    mes = 'Janeiro'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '2':
    mes = 'Fevereiro'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '3':
    mes = 'Março'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '4':
    mes = 'Abril'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '5':
    mes = 'Maio'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '6':
    mes = 'Junho'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '0' and data[4] == '7':
    mes = 'Julho'
    aux = converteData(mes)
    print(aux)
elif data[3] == '0' and data[4] == '8':
    mes = 'Agosto'
    aux = converteData(mes)
    print(aux)
elif data[3] == '0' and data[4] == '9':
    mes = 'Setembro'
    aux = converteData(mes)
    print(aux)
elif data[3] == '1' and data[4] == '0':
    mes = 'Outubro'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '1' and data[4] == '1':
    mes = 'Novembro'
    aux = converteData(data,mes)
    print(aux)
elif data[3] == '1' and data[4] == '2':
    mes = 'Dezembro'
    aux = converteData(data,mes)
    print(aux)

