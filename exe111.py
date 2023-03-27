# Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from exe111.utilidadescev import moeda

print("\33c")
p = float(input("Digite um valor: R$"))
moeda.resumo(p, 60, 45)