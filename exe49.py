#  Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tabuada=int(input("Tabuada do numero: "))
def linha():
    print("="*20)
linha()
for count in range(0, 11):
    print(f"{tabuada} x {count} = {tabuada*count}")
linha()