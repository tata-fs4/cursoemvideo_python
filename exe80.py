# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
listanum = []
n=0
for c in range(0,5):
    n = int(input(f"Digite um valor: "))
    if c == 0 or n > listanum[-1]:
        listanum.append(n)
        print("Adicionado ao final da lista...")
    else:
        for pos, x in enumerate(listanum):
            if n <= x:
                listanum.insert(pos, n)
                break

print(f"Os valores digitados em ordem foram {listanum}")