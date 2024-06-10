# Faça um programa que leia um número qualquer. Caso o número seja par menor que 10, escreva ‘Número
# parmenor que Dez’, caso o número digitado seja ímpar menor que 10 escreva ‘Número Ímpar menor que Dez’,
# caso contrário Escreva ‘Número fora do Intervalo’.

num = float(input('digite um número: '))

if num < 10 and num % 2 == 0:
    print('Número par menor que Dez')

if num < 10 and num % 2 == 1:
    print('Número Ímpar menor que Dez')

else:
    print('Número fora do Intervalo')


