import random
from string import ascii_letters, digits, punctuation

import streamlit as st


def gerador():
  tamanho = st.number_input('Informe o tamanho da senha que deseja:', format='%d', min_value=8)
  senha = ''
  
  for item in range(tamanho):
    caracteres = (ascii_letters+punctuation+ascii_letters).replace('\\', '')
    opcao = random.randint(0, len(caracteres)-1)
    senha += caracteres[opcao]
  st.code(f'''{senha}''', language='python')

if __name__ == '__main__':
   gerador()
