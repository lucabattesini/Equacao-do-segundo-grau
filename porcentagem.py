import streamlit as st
import math 
import random

def porcentagem():
    st.markdown("# Calculos com porcentagem")
    st.markdown("## Selecione sua função")

    xy = st.expander("X são quantos % de Y?")
    xy2 = st.expander("Quanto é X % de Y")
    xy3 = st.expander("X é igual a  Y % de")
 

    with xy:
        coluna, coluna1 = st.columns(2)
        with coluna:
            a = st.number_input("X", value = 0, key="k1")
        with coluna1:
            b = st.number_input("Y", value= 0, key="k2")
        if st.button("Resposta", key="resposta1"):
            st.markdown("Resposta")
    with xy2:
        coluna2, coluna3 = st.columns(2)
        with coluna2:
            c = st.number_input("X", value= 0, key="k3")
        with coluna3:
            d = st.number_input("Y", value= 0, key="k4")
        if st.button("Resposta", key="resposta2"):
            st.markdown("Resposta")
    with xy3:
        coluna4, coluna5 = st.columns(2)
        with coluna4:
            e = st.number_input("X", value= 0, key="k5")
        with coluna5:
            f = st.number_input("Y", value= 0, key="k6")
        if st.button("Resposta", key="resposta3"):
            st.markdown("Resposta")
        

    
    #DEMONSTRAÇÃO DO CÓDIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('porcentagem.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
