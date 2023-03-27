# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
from datetime import date

def linha():
    print("="*20)
linha()
print("Categoria do Atleta - Confederação Nacional de Natação")
linha()

ano= int(input("Digite o ano de nascimento: "))
idade= (date.today().year)-ano
if idade <= 9:
    print("O(a) atleta está na categoria Mirim!")
elif idade <=14:
    print("O(a) atleta está na categoria Infantil!")
elif idade <=19:
    print("O(a) atleta está na categoria Junior!")
elif idade <=20:
    print("O(a) atleta está na categoria Sênior!")
else:
    print("O(a) atleta está na categoria Master!")