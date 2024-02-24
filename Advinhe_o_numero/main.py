import random as rd


def nivel():
    escolha = int(input('Escolha um nível: \n[1] Fácil (10 números) \n[2] Médio (50 números) \n[3] Difícil (100 números): \n'))
    while escolha < 1 or escolha > 3:
      escolha = int(input('Escolha um nível: \n[1] Fácil (10 números) \n[2] Médio (50 números) \n[3] Difícil (100 números): \n'))
    
    nivel = {
      1: 10,
      2: 50,
      3: 100
    }
    return nivel.get(escolha)

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

if __name__ == '__main__':
  partida(nivel())    
  