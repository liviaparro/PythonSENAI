import inputs

print("Lista de presença na reunião")
presenca = []
ausentes = []

while True:
    print("Menu")
    print('[1] - Cadastrar nomes')
    print('[2] - Exibir total de pais')
    print('[3] - exibir a lista em ordem alfabetica')
    print('[4] - Realizar a confirmação de presença dos pais')
    print("[5] - Exibir um relatório da chamada ")
    print("[0] - Sair")

   
    menu = inputs.input_int("Digite sua opção aqui: ")
    if menu == 0:
        break
    elif menu == 1:
        print("Vamos cadastar seu nome: ")
        nome = inputs.input_str("Digite o nome desejado: ")
        if nome in presenca:
            print("Seu nome já esta na lista")
            print(presenca)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                print("Fim")
                break
            else:
                continue  
        else:
            presenca.append(nome)
            print("Nome adicionado")
            print(presenca)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                break
            else:
                continue
    elif menu == 2:
        print("Quantidade de Inscritos")
        print(len(presenca))
        continuar = inputs.input_str("Deseja continuar? (sim/não)")
        if continuar == "não":
            print("Fim")
            break
       
        else:
            continue
       
       
    elif menu == 3:
        presenca.sort()
        for x in presenca:
            print(x)
        continuar = inputs.input_str("Deseja continuar? (sim/não)")
        if continuar == "não":
            print("Fim")
            break
        else:
            continue
    
    elif  menu == 4:
        no = inputs.input_str('Digite o nome para analizar sua presença: ')
        if no in presenca:
            print("Essa pessoa esteve presente")
            print(presenca)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                print("Fim")
                break
            else:
                continue
        else:
            ausentes.append(no)

            print('Essa pessoa não esteve presente')
            print(presenca)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                print("Fim")
                break
            else:
                continue
    elif menu == 5:
        print("MENU")
        print('[1] - Presentes')
        print('[2] - Ausentes')
        escolha = inputs.input_int(("Escolha a opção: "))
        if escolha == 1:
            print(presenca)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                print("Fim")
                break
            else:
                continue
        else:
            print(ausentes)
            continuar = inputs.input_str("Deseja continuar? (sim/não)")
            if continuar == "não":
                print("Fim")
                break
            else:
                continue