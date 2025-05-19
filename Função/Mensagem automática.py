from datetime import datetime

def saudacao(nome):
    hora = datetime.now().hour
    
    if hora >= 0 and hora <= 5:
        print("Boa madrugada", nome)
  
    elif hora >= 5 and hora <= 12:
        print("Bom dia", nome)
    
    elif hora >= 12 and hora <= 19:
        print("Boa tarde", nome)
      
    elif hora >= 19 and hora <= 23:
        print("Boa noite", nome)
    
nome = input("qual seu nome?")
saudacao(nome)

    