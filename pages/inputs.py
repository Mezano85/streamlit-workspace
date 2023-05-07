import streamlit as st 
from pathlib import Path

# Contenido de la página
st.title("Entradas")

st.markdown("### WIP")

# Mostrar el codigo de la página
st.code(Path("pages/inputs.py").read_text(), language="python")