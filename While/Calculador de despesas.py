#desenvolva um programa com um menu que de acordo com a escolha do usuario ele consiga adicionar um valor de uma despesa ou exibir o valor total

print("Despesas")

valor = 0
n_despesas = 0

while True:
    print("Despesas")
    print("1 = Valor da despesa")
    print("2 = Quantidade e valor total da despesa")
    print("0 = Sair")
    menu = int(input("O que você quer fazer hoje? "))
    if menu == 0:
        print("Você saiu")
        break
    elif menu == 1:
        ad_valor = int(input("Qual o valor? "))
        print("Você adicionou", ad_valor, "reais em sua despesa")
        n_despesas += 1
        valor = ad_valor + valor
       
    elif menu == 2:
        print("Você tem o total de ", n_despesas, "despesas, que somam", valor, "reais de despesas")
       
    else:
        print("ERRO")
