import streamlit as st

from src.inferencia import prever

st.set_page_config(
    page_title="Diário Oficial Inteligente de Avaré",
    page_icon="📄"
)

st.title("📄 Diário Oficial Inteligente de Avaré")

st.write(
    "Digite um trecho do Diário Oficial para classificar."
)

texto = st.text_area(
    "Texto",
    height=220
)

if st.button("Classificar"):

    if texto.strip() == "":

        st.warning("Digite um texto.")

    else:

        classe = prever(texto)

        st.success(f"Classe prevista: **{classe}**")