import random
from string import ascii_letters, digits, punctuation


def gerador():
  num_caracter = int(input('Qual o tamanho de senha desejado? '))
  senha = ''
  
  for item in range(num_caracter):
    caracteres = (ascii_letters+punctuation+ascii_letters).replace('\\', '')
    opcao = random.randint(0, len(caracteres)-1)
    senha += caracteres[opcao]
  return f'''{senha}'''

if __name__ == '__main__':
   gerador()
