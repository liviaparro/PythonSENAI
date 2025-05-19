#Jogo de desvendar
import random
nome = input("Digite seu nome: ")
print(nome, "Bem vindo(a) ao jogo de desvendar os números")
print("Para jogar o oponente irá escolher um número secreto e você terá que adivinhar")
numero_secreto = random.randrange(1,100)

    
while True :           
    escolha = int(input('Digite um número: '))
    if escolha < numero_secreto :
        print("O número que você escolheu é menor que o número secreto")
    elif escolha > numero_secreto :
        print("O número que você escolheu é maior que o número secreto")
    else:
       print("parabens vc acertou ")
       print("deseja continuar? ")
       print("[1] - sim ")
       print("[2] - não ")
       opcao = int(input("escolha uma opção "))
       if opcao == 1:
           print("vamos para uma nova rodada, lets gooooo ")
           numero_secreto = random.randrange(1,100)
       else:
           break