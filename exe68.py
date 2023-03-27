#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

def linha():
    print("="*20)
linha()
print("VAMOS JOGAR PAR OU ÍMPAR")
linha()

count = 0
# pc = n = 0

while True:
    n = int(input("Diga um valor: "))
    pc = random.randint(0, 10)
    soma = n + pc
    PI =" "
    while PI not in "PI":
        PI = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    linha()
    if soma % 2 == 0 and PI == "P":
        print(f"Você jogou {n} e o computador {pc}. Total de {soma} deu PAR")
        linha()
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        count += 1
    elif soma % 2 != 0 and PI == "P":
        print(f"Você jogou {n} e o computador {pc}. Total de {soma} deu ÍMPAR")
        linha()
        print("Você PERDEU!")
        break
    elif soma % 2 != 0 and PI =="I":
        print(f"Você jogou {n} e o computador {pc}. Total de {soma} deu ÍMPAR")
        linha()
        print("Você VENCEU!")
        count += 1
        print("Vamos jogar novamente...")
    elif soma % 2 == 0 and PI == "I":
        print(f"Você jogou {n} e o computador {pc}. Total de {soma} deu PAR")
        linha()
        print("Você PERDEU!")
        break
    linha()
        
linha()
print(f"GAME OVER! Você venceu {count} vezes")