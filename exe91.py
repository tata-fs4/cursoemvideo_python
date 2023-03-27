# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
n=1
jogadores = dict()
print("Valores sorteados: ")
for j in range(1,5):
    jogadores["jogador"+str(j)] = randint(1,6)
    print(f"  O jogador {j} tirou {jogadores['jogador'+str(j)]}")
    sleep(1)
print("Ranking dos jogadores: ")
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f"  {n}º lugar: {i} com {jogadores[i]}")
    n +=1
    sleep(1)