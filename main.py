import selectors
import streamlit as st
import math
from equation import equacao
from termology import termologia
from menu import menu

paginas = ["Menu principal", "Equação do segundo grau",
           "Conversão de temperaturas"]

sidebar = st.sidebar.selectbox("Selecione uma função", paginas)


if sidebar == "Menu principal":
    menu()

elif sidebar == "Equação do segundo grau":
    equacao()

elif sidebar == "Conversão de temperaturas":
    termologia()
    

