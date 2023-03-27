# Funções para votação
#   Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    global idade
    idade = date.today().year - ano
    if idade < 16:
        return "Voto Negado"
    elif idade >= 18 and idade < 70:
        return "Voto Obrigatório"
    else:
        return "Voto Opcional"


nascimento = int(input("Informe a data de nascimento: "))
voto(nascimento)
print(f"Com {idade} anos: {voto(nascimento)}")