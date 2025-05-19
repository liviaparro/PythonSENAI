ano_nascimento = int(input("Digite o ano de nascimento "))

subtracao = 2025 - ano_nascimento

if subtracao < 18:
    print("Menor de idade")
else:
    print("Maior de idade")