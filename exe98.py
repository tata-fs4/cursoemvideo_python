# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada
from time import sleep
def contador():
    print("-="*20)
    print("Contagem de 1 até 10 de 1 em 1")
    for c in range(1,10+1, 1):
        sleep(0.5)
        print(c, end= " ", flush= True)
    print("FIM!")
    print("-="*20)
    print("Contagem de 10 até 0 de 2 em 2")
    for c in range(10, 0-1, -2):
        sleep(0.5)
        print(c, end= " ", flush= True)
    print("FIM!")
    print("-="*20)
    print("Agora é sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-="*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for c in range(inicio, fim, passo):
            sleep(0.5)
            print(c, end= " ", flush= True)
        print("FIM!")
    elif fim < inicio:
        if passo > 0:
            passo = -passo
        for c in range(inicio, fim-1, passo):
            sleep(0.5)
            print(c, end= " ", flush= True)
        print("FIM!")
    
    
    
contador()