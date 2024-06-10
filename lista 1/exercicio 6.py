# 6. Faça um programa que receba o salário-base de um funcionário, calcule e
# mostre o salário a receber, sabendo-se que esse funcionário tem gratificação
# de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.

salario_base = float(input('insira um salario: '))

salario_receba = (salario_base * 0.05) + salario_base

salario_imposto = salario_receba - (salario_base * 0.07)


print(f'Seu salário com gratidicação, e com desconto do imposto é {salario_imposto}')

