# 4) Dados 5 pares de valores inteiros a e b, distintos entre si, escreva um programa para imprimir o maior de cada par.

for i in range(1,6):
    a = int(input('Digite um valor para A: '))
    b = int(input('Digite um valor para B: '))
    if a >= b:
        print(a)
    else:
        print(b)