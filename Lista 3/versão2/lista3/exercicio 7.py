# 7. Uma empresa irá dar um aumento de salário aos seus funcionários de acordo com a
# categoria de cada empregado. O aumento seguirá as seguintes regras:
# Funcionários da categoria A ganharão 10% de aumento sobre o salário atual;
# Funcionários da categoria B ganharão 15% de aumento sobre o salário atual;
# Funcionários da categoria C ganharão 25% de aumento sobre o salário atual;
# Funcionários da categoria D ganharão 35% de aumento sobre o salário atual.
# Com base nas regras acima, crie um programa para o cálculo do novo salário dos
# funcionários. O programa deve ler o salário atual e a categoria do funcionário e
# escrever o seu novo salário. A repetição do programa terminará quando for digitado o
# valor 0 (zero) para o salário.

sal = 1
while sal != 0:
    sal = float(input('Digite um salário: '))
    cat = str(input('Digite uma categoria: '))
    if cat == 'a':
        sal = (sal * 0.10) + sal
    elif cat == 'b':
        sal = (sal * 0.15) + sal
    elif cat == 'c':
        sal = (sal * 0.25) + sal
    elif cat == 'd':
        sal = (sal * 0.35) + sal
    else:
        print('ERRO!')
    print('O novo salário é: ', sal)
