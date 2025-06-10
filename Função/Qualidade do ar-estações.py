#2 - A temperatura ideal para a qualidade do ar é entre 20C e 22C no inverno e 23C e 26C no verão.
#A umidade ideal para a saúde humana deve estar entre 40% e 55% no inverno e 40% e 65% no verão.
#Faça uma função que verifica a qualidade do ar com base nesses dados.

def verificar_qualidade(temperatura, umidade, estacao):
    
    if estacao == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print("A qualidade do ar é ideal para o inverno")
        

    elif estacao == "verao":
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 40 and umidade <= 65:
                print("A qualidade do ar é ideal para o verão")
                
                
temperatura = int(input("Qual a temperatura ? "))
umidade = int(input("Qual a umidade ? "))
estacao = str(input("Qual a estação ? "))
verificar_qualidade(temperatura, umidade, estacao)
                
        
    