# 13. Tendo como dados de entrada a altura (h) e o sexo de uma pessoa, construa um programa que calcule
# e imprima seu peso ideal, utilizando as seguintes fórmulas:
# ◆ para homens: (72.7*h) – 58;
# ◆ para mulheres: (62.1*h) – 44.7.



high = float(input('Insira sua altura: '))
sex = input('Insira seu sexo: ')

homem = (72.7 * high) - 58
mulher = (62.1 * high) - 44.7

if sex == homem:
    print(f'seu peso ideal é: {homem}')

else:
    print(f'seu peso ideal é: {mulher}')