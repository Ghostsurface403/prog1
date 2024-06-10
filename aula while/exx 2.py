# 2) Escreva um programa de calcule o somatório de 1 até n, onde n >= 1.

soma = 0
n = int(input('Digite o valor de N: '))
i = 1
while i <= n:
    soma = soma + i
    i = i + 1
print('somatório = ', soma)

n = 3
i = 1
soma = 1
i = 2
soma = 3
i = 3
soma = 6
i = 4
somatório é = 6
#
# n = 1
# while n >= 1:
#     n = int(input('Escreva um valor: '))
#     soma = n + 1
#     print(soma)
#     if n < 1:
#         print('acabou its over fim!')



# n= 1
# while n >= 1:
#     n = int(input('Escreva um valor: '))
#     soma = n + 1
#     print('O somatório é: ',soma)
