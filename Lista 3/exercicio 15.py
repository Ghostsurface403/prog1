# 15.Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
# ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
# ano, crie um programa que calcule e imprima o tempo necessário para que a
# população do país A ultrapasse a população do país B.



# n_nasc_a = 150 #(5000000 * 0.03) / 1000  = 150
# n_nasc_b = 140 #(7000000 * 0.02) / 1000 = 140


hab_a = 5000000
hab_b = 7000000
ano = 0

while hab_a < hab_b:
    hab_a += 150
    hab_b += 140
    ano += 1
print(ano)

