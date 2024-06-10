#1. Crie um programa que leia 20 valores e escreva o seu somatório.

soma = 0
for i in range(1,21,1):
    valor = int(input('Digite um valor: '))
    soma = soma + valor
print(soma)

