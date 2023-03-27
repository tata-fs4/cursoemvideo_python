#Desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média
nome = str(input("Digite o nome do aluno: "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print(f"A nota média do aluno {nome} foi {media:.1f}!")