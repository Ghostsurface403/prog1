# 2. Rescreva o programa abaixo que procure em uma lista um valor fornecido e
# retorne posição onde ele foi encontrado ou -1 caso não esteja na lista, mas
# utilizando uma função

# lista = [1, 2, 10, 5, 20]
# valor = 10
# pos = -1
# for i in range(len(lista)):
#   if lista[i] == valor:
#       pos = i
# print(pos)
#
# _________________________________________________________

# 1° Forma

lista = [1, 2, 10, 5, 20]
valor = 10
pos = -1

def procura_valor_lista(lista, valor,pos):
    for i in range(len(lista)):
        if lista[i] == valor:
            pos = i
    return pos

pos = procura_valor_lista(lista, valor, pos)
print(pos)


# _________________________________________________________

# 2° Forma

lista = [1, 2, 10, 5, 20]
valor = 10

def procura_valor_lista(lista, valor):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            pos = i
    return pos

print(procura_valor_lista(lista, valor))
