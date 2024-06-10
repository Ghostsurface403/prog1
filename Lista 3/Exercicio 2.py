# 2. Crie um programa que leia 6 números inteiros positivos e escreva o
# maior deles.

maior = -1
for i in range(1,7):
    valor = int(input('Insira um valor: '))
    if maior <= valor:
        maior = valor
print(maior)







# for i in range(1,3):
#     valor = int(input('Insira um valor: '))


# if a == b and a == c:
#     print(a)
# elif a > b and a > c:
#     print('O maior valor é: ', a)
# elif b > a and b > c:
#     print('O maior valor é: ', b)
# else:
#     print('O maior valor é: ', c)



# maior = -9999999
# for i in range(1,3):
#     valor = int(input('Insira um valor: '))
#     if maior <= valor:
#         maior = valor
#     print(maior)
