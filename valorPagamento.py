def valorPagamento(prestacao,atraso):
    if atraso != 0:
        valor = prestacao+(prestacao*0.03)+ (prestacao*(atraso*0.001))
    else:
        valor = prestacao
    return valor
v = []
aux = 1
while aux != 0:
    prestacao = float(input('Entre com o valor, em reais, de cada prestação: '))
    aux = prestacao
    atraso = int(input('Entre com o número de dias de pagamento em atraso: '))
    valor = valorPagamento(prestacao,atraso)
    v.append(valor)
    print('O valor da parcela paga foi: R$ {}'.format(valor))
v.pop()
print('  ')
print('Relatório do Dia!')
print('Número de Prestações Pagas: {}'.format(len(v)))
print('Valor Total Pago no Dia: {} '.format(sum(v)))
