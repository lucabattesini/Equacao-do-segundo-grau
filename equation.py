import streamlit as st
import math

def equacao():
    st.title('Resolução equação do segundo grau')
    st.markdown(f'''## escreva os termos em seus respectivos espaços: ''')
    formula = r"\Large ax² + bx + c = 0"
    st.latex(formula)

    # ICOGNITAS

    wrong_number = 0

    a = int(st.number_input("Termo A", value=1, step=1))

    while True:
        if a == wrong_number:
            st.warning(
                'É preciso que pelo menos o termo "A" seja preenchido para obter uma resposta')
            break
        else:
            break

    b = int(st.number_input("termo B", value=0, step=1))
    c = int(st.number_input("termo C", value=0, step=1))

    a2 = a
    b2 = b
    c2 = c


    # CODIGO

    # EQUAÇÃO COMPLETA E IMCOMPLETA

    # DELTA

    delta = int(b ** 2 - 4 * a * c)
    deltaraiz = delta ** 0.5
    
    if delta < 0:
        if st.button('Resposta'):
                st.markdown('''## X não pertence a R''')
                st.markdown(f'''## Delta é igual a: {delta}''')
    elif delta > 0:            
        if deltaraiz == int(deltaraiz):
            if a == 0:
                if st.button('Resposta'):
                    st.markdown(
                        '''## É preciso que pelo menos o termo "A" seja preenchido para obter uma resposta''')

                # DELTA = 0
            if delta == 0:
                x = int(-(b2) + delta**(1/2))
                l = int(2 * a2)
                s = x / l
                if s == int(s):
                    if st.button('Resposta'):
                        answer =  fr"\Large x = {int(s)}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)

                else:

                    if st.button('Resposta'):
                        answer = fr"\Large \frac{{{x}}}{l}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)

                # DELTA MAIOR QUE 0
            elif delta > 0:
                radiciação = ((delta**(1/2)))

                x1 = int(-1 * b2 + radiciação)
                x2 = int(-1 * b2 - radiciação)

                l1 = int(2 * a2)
                l2 = l1

                x1r = x1 / l1
                x2r = x2 / l2

                if x1r == int(x1r) and x2r == int(x2r):
                    if st.button('Resposta'):
                        answer = fr"\Large x' = {int(x1r)} \newline x'' = {int(x2r)}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)

                elif x1r == int(x1r) and x2r == float(x2r):
                    if st.button('Resposta'):
                        answer = fr"\Large x' = {int(x1r)} \newline x'' = \frac{{{x2}}}{l2}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)

                elif x1r == float(x1r) and x2r == int(x2r):
                    if st.button('Resposta'):
                        answer = fr"\Large x' = \frac{{{x1}}}{l1} \newline x'' = {int(x2r)}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)

                elif x1r == float(x1r) and x2r == float(x2r):
                    if st.button('Resposta'):
                        answer = fr"\Large x' = \frac{{{x1}}}{l1} \newline x'' = \frac{{{x2}}}{l2}"
                        st.latex(answer)
                        answerd = fr'\Large Δ = {delta}'
                        st.latex(answerd)
        else:
            if st.button('Resposta'):
                    st.markdown('''## Delta não tem uma raiz Exata''')
                    answerd = fr'\Large Δ = {delta}'
                    st.latex(answerd)
    # DEMONSTRAÇÃO DO CÓDIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('equation.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')