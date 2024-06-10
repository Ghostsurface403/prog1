# 3) Para A e B inteiros e maiores que zero, fazer um programa para o cálculo A
# dividido por B usando subtrações sucessivas.



a = int(input('insira um número: '))
b = int(input('insira o segundo número: '))
if a <= 0 and b <= 0:
    print('Erro!')
resto = a
quociente = 0
while resto - b >= 0:
    resto = a - b
    quociente = quociente + 1

print('o resultado da divisão de',a, 'por', b, 'é:', quociente, 'e restou:',resto)
