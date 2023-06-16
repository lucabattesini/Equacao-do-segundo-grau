import streamlit as st
from equation import equacao
from termology import termologia

def menu():
    st.markdown("# Bem vindo ao Stayline")
    st.markdown("## Calculadora de funções")

    if st.button("Sobre"):
        st.markdown("#### Este site foi desenvouvido como objetivo principal o acadêmico de auxiliar o aprendizado e incentivar o estudo e uso da programação. O web-site stayline pode ser utilizado de diversas formas, basta inserir os números no lugar indicado e apertar no botão “resposta”. Inicialmente o site é dividido em quatro partes, o menu principal e suas atuais 3 funções que consistem em termologia, resolução de equações do 2º grau e calculos com porcentagem. Basta apertar na barra lateral no canto esquedo da tela e selecionar a função desejada, tem algo mais facil que isso? Na determinada função que escolha terá um botão escrito “Mostrar código” onde ao apertalo aparecerá todo o codigo escrito para o desenvolvimento de tal função, reforçando o incentivo do estudo da programação.")
    st.divider()
    st.markdown('''**Desenvolvido por Luca Battesini**''')