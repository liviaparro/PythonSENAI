#faça um programa para calcular diferentes áreas como do circulo, quadrado e retangulo
#exercicio 4

def circulo(raio) :
    return 3.14 * raio **2
   
def quadrado(n1) :
    return n1 * n1
   
def retangulo(n1, n2) :
    return n1 * n2
   
def menu_area():
    print("1 Circulo")
    print("2 Quadrado")
    print("3 Retângulo")
    print("4 Triângulo")
    print("5 Hexágono")
   
    opcao = int(input("Escolha uma opção: "))
   
    if opcao == 1:
        raio = float(input("Digite o raio do circulo: "))
        print("Área do circulo = ",circulo(raio))
       
    elif opcao == 2 :
        lado = float(input("Digite o lado do quadrado: "))
        print("Área do quadrado = ", quadrado(lado))
       
    elif opcao == 3 :
        base = float(input("Digite a base do retangulo: "))
        altura = float(input("Digite a altura do retangulo"))
        print("Área do retângulo = ", retangulo(base, altura))

#exercicio 4.1

def triangulo(lado):
    lado2 = lado * lado
    raiz = round(3 ** 0.5, 2)
    mult = raiz * lado2
    return mult / 4

def hexagono(lado):
    return round(triangulo(lado) * 6, 2)

#exercicio 4.2

def perimetro_circulo(raio):
    return 2 * 3.14 * raio

def perimetro_quadrado(n1):
    return 4 * n1

def perimetro_retangulo(n1, n2):
    return 2 * (n1 * n2)

def perimetro_triangulo(lado):
    return 3 * lado

def perimetro_hexagono(lado1):
    return 6 * lado1

def menu_perimetro():
    print("1 Circulo")
    print("2 Quadrado")
    print("3 Retângulo")
    print("4 Triângulo")
    print("5 Hexágono")
   
    escolha = int(input("Escolha uma opção "))
   
    if escolha == 1:
        raio = float(input("Digite o raio do circulo "))
        print("O perímetro do circulo é ", perimetro_circulo(raio))
       
    elif escolha == 2:
        n1 = float(input("Digite o lado do quadrado "))
        print("O perímetro do quadrado é ", perimetro_quadrado(n1))
       
    elif escolha == 3:
        n1 = float(input("Digite o valor da base do retângulo "))
        n2 = float(input("Digite o valor da altura do retângulo "))
        print("O perímetro do retângulo é ", perimetro_retangulo(n1, n2))
       
    elif escolha == 4:
        lado = float(input("Digite o lado do triângulo "))
        print("O perímetro do triângulo é ", perimetro_triangulo(lado))
       
    elif escolha == 5:
        lado1 = float(input("Digite o lado do hexágono "))
        print("O perímetro do hexágono é ", perimetro_hexagono(lado1))
       

print("1 = Área")
print("2 = Perímetro")

escolha1 = int(input("Escolha uma opção "))

if escolha1 == 1:
    menu_area()
   
elif escolha1 == 2:
    menu_perimetro()
    
