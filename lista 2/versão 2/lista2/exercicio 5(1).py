# 5. Escreva um programa que leia 3 números e imprima o maior deles (suponha números diferentes).
a = float(input('Insira um número para a: '))
b = float(input('Insira um número para b: '))
c = float(input('Insira um número para c: '))

#a maior que tudo e diferente que tudo
if a > b and a != b and a > c and a != c:
    print('a é o número  maior')
#b maior que tudo e diferente que tudo
elif b > a and b != a and b > c and b != c:
    print('b é o número  maior')
# c maior que tudo e diferente que tudo
elif c > a and c != a and c > b and c != b:
    print('c é o número maior')
# else:
else:
    print('Erro!')




