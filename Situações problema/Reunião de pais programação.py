print("Menu de opções")
print("")

print("[1] - Cadastrar os nomes ")
print("[2] - Exibir o total de pais ")
print("[3] - Exibir a lista de nomes ")
print("[4] - Confirmação de presença ")
print("[5] - Exibir o relatório da chamada ")
print("[6] - Sair ")

nomes=[]
presentes=[]
ausentes=[]
while True:
    opcao=int(input("Digite sua escolha"))
    print("")


    if opcao==1:
        nome=input("digite o nome que deseja cadastrar")
        if nome in nomes:
            print("Nome ja cadastrado")
        else:
            nomes.append(nome)
            print("Nome cadastrado com sucesso")
    
    elif opcao==2:
        print("O total de pais são:", len(nomes))
        
    elif opcao==3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    elif opcao==4:
       nome=input("Digite um nome para verificar se está presente:")
       if nome in nomes:
           presentes.append(nome)
           print("nome está em nossa lista de presentes")
       else:
           ausentes.append(nome)
           print("nome está em nossa lista de ausentes")
    
    elif opcao==5:
        print("lista de presentes:")
        for item in presentes:
            print(item)
        print("")
        print("lista de ausentes:")
        for item in ausentes:
            print(item)
        
    elif opcao==6:
        print("Você saiu")
        break
    
    else:
        print("opção inexistente")