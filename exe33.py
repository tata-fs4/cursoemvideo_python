# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Mais um, por favor: "))
# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")