# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print("-="*20)
print("Empréstimo Bancário")
print("-="*20)
valor = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o valor do seu salário? R$ "))
anos= float(input("Quantos anos de financiamento? "))
prestacaomensal= (valor)/(anos*12)
print(f"Para pagar uma casa de R$ {valor:.2f} em {anos} anos", end="")
print(f" a prestação será de R$ {prestacaomensal:.2f}.")
if salario <= (prestacaomensal*0.30):
    print("O empréstimo bancário foi APROVADO!")
else:
    print(f"O empréstimo bancário foi NEGADO, o mínimo é de R$ {prestacaomensal*0.30:.2f}!")