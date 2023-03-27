# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram: ",end = "")
for n in tupla:
    print(f"{n} ", end="")
print(f"\nO maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")