# 1) Faça um programa que leia 15 números inteiros, um de cada vez, e calcule o somatório

soma = 0
for i in range(1,16):
    valor = float(input('Insira um valor: '))
    soma = soma + valor
print('O somatório é =', soma)

i = 0
while i <= 10:
    print(i)
    i = i + 1
print("terminou")


