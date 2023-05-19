import selectors
import streamlit as st
import math
from equation import equacao
from termology import termologia

paginas = ["Menu principal", "Equação do segundo grau",
           "Conversão de temperaturas"]

sidebar = st.sidebar.selectbox("Selecione uma função", paginas)


if sidebar == "Menu principal":
    st.markdown('''# Calculadora de funções ''')
    st.markdown('''## Bem vindo ao Stayline''')
    st.markdown('''Selecione uma função no menu a esquerda''')

elif sidebar == "Equação do segundo grau":
    equacao()

elif sidebar == "Conversão de temperaturas":
    termologia()
    

