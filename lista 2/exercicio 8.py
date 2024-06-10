# 8. Faça um programa que leia o salário de uma pessoa e imprima o desconto do INSS segundo a tabela a seguir:
#
# menor ou igual a R$ 600,00 isento
# maior que R$ 600,00 e menor ou igual a R$ 1200,00 20%
# maior que R$ 1200,00 e menor ou igual a R$ 2000,00 25%
# maior que R$ 2000,00 30%


sal = float(input('Insira um salário: '))
if sal <= 600:
    print('Isento')
elif sal <= 1200:
    desconto = sal - sal * 0.2
    print(desconto)
elif sal <= 2000:
    desconto = sal - sal * 0.25
    print(desconto)
else:
    desconto = sal - sal * 0.3
    print(desconto)
