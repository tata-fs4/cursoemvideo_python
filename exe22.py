# Crie um programa que leia o nome completo de uma pessoal e mostre:
# O nome com todas as letras maiúsculas
# O nome ccom todas minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome=str(input("Digite seu nome completo: ")).strip()
print("Analisando o seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')}")
separa = nome.split()
print(separa)