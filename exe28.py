# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
from random import randint
n1= randint(1,6)
n2= int(input("Escolha um número de 1 a 6: "))
if n2==n1:
    print(f"Parabéns!!! O número escolhido pela máquina foi {n1}")
else:
    print(f"Número errado! Eu pensei no número {n1} e não no {n2}. Tente Novamente.")