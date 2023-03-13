
import streamlit as st
import pandas as pd

st.title('Conversor')

file = st.file_uploader("Inserir CSV", type=['csv'])

if file is not None:
    df = pd.read_csv(file)

    st.download_button(
        label="Baixar resultados",
        data=df.to_csv(),
        file_name='resultados.csv'
    )




