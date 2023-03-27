# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade= str(input("Digite o nome da cidade: ")).strip()
cidade=cidade.title()
cidade= cidade.split()
print(f"A cidade começa com o nome 'SANTO'? {'Santo' in cidade[0]}")