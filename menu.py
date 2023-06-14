import streamlit as st
from equation import equacao
from termology import termologia

def menu():
    st.markdown("# Bem vindo ao Stayline")
    st.markdown("## Calculadora de funções")

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('menu.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
