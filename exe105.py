# Validando entrada de dados em Python
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#    - Quantidade de notas
#    - A maior nota
#    - A menor nota
#    - A média da turma
#    - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*n, s=False):
    """[Notas]
    Função para categorizar dados(Notas) a serem informadas 
    não inporta a quantidade de notas 
    Returns:
        [dici["total"]] -- [Retorna o valor total de notas]
        [dici["maior"]] -- [Retorna o valor maior das notas]
        [dici["menor"]] -- [Retorna o valor menor das notas]
        [dici["média"]] -- [Retorna o valor a médias das notas]
        [dici["situação"]] -- [Retorna a situação do aluno]
    """
    dici = dict()
    dici["total"] = len(n)
    dici["maior"] = max(n)
    dici["menor"] = min(n)
    dici["média"] = (sum(n) / (dici["total"]))

    if s == True:
        if dici["média"] >= 7:
            dici["situação"] = "BOA"
        elif dici["média"] >= 5:
            dici["situação"] = "RAZOÁVEL"
        else:
            dici["situação"] = "RUIM"
    return dici

def linhas():
    print("-"*55)


#Programa princinpal
linhas()
print(notas(5.5, 9.5, 10, 6.5, s=True))
linhas()
help(notas)