import streamlit as st

def porcentagem():
    st.markdown("# Calculos com porcentagem")

    if st.button("Porcentagem de um valor"):
        number1 = st.number_input("Valor")
        number2 = st.number_input("Igual a x% de")
    
    if st.button("valor de uma porcentagem"):
        porcento = st.number_input("Porcentagem")
        number = st.number_input("De")

    
    
    #DMONSTRAÇÃO DO CÓDIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('porcentagem.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
