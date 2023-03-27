# Transformando módulos em pacotes
# Dentro do pacote que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from exe112.utilidadescev import moeda
from exe112.utilidadescev import dados

print('\33c')
p = dados.leiaDinheiro('Digite um valor: R$')
moeda.resumo(p, 60, 45)