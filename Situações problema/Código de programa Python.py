# Implementem o código do programa em Python.

# Calcule a área do hexágono e do triangulo equilátero

print("área do hexágono")
lado = int(input("digite o lado do hexágono "))
lado2 = lado * lado
raiz = round( 3 ** 0.5, 2)
mult = raiz * lado2
div = mult / 4
mult2 =round(div * 6, 2)
print("a área do hexágono é ", mult2)