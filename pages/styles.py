import streamlit as st 
from pathlib import Path

# Contenido de la página
st.title("Estilos y Temas")

st.markdown("### WIP")

# Mostrar el codigo de la página
st.write("---")
st.code(Path("pages/styles.py").read_text(), language="python")