# 2) Um vendedor necessita de um programa que calcule o preço total devido
# por um cliente. O programa deve ler
# o código de um produto,
# a quantidade comprada,
# valor unitário e
# calcular o preço total de cada produto.
# Considere o último produto com o código igual a zero.

# codigo >0  and codigo <= 10
# quantidade >0  and codigo <= 10
# valor unitário >0  and codigo <= 10
# total =
#

total = 0
cod = 1
while cod != 0:
    cod = int(input('Digite o codigo: '))
    quant = int(input('Digite a quantidade: '))
    val = int(input('Digite o valor: '))
    total = total + val * quant
print('total = ',total)