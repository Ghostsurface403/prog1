# 13.A série de Fibonacci é formada pela seguinte seqüência:”
# etc”. Escreva um programa que gere a série de Fibonacci até o vigésimo termo.
ant = 1
prox = 1
print(ant)
print(prox)
for f in range(1,21 - 2):
    aux = ant + prox    # 13
    ant = prox          # 8
    prox = aux          # 13
    print(prox)


#  0 + 1 = 1
#      1 + 1 = 2
#          1 + 2 = 3
#              2 + 3 = 5

# 0,1,2,3,4,5,6,7,8,9
#
#
