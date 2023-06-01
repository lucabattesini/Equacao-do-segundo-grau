import streamlit as st

def porcentagem():
    st.markdown("# Calculos com porcentagem")
    st.markdown("Deixe como 0 os números indefinidos")

    coluna1, coluna2 = st.columns(2)

    with coluna1:
        total = st.number_input("Número total")
        subtotal = st.number_input("Parte do número total")
    with coluna2:
        porcento = st.number_input("Porcentagem", value=100)
        number = st.number_input("Porcentagem do número total")
    
    if number == 0:
        subtotal2 = subtotal * porcento
        s = subtotal2 / total
        if st.button("resposta"):
            st.markdown(f"## {subtotal} é igual a {s}% de {total}")
    
    elif subtotal == 0:
        total2 = total * number
        s = total2 / porcento
        if st.button("resposta"):
            st.markdown(f"## {number}% de {total} é igual a {s}")
    
    elif total == 0:
        subtotal2 = subtotal * porcento
        s = subtotal2 / number
        if st.button("resposta"):
            st.markdown(f"{subtotal} é igual a {number}% de {total}")
    

    
    #DEMONSTRAÇÃO DO CÓDIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('porcentagem.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
