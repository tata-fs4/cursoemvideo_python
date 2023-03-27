# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
listanum = []
next = "S"
while next == "S":
    n = int(input("Digite um valor: "))
    if n not in listanum:
        listanum.append(n)
    else:
        print("Valor duplicado! Não vou adicionar...")
    next = str(input("Quer continuar? [S/N] ")).upper()
listanum.sort()
print(f"Os valores digitados em ordem crescente foi: {listanum}")