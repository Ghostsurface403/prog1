# 6. Construa um programa que leia vários números e informe quantos números entre 100
# e 200 foram digitados. Quando o valor 0 (zero) for lido, o programa deverá cessar sua
# execução.

lidos = 0
num = 1
while num != 0:
    num = int(input('Digite um númemro: '))
    if num >= 100 and num <= 200:
        lidos += 1
print('A quantidade de números lidos foi: ',lidos)




