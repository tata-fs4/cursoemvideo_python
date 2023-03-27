# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
from math import sqrt, hypot
co= float(input("Digite o comprimento do cateto oposto: "))
ca= float(input("Digite o comprimento do cateto adjacente: "))
hi= hypot(ca,co)
print(f"Um triângulo com o cateto oposto {co} e cateto adjacente {ca} possui hipotenusa {hi:.2f} ")