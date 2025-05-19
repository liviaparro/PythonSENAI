# passo a passo

#1 - exibir quantos litros de combustível e quantos reais é preciso pra fazer uma viagem de 800 km

#2 - o carro tem dez litros no tanque, já percorreu 90 km, o combustível custa R$6,90, o carro tem autonomia de sete km por litro

#3 -
# passo 1: descobrir quantos litros de combustível é preciso pra viajem
# passo 2: descobrir quantos reais é preciso pra fazer a viajem

print("viagem 800 km ")
quilometro= int(input("quantos km ainda falta percorrer "))
litros= int(input("digite quantos km por litro é gasto "))
n1= quilometro / litros

print("vai ser necessário = ", n1, "litros")
preco= float(input("digite o preco da gasolina "))
n2= n1 * preco
print("o preco total é ", n2, "reais" )