# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
listanum = []
par = []
impar = []

while True:
    n = int(input(f"Digite um valor: "))
    listanum.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    next = str(input("Quer continuar? [S/N] "))
    if next in "Nn":
        break

print(f"A lista completa é {listanum}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")