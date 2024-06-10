# 6. Faça um programa que leia a idade de uma pessoa e escreva se a pessoa é 'maior de idade',
# 'menor de idade' ou 'maior de 65 anos'. Apenas uma mensagem deve ser apresentada.


age = int(input('Digite sua idade: '))

if age < 18 and age > 0:
    print('Menor de idade')
elif age >= 18 and age <= 65:
    print('Maior de idade')
elif age <= 0:
    print('idade inválida')
else:
    print('Maior de 65 anos')