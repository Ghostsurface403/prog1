# 1. Rescreva o programa abaixo que exclui o primeiro elemento da lista com
# valor especificado, mas utilizando uma função.

# lista = [1, 4, 5, 6, 4, 7]
# valor = 4
# removeu = False
# temp = []
# for i in range(len(lista)):
#     if lista[i] != valor or removeu:
#         temp.append(lista[i])
#     else:
#         removeu = True
# lista = temp
# print(lista)
#
# _____________________________________________________________

lista = [1, 4, 5, 6, 4, 7]
valor = 4

def remove_valor_lista(lista, valor):
    removeu = False
    temp = []
    for i in range(len(lista)):
        if lista[i] != valor or removeu:
            temp.append(lista[i])
        else:
            removeu = True
    return temp

lista = remove_valor_lista(lista, valor)

print(lista)