
# -------- Dicionarios --------

# Criar
aluno = {
    "nome": "Lívia",
    "idade": 16,
    "altura": 1.57,
    "matriculado": True
}

objeto = {
    "nome": "Armário",
    "altura": 1.90,
    "cor": "Marrom",
}
print(objeto)
objeto2 = {
    "nome": "Geladeira",
    "altura": 1.90,
    "cor": "Branco",
}
print(objeto2)
objeto3 = {
    "nome": "Fogão",
    "altura": 1.40,
    "cor": "cinza",
}
print(objeto3)

# Adicionar campo
aluno["peso"] = 50

# print(aluno)

# Alterar campo
aluno["idade"] = 17

# print(aluno)

# Deletar campo
del aluno["altura"]

# print(aluno)

# Verificar
if "altura" in aluno:
    print("Altura existente")
else:
    #print("Altura inexistente")
    print()

# Exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
    

# Exibir uma lista de Dicionários
lista_objeto = [objeto, objeto2, objeto3]

    # Escolhendo os campos
for objeto in lista_objeto:
    print(f"{objeto['nome']}")

    
    # Exibindo todos
for objeto in lista_objeto:
    for chave, valor in objeto.items():
        print(f"{chave}: {valor}")
    print()

    
    
    
    
    