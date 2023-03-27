# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(lista):
    print(f"Sorteando os 5 valores da lista: ", end = "")
    for i in range(0,5):
        lista.append(randint(1, 10))
        sleep(0.5)
        print(lista[i], end= " ")
    print("PRONTO!")

    
def somapar(lista):
    pares = []
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            pares.append(lista[c])
    print(f"Somando os valores pares de {lista}, temos {sum(pares)}.")
    
    

lista = []
sorteia(lista)
somapar(lista)