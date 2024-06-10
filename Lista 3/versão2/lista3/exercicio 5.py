# 5. Construa um programa que permaneça lendo números inteiros enquanto forem
# positivos e que, ao final do programa, informe quantos números foram lidos.

lidos = 0
num = 1
while num >= 1:
    num = int(input('Digite un número: '))
    lidos += 1
lidos -= 1
print('Terminou')
print('A quantidade de números lidos foi: ',lidos)




