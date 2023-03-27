# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
print("-="*20)
print("Conversor de número: binário, octal ou hexadecimal")
print("-="*20)

n = int(input("Escreva um número inteiro qualquer: "))
print("""Escolha uma das base para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL""")
opção= int(input("Sua opção: "))

if opção==1:
    print(f"Número {n} convertido para binário: {bin(n)[2:]}.")
elif opção==2:
    print(f"Número {n} convertido para octal: {oct(n)[2:]}.")
elif opção==3:
    print(f"Número {n} convertido para hexadecimal: {hex(n)[2:]}")
else:
    print("Opção inválida, tente novamente!")