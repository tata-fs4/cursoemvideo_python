# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    print("-"*(len(txt)+4))
    print(f"  {txt}  ")
    print("-"*(len(txt)+4))
    
escreva("Curso em vídeo!")
escreva("Curso de Python no YouTube")