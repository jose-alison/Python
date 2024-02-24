import sys

from Advinhe_o_numero.main import partida as adivinhe
from Gerador_de_senhas.main import gerador as gerador


def main():
    try:
        escolha = 0
        while escolha < 1 or escolha > 2:
            escolha = int(input('''O que deseja fazer hoje?
              [1] Gerar uma senha
              [2] Jogar Adivinhe o número e testar sua sorte
              '''))
        if escolha == 1:
            gerador()
        elif escolha == 2:
            adivinhe()
    except Exception as e:
        print('Ocorreu um problema na execução do código:', e)
    finally:
        opc = input('Deseja continuar? (S/N)').upper()
        while opc not in ('S', 'N'):
            opc = input('Deseja continuar? (S/N)').upper()
        
        if opc == 'S':
            main()
        else: 
            sys.exit()


if __name__ == "__main__":
    main()