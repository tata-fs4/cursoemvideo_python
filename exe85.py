# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]]
temp = 0

for n in range(1,8):
    temp = int(input(f"Digite o {n}º valor: "))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
print(f"Os valores pares em ordem crescente: {sorted(lista[0])}")
print(f"Os valores ímpares em ordem crescente: {sorted(lista[1])}")
print(lista)