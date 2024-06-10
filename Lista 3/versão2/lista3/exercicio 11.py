# 11.Crie um programa que receba o valor e o código de várias mercadorias vendidas em
# um determinado dia. Os códigos obedecem à lista a seguir:
# 'L': limpeza 'A': alimentação 'H': higiene
#
# Calcule e imprima o total vendido naquele dia para cada um dos códigos e o total
# vendido para todos os códigos juntos. Para encerrar a entrada de dados, digite o valor
# da mercadoria igual a 0 (zero).

somalimp = 0
somaalim = 0
somahig = 0
mercad = 1
while mercad != 0:
    mercad = float(input('Digite o valor da mercadoria: '))
    cod = input('Digite o código da mercadoria: ')
    if cod == 'L':
        somalimp = somalimp + mercad
    elif cod == 'A':
        somaalim = somaalim + mercad
    elif cod == 'H':
        somahig = somahig + mercad
total = somalimp + somaalim + somahig
print('O total da limpeza foi igual a:', somalimp)
print('O total da alimentação foi igual a:', somaalim)
print('O total da higiene foi igual a:', somahig)
print('O total foi igual a:', total)
