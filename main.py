import selectors
import streamlit as st
import math

paginas = ["Menu principal", "Equação do segundo grau",
           "Conversão de temperaturas"]

sidebar = st.sidebar.selectbox("Selecione uma função", paginas)

if sidebar == "Menu principal":
    st.markdown('''# Calculadora de funções ''')
    st.markdown('''## Bem vindo ao Stayline''')
    st.markdown('''Selecione uma função no menu a esquerda''')

elif sidebar == "Equação do segundo grau":
    st.title('Resolução equação do segundo grau')
    st.markdown(f'''## escreva os termos em seus respectivos espaços: ''')
    formula = r"\Large ax² + bx + c = 0"
    st.latex(formula)

    # ICOGNITAS

    wrong_number = 0

    a = st.number_input("Termo A", value=1, step=1)

    while True:
        if a == wrong_number:
            st.warning(
                'É preciso que pelo menos o termo "A" seja preenchido para obter uma resposta')
            break
        else:
            break

    b = st.number_input("termo B", value=0, step=1)
    c = st.number_input("termo C", value=0, step=1)

    a2 = a
    b2 = b
    c2 = c

    # CODIGO

    # EQUAÇÃO COMPLETA E IMCOMPLETA

    # DELTA

    delta = int(b ** 2 - 4 * a * c)
    deltaraiz = delta ** (1/2)

    if deltaraiz == int(delta):
        if a == 0:
            if st.button('Resposta'):
                st.markdown(
                    '''## É preciso que pelo menos o termo "A" seja preenchido para obter uma resposta''')

            # DELTA MENOR QUE 0
        elif delta < 0:

            if st.button('Resposta'):
                st.markdown('''## X não pertence a R''')
                st.markdown(f'''## Delta é igual a: {delta}''')

            # DELTA = 0
        elif delta == 0:
            x = int(-(b2) + delta**(1/2))
            l = int(2 * a2)
            s = x / l
            if s == int(s):
                if st.button('Resposta'):
                    answer =  fr"\Large x = {int(s)}"
                    st.latex(answer)
                    st.markdown(f'''## Delta é igual a: {delta}''')

            else:

                if st.button('Resposta'):
                    answer = fr"\Large \frac{{{x}}}{l}"
                    st.latex(answer)
                    st.markdown(f'''## Delta é igual a: {delta}''')

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
                    st.markdown(f'''## Delta é igual a: {delta}''')

            elif x1r == int(x1r) and x2r == float(x2r):
                if st.button('Resposta'):
                    answer = fr"\Large x' = {int(x1r)} \newline x'' = \frac{{{x2}}}{l2}"
                    st.latex(answer)
                    st.markdown(f'''## Delta é igual a: {delta}''')

            elif x1r == float(x1r) and x2r == int(x2r):
                if st.button('Resposta'):
                    answer = fr"\Large x' = \frac{{{x1}}}{l1} \newline x'' = {int(x2r)}"
                    st.latex(answer)
                    st.markdown(f'''## Delta é igual a: {delta}''')

            elif x1r == float(x1r) and x2r == float(x2r):
                if st.button('Resposta'):
                    answer = fr"\Large x' = \frac{{{x1}}}{l1} \newline x'' = \frac{{{x2}}}{l2}"
                    st.latex(answer)
                    st.markdown(f'''## Delta é igual a: {delta}''')
    else:
        if st.button('Resposta'):
                st.markdown('''## Delta não tem uma raiz Exata''')
                st.markdown(f'''## Delta é igual a {delta}''')

elif sidebar == "Conversão de temperaturas":

    # TITULOS

    st.markdown('''# Conversão de temperaturas''')
    st.markdown('''## Adicione apenas uma temperatura''')

    # ICOGNITAS

    c = st.number_input("Celsius", value=0.0)

    f = st.number_input("Fahrenheit", value=32.0)

    k = st.number_input("Kelvin", value=273.15)

    if c != 0:

        # CELSIUS PARA:

        # CELSIUS PARA KELVIN
        ck = float(c + 273.15)

        # CELSIUS PARA FAHRENHEIT
        frc = float(c * 9 + 160)
        cf = float(frc / 5)

        if st.button('Resposta'):
            st.markdown(f'''## Kelvin: {round(ck,3)}''')
            st.markdown(f'''## Fahrenheit: {round(cf,3)}''')

    elif k != 273.0:

        # KELIVIN PARA

        # KELVIN PARA CELSIUS

        kc = float(k - 273.15)

        # KELVIN PARA FAHRENHEIT

        frc = float(k * 9 + 160 - 2458.35)
        kf = float(frc / 5)

        if st.button('Resposta'):
            st.markdown(F'''## Celsius: {round(kc,3)}''')
            st.markdown(F'''## Fahrenheit: {round(kf,3)}''')

    elif f != 32.0:
        # FAHRENHEIT PARA

        # FAHRENHEIT PARA CELSIUS

        frc = float(f * 5 - 160)
        fc = float(frc / 9)

        # FAHRENHEIT PARA KELVIN

        frc = float(f * 5 + 2298.35)
        fk = float(frc / 9)

        if st.button('Resposta'):
            st.markdown(F'''## Celsius: {round(fc,3)}''')
            st.markdown(F'''## Kelvin: {round(fk,3)}''')


# DEMONSTRAÇÃO DO CÓDIGO

st.divider()

codigo = st.expander("Mostrar código")

with codigo:
    with open('main.py', 'r') as main:
        codigo = main.read()

    st.code(codigo, language='python')

st.markdown('''**Desenvolvido por Luca Battesini**''')
