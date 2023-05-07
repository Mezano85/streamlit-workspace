import streamlit as st 
from pathlib import Path

st.title("Estructura de páginas")

st.write(
    """ 
        ---
        ## default
        
        Streamlit por default maneja una forma de estructura multi-página, pero este 
        metodo implica una forma en el nómbre del archivo python que incluso debe contener 
        un icono se es que se quiere mostrar en el menú.  La estructura default es:
    """
)
st.code("{número de página}_{icono}_nombre_de_la_pagina.py", language="sh")
st.write(
    """
        * Número de página: Este número proporciona el orden con el que se verá en el menú
        de páginas.
        
        * icono: Icono que aparece a ún lado del nombre de la página en el menú.
        
        * Nombre de la página: El el nombre que aparecerá en el menú, los _ aparecerán como espacios en blanco.
        
        Estos archivos deben ser almacenados en la carpeta _pages_.
    """
)
st.markdown(
    """
        ---
        ## st_pages
        
        En este proyecto utilizaremos la librería **st_pages** para administrar la
        estructura de páginas en el proyecto. La forma más simple de utilizar la estructura de 
        paginas es con el archivo:
    """
)
st.code(".streamlit/pages.toml", language="sh")
st.markdown(
    """ 
        El codigo para que sea considerado el archivo de configuración se debe ubicar en el app.py.
    """
)
st.code(
    """ 
        from st_pages import show_pages_from_config
        show_pages_from_config()
    """,
    language = "python"
)
st.markdown(
    """ 
        En el archivo se definen 3 elementos para cada página:
        
        * path
        * name
        * icon
        
        Aquí el contenido del archivo pages.toml de este proyecto:
    """
)
st.code(Path(".streamlit/pages.toml").read_text(), language="toml")
st.markdown(
    """ 
    por acá la lista de [iconos](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
    
    """
)

# Mostrar el codigo de la página
st.code(Path("pages/pages.py").read_text(), language="python")