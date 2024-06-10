# 4. Crie um programa que leia um número e imprima a raiz quadrada do número caso ele seja positivo
# e o quadrado do número caso ele seja negativo.
# Obs. Não se esqueça de tratar o caso do número ser igual a zero.
import math

num = float(input('Insira um número: '))

if num > 0:
    num = math.sqrt(num)
    print(num)

if num == 0:
    print('Erro!')

else:
    num = num * num
    print(num)
