# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

def linha():
    print("="*20)
linha()
print("Analisador de Triângulos")
linha()
n1= float(input("Primeiro segmento: "))
n2= float(input("Segundo segmento: "))
n3= float(input("Terceiro segmento: "))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
    if n1==n2==n3:
        print("EQUILÁTERO!")
    elif n1!= n2 != n3 != n1:
        print("ESCALENO")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")