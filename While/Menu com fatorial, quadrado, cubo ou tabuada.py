#desenvolva um programa que tenha um menu onde o usuario vai escolher se quer fatorial, quadrado, cubo ou tabuada e depois ler um numero e retornar o resultado da escolha

print("Escolha")

n = 0

while True:
    print("Escolha")
    print("[1] = Fatorial")
    print("[2] = Quadrado")
    print("[3] = Cubo")
    print("[4] = Tabuada")
    print("[0] = Sair")
    menu = int(input("Escolha uma opção "))
    if menu == 0:
        print("Você saiu")
        break
    elif menu == 1:
        n1 = int(input("Digite um número "))
        fatorial = 1
        while (n1 > 0 ):
            fatorial = fatorial*n1
            n1 = n1 - 1
            print("O fatorial do número é", fatorial)
    elif menu == 2:
        n2 = int(input("Digite um número para seu quadrado "))
        result = n2*n2
        print("O quadrado é", result)
    elif menu == 3:
        n3 = int(input("Digite um número para seu cubo "))
        result = n3*n3*n3
        print("O resultado do cubo é", result)
    elif menu == 4:
        n4 = int(input("Digite um número para sua tabuada "))
        print(n4, 'X 1 =', n4*1)
        print(n4, 'X 2 =', n4*2)
        print(n4, 'X 3 =', n4*3)
        print(n4, 'X 4 =', n4*4)
        print(n4, 'X 5 =', n4*5)
        print(n4, 'X 6 =', n4*6)
        print(n4, 'X 7 =', n4*7)
        print(n4, 'X 8 =', n4*8)
        print(n4, 'X 9 =', n4*9)
        print(n4, 'X 10 =', n4*10)
