#4 - Crie uma função que calcula o valor do frete da seguinte forma:
#	valor = (peso x 0.5) + (distância x 0.1) + taxa_fixa

def calcular_frete (peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    print("valor do frete é: ",valor)
    
peso = int(input("Digite o peso: "))
distancia = int(input("Digite a distancia: "))
taxa_fixa = 15
calcular_frete(peso, distancia, taxa_fixa)