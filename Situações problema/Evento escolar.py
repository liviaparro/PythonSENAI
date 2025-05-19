import inputs
nomes=[]

while True:
    print("Menu")
    print("")
    print("[1] - Cadastrar nomes")
    print("[2] - Total de inscritos")
    print("[3] - Lista de nomes em ordem alfabética")
    print("[4] - Consulta de nomes")
 
    menu = inputs.input_int(("Escolha uma opção: "))
    
    if menu == 1:
        nome = inputs.input_str(("Digite seu nome completo: "))
        if nome in nomes:
            print("Esse nome ja existe na lista ")
        else:
            nomes.append(nome)
            print("Seu nome foi adicionado ")
            
    elif menu == 2:
        print(len(nomes))
        
    elif menu == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    elif menu == 4:
        nome = inputs.input_str(("Digite seu nome completo: "))
        if nome in nomes:
            print("Nome encontrado!")
            print("[1] - Sim")
            print("[2] - Não")
            remover = input("Deseja removê-lo? (sim ou não): ")
            nomes.remove(nome)
            print("Nome removido")
            continuar = input("Gostaria de avançar? (sim ou não)")
            if continuar == "não":
                print("Fim")
                break
                
            else:
                print("Continue a inscrição")
        else:
            print("Nome não encontrado")
            print("[1] Sim")
            print("[2] Não")
            menu2 = inputs.input_str(("Deseja adicioná-lo? "))
            if menu2 == 1:
                nomes.append()
                print("Seu nome foi adicionado")
                