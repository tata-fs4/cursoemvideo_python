# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

pessoa = dict()
pessoa["nome"] = str(input("Nome: "))
anonasc = int(input("Ano de Nascimento: "))
pessoa["idade"] = date.today().year - anonasc
pessoa["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salário"] = float(input("Salário: R$"))
    pessoa["aposentadoria"] = pessoa["idade"]+(35-(date.today().year - pessoa["contratação"]))
print("-="*30)
print(pessoa)

for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")