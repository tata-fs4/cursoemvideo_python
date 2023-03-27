# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considerando o dolar a 5.22
carteira = float(input("Digite o valor na carteira: R$"))
dolar = carteira/5.22
print(f"Com R${carteira:.2f} é possível comprar US${dolar:.2f}!!!")