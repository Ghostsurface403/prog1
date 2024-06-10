# 10. Faça um programa que leia 3 números e imprima se eles podem ou não ser lados de um triângulo.



lado1 = float(input('digite um número: '))
lado2 = float(input('digite um número: '))
lado3 = float(input('digite um número: '))
if lado1 <= 0 and lado2 <= 0 and lado3 <= 0:
    print('Os números não compõem um triangulo! ')
if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  print('Os números compõem um triangulo!')
  if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Os números compõem um triangulo!')
else:
  print('Os números compõem um triangulo!')



