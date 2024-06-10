# 10.Em uma entrevista feita com o público em geral foi perguntada a idade, o sexo ('F' ou
# 'M') e o estado civil ('S' ou 'C') de cada indivíduo. Faça um programa que leia todos os
# dados coletados na entrevista. A leitura deverá terminar quando for informado o valor -
# 1 para a idade. Ao término da leitura, o programa deverá imprimir o percentual de
# pessoas do sexo masculino solteiras, o número de mulheres casadas e a idade do
# homem mais jovem que seja casado, considerando o conjunto de entrevistados.

hs = 0
mc = 0
ihcn = 200
htotal = 0
mtotal = 0
age = 2

while age != 1:
    age = int(input('Digite sua idade: '))
    if age == 1:
        break
    sex = str(input('Digite seu sexo: (M para mulher e H para Homem) '))
    civ = str(input('Digite seu estado civil: (S para solteiro e C para casado) '))
    if sex == 'M':
        mtotal += 1
        if civ == 'C':
            mc += 1

    elif sex == 'H':
        htotal += 1
        if civ == 'S':
            hs += 1
        elif civ == 'C':
            if age < ihcn:
                age = ihcn

if htotal == 0:
    print('Nenhum homem foi consultado')
else:
    phs = hs / htotal
    print('O percentual de homens solteiros é: ', phs)
    print('A idade do homem casado mais jovem é', ihcn)

if mtotal == 0:
    pmc = mc / mtotal
    print('O número de mulheres casadas é? ', pmc)


