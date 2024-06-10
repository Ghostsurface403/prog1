# 8. Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e
# cresce 3 centímetros por ano. Construa um programa que calcule e imprima quantos
# anos serão necessários para que Zé seja maior que Chico.

# 1,50 chico a cada 360 dias = + 2
# 1,10 ze a cada 360 dias = + 3


chico = 150
ze = 110
lidos = 0
while ze < chico:
    ze += 1
    lidos += 1
print('zé será do mesmo tamanho de chico em ',ze, 'anos')

# chico = 1,50 + 2
# ze = 1,10 + 3
#
#
#
# chico = 1,52 + 2
# ze = 1,13 + 3
#
# conclusão:
# a cada ano ze cresce 1 a mais que chico
#
# 52
# 13
# 54
# 16
#  depois de 40 anos eles terão a mesma altura
#
