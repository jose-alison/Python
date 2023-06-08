import random as rd


def nivel():
    escolha = int(input('Escolha um nível: \n[1] Fácil (10 números) \n[2] Médio (50 números) \n[3] Difícil (100 números): \n'))
    if escolha == 1:
      return 10
    elif escolha == 2:
      return 50
    elif escolha == 3:
      return 100
    else:
      escolha = int(input('Escolha um nível: \n[1] Fácil \n[2] Médio \n[3] Difícil: \n'))


def game(nivel):
  numero = rd.randint(1, nivel)

  palpite = int(input(f'Teste sua sorte:\nEscolha um numero entre 1 e {nivel}: '))

  if palpite == numero:
    return print(f'Parabéns, foi exatamente o número {palpite} que eu pensei.\n')
  else:
    return print(f'Que pena, o numero era {numero}.\n')


def partida(nivel):
  partida = 1
  while partida <= 3:
    print(f'****** Partida {partida} de 3 ******')
    game(nivel)
    partida += 1

def main():
  partida(nivel())    

main()