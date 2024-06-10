# 9. Construa um programa que calcule e imprima a média aritmética de vários valores
# inteiros positivos, lidos externamente. O final da leitura acontecerá quando for lido um
# valor negativo.

som = 0
num = 0
lido = 0

while num >= 0:
    num = int(input('Digite um valor: '))

    if num < 0:
        break

    som += num
    if num != 0:
        lido += 1

if lido == 0:
    print('A média é 0')
else:
    media = som / lido
    print('A média é = ', media)
