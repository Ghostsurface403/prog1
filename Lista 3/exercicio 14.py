# 14.Crie um programa que solicite ao usuário 10 valores, apresente o maior valor lido e a
# posição (1o , 2o , 3o , etc.) em que o mesmo foi informado.
maior = -9999
posicao = -1
for i in range(1,11):
    valor = int(input('Insira um valor: '))
    if maior < valor:
        maior = valor
        posicao = i
print('O maior valror é:', maior)
print('A posição do maior valor é:', posicao,'°')
