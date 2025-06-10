#3 - Faça uma função que receba uma distância em km e uma velocidade, calcule quanto tempo levará para fazer esse percurso.

def calcular_percurso(distancia, velocidade):
    tempo = distancia / velocidade
    print("O tempo é", tempo)
    
distancia = int(input("Qual a distância ? "))
velocidade = int(input("Qual a velocidade ? "))
calcular_percurso(distancia, velocidade)
