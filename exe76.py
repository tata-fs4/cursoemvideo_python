# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
def linha():
    print("="*30)
linha()
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

linha()
print("{:^50}".format("LISTAGEM DE PREÇOS"))
linha()

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

linha()