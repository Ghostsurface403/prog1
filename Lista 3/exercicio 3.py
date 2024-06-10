# 3. Escreva um programa que leia um conjunto de 20 números e mostre qual foi o maior e
# menor valor fornecido.

menor = 99
maior = 0
for i in range(1,5):
    num = int(input('Digite um número positivo: '))

    if maior <= num:
        maior = num

    if menor >= num:
        menor = num
print('O maior número é: ',maior)
print('O menor número é: ',menor)

