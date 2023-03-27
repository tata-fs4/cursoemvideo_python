# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
pessoas = list()
dado = list()
cont = 0
maxpeso = 0
maxnome = ""
minpeso = 0
minnome = ""

while True:
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    if maxpeso == 0 and minpeso == 0:
        maxpeso = minpeso = dado[1]
        maxnome = minnome = dado[0]
    elif dado[1] > maxpeso:
        maxpeso = dado[1]
        maxnome = dado[0]
    elif dado[1] < minpeso:
        minpeso = dado[1]
        minpeso = dado[0]
    pessoas.append(dado[:])
    dado.clear()
    cont += 1
    resposta = str(input("Quer continuar? Digite S ou N: ")).upper()
    if resposta in "N":
        break

print(f"Ao todo, você cadastrou {cont} pessoas.")
print(f"O maior peso foi de {maxpeso} de {maxnome}")
print(f"O menor peso foi de {minpeso} de {minnome}")