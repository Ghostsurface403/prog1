# 11. Elabore um programa que leia o preço da etiqueta de um produto e o código da condição de pagamento,
# calcule e imprima o valor a ser pago pelo cliente de acordo com a tabela a seguir:
#
# Código Condição de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 5% de desconto
# 3 Em duas vezes, preço normal da etiqueta sem juros
# 4 Em três vezes, preço normal da etiqueta mais juros de 5%

etiq = float(input('Digite o preço da etiqueta: '))
cod = int(input('Digite a condição de pagamento: '))

# valor a ser pago pelo cliente

if cod == 1:
    pag = etiq - (etiq * 0.10)
elif cod == 2:
    pag = etiq - (etiq * 0.05)
elif cod == 3:
    pag = etiq
elif cod == 4:
    pag = etiq + (etiq * 0.05)
else:
    print('Erro!')

print(pag)

