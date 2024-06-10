# 2) Faça um programa que leia 25 números inteiros e calcule o somatório dos números pares lidos.

somapares = 0
for i in range(1,26):
    valor = float(input('Digite um valor: '))
    if valor % 2 == 0:
        somapares = somapares + valor
print('O somatório é = ', somapares)