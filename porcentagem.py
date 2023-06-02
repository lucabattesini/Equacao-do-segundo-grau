import streamlit as st

def porcentagem():
    st.markdown("# Calculos com porcentagem")
    st.markdown("Deixe como 0 os números indefinidos")

    coluna1, coluna2 = st.columns(2)

    with coluna1:
        total = st.number_input("Número total", value=0)
        subtotal = st.number_input("Parte do número total", value=0)
    with coluna2:
        porcento = st.number_input("Porcentagem", value=100)
        subporcento = st.number_input("Porcentagem do número total", value=0)

    if subporcento == 0:
        if total == 0:
            st.warning(f"## Não é possivel dividir números por 0")
        else:
            subtotal2 = subtotal * porcento
            s = subtotal2 / total
            if st.button("resposta"):
                st.markdown(f"## {subtotal} é igual a {s}% de {total}")
    
    elif subtotal == 0:
        total2 = total * subporcento
        s = total2 / porcento
        if st.button("resposta"):
            st.markdown(f"## {subporcento}% de {total} é igual a {s}")
    
    elif total == 0:
        subtotal2 = subtotal * porcento
        s = subtotal2 / subporcento
        if st.button("resposta"):
            st.markdown(f"## {subtotal} é igual a {subporcento}% de {s}")
    

    
    #DEMONSTRAÇÃO DO CÓDIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('porcentagem.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
