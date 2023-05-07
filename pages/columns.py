import streamlit as st 
from pathlib import Path

# Contenido de la página
st.title("Columnas")

st.write(
    """ 
        En Streamlit, se pueden utilizar columnas para organizar y distribuir el contenido 
        de la aplicación. Las columnas permiten que el contenido se muestre en múltiples columnas, 
        lo que facilita la lectura y la navegación para el usuario.

        Para utilizar columnas en Streamlit, se puede utilizar la función st.columns(). 
        Esta función devuelve una lista de objetos de columna, que se pueden utilizar para colocar 
        el contenido de la aplicación en las columnas deseadas.

        Por ejemplo, si deseas mostrar dos bloques de contenido lado a lado, 
        se pueden utilizar dos columnas, de la siguiente manera:
         
    """)

# mensaje en dos columnas
col1, col2 = st.columns(2)
with col1:
    st.write(
        """ 
            ---
            El contenido de este texto esta en la primer columna, separar las columas de esta forma genera que ambas 
            estén del mismo tamaño.
        """
    )
with col2:
    st.write(
        """ 
            ---
            Este es el contenido de la segunda columna, que también es del mismo tamaño que la primera.
        """
    )
    
st.write(
    """ 
        ---
        También es posible definir el tamaño de las columnas, esto es por medio de definir 
        el tamaño de la proporción de la siguiente forma:
    """
)

col1, col2 = st.columns([8 ,2])
with col1:
    st.write(
        """ 
            ---
            Para este caso, el tamaño de la columna 1 es del 80 por ciento del espacio, esta cifra
            puede ser expresada en diferentes valores, por ejemplo: [4,1], [8,2].
        """
    )
with col2:
    st.write(
        """ 
            ---
            Esta columná queda mucho más pequeña.
        """
    )

# Mostrar el codigo de la página
st.code(Path("pages/columns.py").read_text(), language="python")