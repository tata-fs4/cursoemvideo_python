# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a 1250 reais, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
funcio = str(input("Digite o nome do funcionário: "))
sal = float(input("Digite o salário atual: R$"))

if sal> 1250:
    print(f"O funcionário {funcio} terá um aumento de {sal*0.10}")
else:
    print(f"O funcionário {funcio} terá um aumento de R${sal*0.15}!")