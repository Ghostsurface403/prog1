# 1) Para o programa e supondo que o usuário tem a intenção de digitar com
# os seguintes dados (1,3,0,4,2,-1) para entrada de dados, responda as
# questões:

# Quais os valores lidos? 1,3,0,4,2
# Que valor será impresso? 10
# Quantas repetições serão realizadas? 6
# O que aconteceria se a expressão lógica fosse A != 0? s seria 4

s = 0
a = int(input('Digite o valor de A: '))
while a != 0:
    s = s + a
    a = int(input('Digite o valor de A: '))
print(s)

# a = 1
# s = 1
#
# a = 3
# s = 4
#
# a = 0
# s = 4
#
# a = 4
# s = 8
#
# a = 2
# s = 10
