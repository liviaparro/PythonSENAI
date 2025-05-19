#solicite um numero ao usuario e exiba todos os numeros pares e a quantidade deles ate o numero solicitado
n = int(input("Digite um número par "))
quant = 0

while True:
    n = n - 1
    if n % 2 == 0:
        print(n)
        quant = quant + 1
    elif n <= 0:
        print("A quantidade é", quant + 1)
        break