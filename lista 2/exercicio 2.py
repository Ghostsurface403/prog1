# Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

num = float(input('Digite um número: '))

if num % 3 == 0 and num % 7 == 0:
    print('O número é divisível por 3 e 7')

else:
    print('O número NÃO é divisível por 3 e 7')