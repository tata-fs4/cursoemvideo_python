# Faça um algoritmo que leia O salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o valor do salário: R$"))
aumento = salario*1.15
print(f"O salário do funcionário é: R${salario}")
print(f"O novo salário do funcionário com 15% de aumento será: R${aumento:.2f}")