# 4. Crie um programa que leia um número inteiro positivo e encontre o fatorial deste
# número.

# num irá recber o numero do fatorial e fat começa com 1
# para não modificar o resultado na primeira multiplicação
num = int(input('Digite um número positivo: '))
fat = 1
# num = num * 3
# num = num * 2
# o loop irá rodar enquanto ele for maior que 1
# dentro do loop fat será igual a ele multiplicado  pelo numero do input,
while num > 1:
    fat = fat * num
    num = num - 1
print(fat)

# 4!  = 4 * 3 * 2
# 4 ! = fat
# fat = 4
# num = 3
# fat = 3
# num = 2
#