import streamlit as st 
from pathlib import Path

# Contenido de la página
st.title("Gráficas")

st.markdown("### WIP")

# Mostrar el codigo de la página
st.code(Path("pages/charts.py").read_text(), language="python")