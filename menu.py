import streamlit as st
from equation import equacao
from termology import termologia

def menu():
    st.markdown("# Bem vindo ao Stayline")
    st.markdown("## Calculadora de funções")
    if st.button("Equações do segundo grau"):
        equacao()
    if st.button("termologia"):
        termologia()