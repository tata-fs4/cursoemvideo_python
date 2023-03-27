# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
gol= list() 
jogador = dict()
jogador["nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(0, partidas):
    gol.append(int(input(f"Quantos gols na partida {i}? ")))

jogador["gols"] = gol[:]
jogador["total"] = sum(gol)

print("-="*40)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")

print("-="*40)


print(f"O jogador {jogador['nome']} jogou {partidas} partidas")

for i, v in enumerate(jogador["gols"]):
    print(f"   => Na partida {i}, fez {v} gols.")

print(f"Foi um total de {jogador['total']} gols.")