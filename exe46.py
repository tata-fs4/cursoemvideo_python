# Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
def linha():
    print("="*20)
linha()
print("Fogos de Artifício")
linha()
for c in range (10, -1, -1):
    print(f"{c}!")
    sleep(1)
sleep(1)
print("BUM! BUM! POOW!!!")