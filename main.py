import streamlit as st
from src.models.gerador_senhas import gerador

st.set_page_config(
    page_title='Miscelânea de coisas',
    layout='wide'
)

st.title('Miscelânea de ferramentas')

tbInicial, tbSenha, tbAdivinhe = st.tabs(['Inicio', 'Gerador de senhas', 'Jogo de advinhação'])

with tbSenha:
    gerador()

with tbAdivinhe:
    st.markdown("# <div style='text-align:center;'>:red[Em desenvolvimento]</div>", unsafe_allow_html=True)
    st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')