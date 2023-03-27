# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número: "))
mult=0

for count in range(1,n+1):
    if n % count == 0:
        print("\033[33m", end="")
        mult+= 1
    else:
        print("\033[31m", end="")
    print (f"{count} ", end="")
print(f"\nO número {n} foi divisível {mult} vezes")
if mult == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele não é PRIMO!")