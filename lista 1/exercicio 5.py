# 5. Faça um programa que receba o salário de um funcionário e o percentual de
# aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input('insira um salario: '))
percentual_aumento = float(input('insira um percentual: (apenas números) '))

print(f'Seu percentual de aumento é: {percentual_aumento}%')


percentual_aumento = percentual_aumento/100
salario_novo = (salario * percentual_aumento) + salario

print(f'Seu novo salário é: {salario_novo}')
