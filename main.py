import streamlit as st
import math


st.title('Resolução equação do segundo grau')

st.markdown('''## escreva os termos em seus respectivos espaços: aX² + bX + c = 0''')


#ICOGNITAS

a = st.number_input("Termo A", value=0, step=1)
b = st.number_input("termo B", value=0, step=1)
c = st.number_input("termo C", value=0, step=1)

a2 = a
b2 = b
c2 = c


#CODIGO


    #EQUAÇÃO COMPLETA E IMCOMPLETA

    #DELTA
delta = int(b**2 -4*a*c)


if a == 0:
    if st.button('Resposta'):
        st.markdown('''## É preciso que pelo menos o termo "A" seja preenchido para obter uma resposta''')
                

    #DELTA MENOR QUE 0
elif delta < 0:

    if st.button('Resposta'):
        st.markdown('''## X não pertence a R''')
        st.markdown(f'''## Delta é igual a: {delta}''')

    #DELTA = 0
elif delta == 0:
    x = int(-(b2) + delta**(1/2))
    l = int(2 * a2)
    s = int(x / a2)

    if st.button('Resposta'):
        st.markdown(f'''## X é igual a: {s}''')
        st.markdown(f'''## Delta é igual a: {delta}''')

    #DELTA MAIOR QUE 0
elif delta > 0:
    radiciação = int((delta**(1/2)))

    x1 = int(-1 *b2 + radiciação)
    x2 = int(-1 *b2 - radiciação)
            
    l1 = int(2 * a2)
    l2 = l1

    x1r = int(x1 / l1)
    x2r = int(x2 / l2)

    if st.button('Resposta'):
        st.markdown(f'''## X1 = {x1r} \n ## X2 = {x2r}''')
        st.markdown(f'''## Delta é igual a: {delta}''')



#DEMONSTRAÇÃO DO CÓDIGO


codigo = st.expander("Mostrar código")

with codigo:
    with open('main.py', 'r') as main:
        codigo = main.read()

    st.code(codigo, language='python')

