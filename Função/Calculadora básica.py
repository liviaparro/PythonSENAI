#crie uma função que receba dois números como parametros e exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão
#exercicio 3

def calculadora(n1, n2):
    print("Soma", adicao (n1, n2))
    print("Subtração", subtracao (n1, n2))
    print("Multiplicação", multiplicacao (n1, n2))
    print("Divisão", divisao (n1, n2))
   

#exercicio 3.1

def adicao(n1, n2):
    conta_soma = n1 + n2
    return conta_soma

def subtracao(n1, n2):
    conta_subtracao = n1 - n2
    return conta_subtracao

def multiplicacao(n1, n2):
    conta_multiplicacao = n1 * n2
    return conta_multiplicacao

def divisao(n1, n2):
    conta_divisao = n1 / n2
    return conta_divisao

#exercicio 3.2

def menu():
    print("Calculadora")
    print("Para a conta adição, digite 1")
    print("Para a conta subtração, digite 2")
    print("Para a conta multiplicação, digite 3")
    print("Para a conta divisão, digite 4")
   
def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def resultado(n1, n2):
    print("O resultado da adição é ", adicao(n1, n2))
    print("O resultado da subtração é ", subtracao(n1, n2))
    print("O resultado da multiplicação é ", multiplicacao(n1, n2))
    print("O resultado da divisão é ", divisao(n1, n2))

   
def calculo(n1, n2):
    if conta == "1":
        print("O resultado da adição é ",soma(n1, n2))
    elif conta == "2":
        print("O resultado da subtração é ", subtracao(n1, n2))
    elif conta == "3":
        print("O resultado da multiplicação é ", multiplicacao(n1, n2))
    elif conta == "4":
        print("O resultado da divisão é ", divisao(n1, n2))
    elif conta == "5":
        tudo(n1, n2)
    else:
        print("Erro")    
   
menu()
conta = input("Digite a operação: ")
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))

calculo(n1, n2)  
    
