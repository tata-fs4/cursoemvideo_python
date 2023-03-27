# Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input("Digite um nome completo: ")).strip().title()
nome= nome.split()
print(f"O primeiro nome é: {nome[0]}")
print(f"O último sobrenome é: {nome[-1]}")