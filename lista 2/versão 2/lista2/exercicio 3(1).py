# Construa um programa que LEIA o preço e o código de origem do
# produto e IMPRIMA seu preço e sua procedência, de acordo com a tabela abaixo.
# Caso o código não seja nenhum dos especificados, o produto
# deve ser encarado como 'importado'. Se o produto for importado, deverá também ser calculado e apresentado
# o preço acrescido de 15%, correspondente ao imposto de importação.

# Código Procedência
# 1 Sudeste
# 2 Sul
# 3 Centro-Oeste
# 4 Nordeste
# 5 Norte




codigo = int(input('Insira o codigo de acordo com o produto: '))
preco = int(input('Insira o preço do produto: '))
if codigo == 1:
    print('procedência: sudeste preço: ',preco)
elif codigo == 2:
    print('procedência: sul preço: ',preco)
elif codigo == 3:
    print('procedência: Centro-Oeste preço: ',preco)
elif codigo == 4:
    print('procedência: Nordeste preço: ',preco)
elif codigo == 5:
    print('procedência: Norte preço: ',preco)
else:
    preco = preco * 0.15 + preco
    print('Produto Importado preço: ',preco)


