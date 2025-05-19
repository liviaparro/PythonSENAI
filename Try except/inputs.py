

def input_str(mensagem):
    while True:
        numero_str = str(input(mensagem))
        
        if not numero_str.isalpha():
            print("Digite apenas letras")
        else:
            return numero_str

def input_int(mensagem):
    while True:
        try:    
            numero_int= int(input(mensagem))
            return numero_int    
        except ValueError:
            print("Digite apenas letras")
        
def input_float(mensagem):
    while True:
        try:
            numero_float = float(input(mensagem))
            return numero_float
        
        except ValueError:
            return numero_float
            print("Digite apenas letras") 