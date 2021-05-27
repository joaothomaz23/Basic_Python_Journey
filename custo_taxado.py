imposto = float(input('Entre com o valor do imposto sobre a venda: (Em porcentagem)'))
custo = float(input('Entre com o custo de cada venda, sem imposto somado: '))
def somaimposto(imposto, custo):
    custo_taxado = custo + (custo*(imposto/100))
    return custo_taxado
x = somaimposto(imposto,custo)
print(x)

