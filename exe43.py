# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
def linha():
    print("="*20)
linha()
print("Calculadora IMC")
linha()
peso = float(input("Qual é seu peso? (Kg)"))
altura = float(input("Qual é sua altura? (m) "))
imc =  peso/(altura*altura)
if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso!")
elif imc<=25>18.5:
    print(f"Seu IMC é {imc:.2f}, você está com peso ideal!")
elif imc<=30>25:
    print(f"Seu IMC é {imc:.2f}, você está com sobrepeso!")
elif imc<=40>30:
    print(f"Seu IMC é {imc:.2f}, você está com OBESIDADE!")
else:
    print(f"Seu IMC é {imc:.2f}, você está com OBESIDADE MÓRBIDA!")