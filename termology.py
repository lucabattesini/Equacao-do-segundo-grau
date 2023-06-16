import streamlit as st

def termologia():
    # TITULOS

    st.markdown('''# Conversão de temperaturas''')
    st.markdown('''## Adicione apenas uma temperatura''')

    # ICOGNITAS

    c = st.number_input("Celsius", value=0.0)

    f = st.number_input("Fahrenheit", value=0.0)

    k = st.number_input("Kelvin", value=0.0)

    if c and f and k == 0:
        if st.button("Resposta"):
            st.markdown("mec")

    elif c != 0:

        # CELSIUS PARA:

        # CELSIUS PARA KELVIN
        ck = float(c + 273.15)

        # CELSIUS PARA FAHRENHEIT
        frc = float(c * 9 + 160)
        cf = float(frc / 5)

        if st.button('Resposta'):
            st.markdown(f'''## Kelvin: {round(ck,3)}''')
            st.markdown(f'''## Fahrenheit: {round(cf,3)}''')

    elif k != 0:

        # KELIVIN PARA

        # KELVIN PARA CELSIUS

        kc = float(k - 273.15)

        # KELVIN PARA FAHRENHEIT

        frc = float(k * 9 + 160 - 2458.35)
        kf = float(frc / 5)

        if st.button('Resposta'):
            st.markdown(F'''## Celsius: {round(kc,3)}''')
            st.markdown(F'''## Fahrenheit: {round(kf,3)}''')

    elif f != 0:
        # FAHRENHEIT PARA

        # FAHRENHEIT PARA CELSIUS

        frc = float(f * 5 - 160)
        fc = float(frc / 9)

        # FAHRENHEIT PARA KELVIN

        frc = float(f * 5 + 2298.35)
        fk = float(frc / 9)

        if st.button('Resposta'):
            st.markdown(f'''## Celsius: {round(fc,3)}''')
            st.markdown(f'''## Kelvin: {round(fk,3)}''')
    
    #VISUALIZAÇÃO DO CODIGO

    st.divider()

    codigo = st.expander("Mostrar código")

    with codigo:
        with open('termology.py', 'r') as main:
            codigo = main.read()

        st.code(codigo, language='python')

    st.markdown('''**Desenvolvido por Luca Battesini**''')
