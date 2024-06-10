# 14. Faça um programa que leia 3 números e verifique se eles podem ou não ser lados de um triângulo. Se podem,
# escreva se o triângulo formado é 'equilátero', 'isósceles' ou 'escaleno'. Caso contrário, informe que os números
# não compõem um triângulo.



lado1 = float(input('digite um número: '))
lado2 = float(input('digite um número: '))
lado3 = float(input('digite um número: '))
if lado1 <= 0 and lado2 <= 0 and lado3 <= 0:
    print('Os números não compõem um triangulo! ')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  print('Triangulo escaleno')
elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Tringulo equilatero')
else:
  print('Triangulo isosceles')







