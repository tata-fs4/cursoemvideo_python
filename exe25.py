# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome= str(input("Digite um nome: ")).strip()
nome= nome.title()
print(f"O nome possui a palavra Silva? {'Silva' in nome}")