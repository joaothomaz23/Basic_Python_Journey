cpf = input('Entre com o seu CPF para a validação: ')
if len(cpf) == 14:
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        print('Tudo Limpo!')
    else:
        print('Acesso Negado! Formatação Incorreta')
else:
    print('Acesso Negado! Formação Incorreta')
