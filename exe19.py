#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
from random import choice
s = []
for c in range(0,4):
    s.append ( str(input("Nome do aluno: ")) )

print(f"Lista de alunos: ", *s)
print(f"O aluno sorteado para apagar o quadro foi: {choice(s)}")