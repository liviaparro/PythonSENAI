#passo 1: crie uma lista com os nomes de 5 objetos

objetos = ["Caneta", "Lápis", "Apontador", "Estojo", "Régua"]

#passo 2: adicione mais um objeto ao final da lista

objetos.append("Cola ")

#passo 3: acesse o objeto que está na segunda posição e exiba-o

print(objetos [1])

#passo 4: remova um objeto da lista e exiba-o

print(objetos.pop (1))

#passo 5: exiba o tamanho da lista

print(len(objetos))

#passo 6: mostre todos os itens com o for

for objeto in objetos:
    print(objeto)
    
#passo 7: verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione.
    
if "Cadeira" in objetos:
    objetos.remove("Cadeira ")
else:
    objetos.append("Cadeira ")
    
#passo 8: ordene a lista em ordem alfabética, exiba o antes e o depois
    
print(objetos)
print(objetos.sort ())
print(objetos)

#passo 9: exiba o primeiro e o último objeto e exiba eles.

print(objetos [0])
print(objetos[len(objetos)-1])

#passo 10: Limpe toda a lista

objetos.clear()