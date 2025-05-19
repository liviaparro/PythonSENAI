# passo a passo

#1 - Exibir quanto custa encher um tanque de 50 litros de um carro

#2 - O tanque tem 50 litros de capacidade, está com 20 litros atualmente, o custo do combustível é de R$5,80/litro

#3 -
#passo 1: Descobrir quantos litros faltam para encher o tanque
#passo 2: Fazer a subtração de 50 - 20
#passo 3: Descobrir quanto custa 30 litros de combustível
#passo 4: Fazer a multiplicação de 30 * 5,80
#passo 5: Exibir o custo do combustível

capacidade_total= int(input("digite a capacidade do tanque "))
combustível= int(input("digite quantos litros de combustível tem no tanque"))
resultado= capacidade_total - combustível

preco= float(input("digite quanto custa o litro do combustível "))
resultado2= resultado * preco

print("o custo foi de R$", resultado2)