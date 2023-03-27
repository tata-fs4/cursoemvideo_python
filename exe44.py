# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
def linha():
    print("="*20)
linha()
print("Condições de Pagamento")
linha()
preço= float(input("Qual o valor da compra? R$"))
print(""" FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
forma= int(input("Qual é a opção? "))

if forma==1:
    total = preço*0.90
elif forma==2:
    total = preço*0.95
elif forma==3:
    total = preço
    parcela= total/2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!")
elif forma==4:
    total= preço*1.20
    totparc= int(input("Quantas parcelas? "))
    parcela= total/totparc
    print(F"Sua compra será parcelada em {totparc}x de R${parcela:.2f}.")
else:
    total = preço
    print("OPÇÃO INVÁLIDA de pagamento. Tente Novamente!")
print(f"Sua compra de R${preço:.2F} vai custar R${total:.2f} no final.")