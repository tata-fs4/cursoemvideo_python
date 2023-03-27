# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
def linha():
    print("="*20)
linha()
print("Números Pares")
linha()
for c in range(1, 50, 2):
    print(c+1, end=" ")
print("FIM")