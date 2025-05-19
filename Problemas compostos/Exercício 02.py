# passo a passo

#1 - Exibir o novo preço do produto e quanto ele diminuiu

#2 - Aplicar 5% de desconto no produto

#3 -
# passo 1: Solicitar o nome de um produto e preço
# passo 2: Aplicar o desconto de 5%
# passo 3: Exibir o novo preço do produto e quanto ele diminuiu

print("desconto do produto ")

nome = input("escreva o nome do produto ")
preco = int(input("digite o preço "))
resultado = preco / 5
resultado2 = preco - resultado

print("o desconto foi de ", resultado, "o preço final é ", resultado2)