# 3. Rescreva o programa abaixo que exclui um elemento da lista em uma
# determinada posição e obter o valor excluído, mas utilizando uma função.

# lista = [1, 2, 3, 4]
# pos = 2
# elemento_retirado = 0
# temp = []
# for i in range(len(lista)):
#     if i != pos:
#         temp.append(lista[i])
#     else:
#         elemento_retirado = lista[i]
# lista = temp
# print(lista)
# print(elemento_retirado)

# __________________________________________________________

# printa só o elemento retirado

# lista = [1, 2, 3, 4]
# pos = 2
#
# def exclui_elemento(lista, pos):
#     elemento_retirado = 0
#     temp = []
#     for i in range(len(lista)):
#         if i != pos:
#             temp.append(lista[i])
#         else:
#             elemento_retirado = lista[i]
#     return elemento_retirado
#
# elemento_retirado = exclui_elemento(lista, pos)
#
# print(elemento_retirado)


# printa  elemento retirado

lista = [1, 2, 3, 4]
pos = 2

def exclui_elemento(lista, pos):
    elemento_retirado = 0
    temp = []
    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            elemento_retirado = lista[i]
    return lista(pos)

elemento_retirado = exclui_elemento(lista, pos)

print(elemento_retirado)

# ____________________________________________________________________

lista = [1, 2, 3, 4]
pos = 2

def exclui_elemento(lista, pos):
    elemento_retirado = 0
    temp = []
    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            elemento_retirado = lista[i]
    return elemento_retirado

elemento_retirado = exclui_elemento(lista, pos)

print(elemento_retirado)