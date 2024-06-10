# def saudacao ():
#     print('hello world')
#
# saudacao()
#
# def fatorial(x):
#     fat = 1
#     if (x >= 1):
#         for i in range(1,x + 1):
#             fat = fat * i
#     return(fat)
def fatorial():
    x = n
    fat = 1
    if (x >= 1):
        for i in range(1, x + 1):
            fat = fat * i
    return(fat)

n = int(input('entre com o valor de n '))
c = fatorial()
print(c)

# printa só o elemento retirado

lista = [1, 2, 3, 4]
pos = 2

def exclui_elemento(lista, pos):
    temp = []
    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            print(lista[i])
    return temp

lista = exclui_elemento(lista, pos)

print(lista)