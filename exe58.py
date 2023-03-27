from random import randint
computador = randint(0, 10)
print("Acabei de pensar em um número de 0 a 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print(f"Acertou!! Utilizou {palpites} tentativas. Parabéns.")