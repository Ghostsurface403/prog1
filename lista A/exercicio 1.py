# sabendo-se que: um pé é igual a 12 polegadas, uma jarda é igual a 3 pés, uma milha igual a
# 1760 jardas, faça um programa que receba uma medida em pés, faça as conversões e apresente o resultados
# em polegas, jardas e milhas

# 1 pe = 12 polegadas
# 1 jarda = 3 pes
# 1 milha =1760 jardas
#
# 1 polegada = 0,0833333 pe
# 1 jarda = 3 pes

print('Conversor de Jardas para pés!')

foot = float(input('Digite uma medida em pés: '))
yards = foot * 1/3

print(f'{foot} pés é igual a {yards} Jardas.')



print('Conversor de Milhas para Pés!')

foot = float(input('Digite uma medida em Pés: '))
miles = foot * 0.000189394

print(f'{foot} pés é igual a {miles} Milhas.')




print('Conversor de Polegadas para Pés!')

foot = float(input('Digite uma medida em pés: '))

inches = foot * 12

print(f'{foot} pés é igual a {inches} Polegadas.')


