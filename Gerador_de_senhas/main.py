import random

def gerador(tamanho):
  letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'l', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  
  especiais = ['/', '*', '-', '+', '.', '-', '_', '^', '[', ']', 
             '{', '}', '?', '&', '%', '$', '#', '~', '@', '!']
  senha = ''
  
  for item in range(tamanho):
    opcao = random.randint(1, 4)
    if opcao == 1:
      caracter = letras[random.randint(0, len(letras)-1)]
    elif opcao == 2:
      caracter = letras[random.randint(0, len(letras)-1)].upper()
    elif opcao == 3:
      caracter = numeros[random.randint(0, len(numeros)-1)]
    elif opcao == 4:
      caracter = especiais[random.randint(0, len(especiais)-1)]
    senha = senha + senha.join(caracter)

  return senha


def main():
  num_caracter = int(input('Qual o tamanho de senha desejado? '))
  return gerador(num_caracter)
