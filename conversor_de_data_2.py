data = input('Data de Nascimento: ')
if data[3] == '0' and data[4] == '1':
    mes = 'Janeiro'
    
elif data[3] == '0' and data[4] == '2':
    mes = 'Fevereiro'
    
elif data[3] == '0' and data[4] == '3':
    mes = 'Março'
    
elif data[3] == '0' and data[4] == '4':
    mes = 'Abril'
    
elif data[3] == '0' and data[4] == '5':
    mes = 'Maio'
    
elif data[3] == '0' and data[4] == '6':
    mes = 'Junho'
   
elif data[3] == '0' and data[4] == '7':
    mes = 'Julho'
   
elif data[3] == '0' and data[4] == '8':
    mes = 'Agosto'
   
elif data[3] == '0' and data[4] == '9':
    mes = 'Setembro'
    
elif data[3] == '1' and data[4] == '0':
    mes = 'Outubro'
    
elif data[3] == '1' and data[4] == '1':
    mes = 'Novembro'
    
elif data[3] == '1' and data[4] == '2':
    mes = 'Dezembro'

a = 'Você nasceu em '+data[0]+data[1]+' de '+mes+' de '+data[6]+data[7]+data[8]+data[9]
print(a)
