# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

def linha():
    print("="*20)
linha()
print("Calculadora de tempo de alistamento")
linha()
data = int(input("Informe o seu ano de nascimento: "))
ano= (date.today().year)-data
if ano<18:
    print(f"Falta {18-ano} anos para se alistar!")
elif ano==18:
    print(f"Está na hora de se alistar! Você já possui {ano} anos.")
else:
    print(f"Você passou {ano-18} anos do tempo de alistamento!")