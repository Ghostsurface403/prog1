# 7. Crie um programa que leia 2 notas de um aluno e calcule a média. Se a média do aluno for
# maior que 7.0, escreva 'Aprovado'; se for menor que 7.0 mas maior que 3.0, escreva 'Exame'; se for menor que 3.0, escreva
# 'Reprovado'. Além da mensagem, informe também qual foi a média do aluno.

nota_a = float(input('Insira uma nota: '))
nota_b = float(input('Insira uma nota: '))

media = (nota_a + nota_b) / 2

print(media)

if media >= 7 and media <= 10:
    print('Aprovado')

if media < 7 and media >= 3:
    print('Exame')

if media >= 0 and media < 3:
    print('Reprovado')

