#1 - Faça uma função que verifica se o número é positivo ou negativo e retorne True ou False


def verificar_negativo(numero):
    if numero < 1:
        print(input("Esse número é negativo "))
        return False


    elif numero > 1:
        print(input("Esse número é positivo" ))
        return True

numero = int(input("Digite um numero: "))
verificar_negativo (numero)

