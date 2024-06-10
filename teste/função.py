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