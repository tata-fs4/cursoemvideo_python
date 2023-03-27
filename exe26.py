# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.
frase= str(input("Digite uma frase:"))
frase= frase.lower()
print(f"A letra 'A' aparece {frase.count('a')} vezes.")
print(f"A primeira letra 'A' está na posição {frase.find('a')+1}.")
print(f"A última letra 'A' está na posição {frase.rfind('a')+1}.")