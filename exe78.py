# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
for posição, valor in enumerate(valores):
    if valor == max(valores):
        maior = posição
    elif valor == min(valores):
        menor = posição
print(f"O maior valor digitado foi {valores[maior]} na posição {maior}")
print(f"O menor valor digitado foi {valores[menor]} na posição {menor}")