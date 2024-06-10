# 12.Construa um programa que funcione através do seguinte menu (o programa deve
# apresentar o menu ao usuário e, dependendo da opção escolhida, realizar a operação
# correspondente):
# MAQUINA ESPERTA
# 1 – Soma vários números
# 2 – Multiplica vários números
# 3 – Sai do programa
# DIGITE A OPÇÃO:
# Para terminar as repetições nas opções 1 e 2, use um número pequeno, como -0,0001
op = 1
while op != 3:
    print('MAQUINA ESPERTA')
    print()

    print('1 – Soma vários números')
    print('2 – Multiplica vários números')
    print('3 – Sai do programa')
    print()

    op = int(input('DIGITE A OPÇÃO: '))
    print()
    if op == 1:
        print('1 – Soma vários números. coloque um número negativo para encerrar o processo de soma.')
        print()

        soma = 0
        num = 0
        while num >= 0:
            soma += num
            num = int(input('Digite um número: '))
        print('O resultado da soma foi:', soma)
        print()
    elif op == 2:
        print('2 – Multiplica vários números. coloque um número negativo para encerrar o processo de multiplicação.')
        print()

        mult = 1
        num = 1
        while num >= 0:
            mult *= num
            num = int(input('Digite um número: '))
        print('O resultado da multiplicação foi:', mult)
        print()
    elif op == 3:
        print('Programa finalizado!')
    else:
        print('ERRO! Opção invalida.')
        print()