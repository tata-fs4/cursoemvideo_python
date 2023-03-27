# Reduzindo ainda mais seu programa
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from exe110 import moeda
print('\33c')
p = float(input('Digite um valor: R$ '))
moeda.resumo(p, 30, 78)