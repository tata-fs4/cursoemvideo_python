#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
from math import sin, cos, tan, radians
a = float(input("Digite o ângulo que você deseja: "))
print(f"Seno {sin(radians(a)):.2f}")
print(f"Cosseno {cos(radians(a)):.2f}")
print(f"Tangente {tan(radians(a)):.2f}")