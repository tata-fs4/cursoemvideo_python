# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
from math import floor
n = float(input("Digite um número: "))
print(f"O número {n} tem a sua porção inteira {math.floor(n)}")