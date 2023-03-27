# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

menores= 0
maiores= 0
for i in range(1,8):
    n= int(input(f"Em que ano a {i} pessoa nasceu? "))
    if (date.today().year) - n < 18:
        menores += 1
    else:
        maiores += 1
print(f"O numero de pessoas maiores de idade é: {maiores}.")
print(f"O número de pessoas menores que 18 anos é: {menores}.")