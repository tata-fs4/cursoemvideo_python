#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for i in range(1,6):
    n = float(input(f"Peso da {i}ª pessoa: "))
    lista.append(n)
lista = sorted(lista)
print(f"O menor peso da lista é: {lista[0]} kg")
print(f"O menor peso da lista é: {lista[-1]} kg")