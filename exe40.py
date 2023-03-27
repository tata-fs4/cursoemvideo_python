# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - MÉDIA 7.0 ou superior: APROVADO
def linha():
    print("="*20)
linha()
print("Calculadora de Nota")
linha()
nota1= float(input("Digite a nota 1 do aluno: "))
nota2= float(input("Digite a nota 2 do aluno: "))
media= (nota1+nota2)/2
if media >= 7:
    print(f"Parabéns! Você está aprovado, sua nota média foi {media:.1f}!")
elif 7 > media >=5:
    print(f"Você está em recuperação, sua nota média foi {media:.1f}!")
else:
    print(f"Você está reprovado, sua nota média foi {media:.1f}!")