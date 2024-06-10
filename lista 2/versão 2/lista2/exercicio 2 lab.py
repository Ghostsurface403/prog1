# Dado o nome e o salário bruto de um funcionário, imprimir o nome, o salário bruto, a margem de
# desconto, o valor do desconto, e o salário líquido. o desconto será obtido se o salário bruto for menor ou
# igual a 1400 reais, a margem de desconto será 10%, caso contrário a margem de desconto será de 15%.

nome = str(input('Insira um nome: '))
salario_bruto = float(input('Insira um salário: '))

if salario_bruto <= 1400:
    margem_desconto = 0.10
else:
    margem_desconto = 0.15

valor_desconto = salario_bruto * margem_desconto
salario_liquido = salario_bruto - valor_desconto

print(nome)
print(salario_bruto)
print(margem_desconto)
print(valor_desconto)
print(salario_liquido)

