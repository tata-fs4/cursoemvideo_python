# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
listanum = []
n=0
next = "S"
while next == "S":
    listanum.append(int(input(f"Digite um valor: ")))
    next = str(input("Quer continuar? [S/N] ")).upper()
listanum.sort(reverse= True)
print(f"Foram digitados {len(listanum)} números")
print(f"Os valores em ordem descrescente são {listanum}")
if 5 in listanum:
    print("O valor 5 está presente na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")