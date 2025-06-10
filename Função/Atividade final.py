lista = []

def menu():
    print("[1] - Cadastro de nomes")
    print("[2] - Média")
    print("[3] - Situação")
    print("[0] - Sair")

#Cadastro e informação de nomes
#O usuário possa informar o nome do aluno.
#Coleta dados do aluno, calcula e armazena em uma lista. 

def cadastrar_aluno(nome):
     if nome in lista:
            print("Esse nome já está cadastrado")
     else:
        lista.append(nome)
        print("Seu nome foi cadastrado")
        
nome = str(input("Digite o nome completo: "))
cadastrar_aluno(nome)
        

    
#O sistema receba três notas e calcule a média automaticamente.
#Calcular_media(n1, n2, n3) → retorna a média das notas.
#Coleta dados do aluno, calcula e armazena em uma lista.

def calcular_media(n1, n2, n3):
        soma = n1 + n2 + n3
        media = soma / 3
        print("Resultado da media: ", media)
        return media
n1 = float(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
calcular_media(n1, n2, n3)

#Com base na média, o sistema deve indicar se o aluno está "Aprovado" (média ≥ 7), "Recuperação" (entre 5 e 6.9) ou "Reprovado" (média < 5).
#Coleta dados do aluno, calcula e armazena em uma lista.
#Retorna a situação do aluno com base na média.
#Mostra o relatório final com nome, média e situação.

 

def verificar_situacao(media):
    if media >= 7:
            return "Aprovado"
    
    elif media >= 5 and media <= 7:
        return "Recuperacao"
        
    else:
        return "Reprovado"
        
media = (n1 + n2 + n3) / 3

verificar_situacao(media)


#Listas e dicionários
#O sistema deve permitir o cadastro de vários alunos e exibir um resumo final com o nome de cada aluno e sua situação. 
#Coleta dados do aluno, calcula e armazena em uma lista.


