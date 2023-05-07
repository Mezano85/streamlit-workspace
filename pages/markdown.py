import streamlit as st 
from pathlib import Path

st.title("Markdown")

st.write(
    """ 
    ---
    En Streamlit, **st.write** y **st.markdown** son dos formas diferentes de mostrar texto en una aplicación. 
    La principal diferencia es que **st.write** es más flexible y puede manejar una amplia variedad de tipos de datos, 
    mientras que **st.markdown** se utiliza específicamente para mostrar texto con formato de Markdown.

    La función **st.write** puede manejar varios tipos de datos, como cadenas de texto, números, listas, 
    diccionarios, marcos de datos (DataFrames), entre otros. La función detecta automáticamente el 
    tipo de dato que se le pasa y lo muestra de manera adecuada.

    Por otro lado, la función **st.markdown** se utiliza específicamente para mostrar texto con formato de Markdown. 
    Esto significa que el texto puede contener elementos como encabezados, enlaces, imágenes, énfasis en el texto y 
    otros elementos que se pueden formatear con Markdown.

    En resumen, si solo necesitas mostrar texto sin formato, **st.write** es una buena opción. 
    Pero si deseas formatear el texto con elementos de Markdown, como encabezados, enlaces, 
    listas, etc., entonces st.markdown es la opción correcta.
    """
)

st.markdown(
    """ 
        Markdown es un lenguaje de marcado ligero que se utiliza para dar formato al texto.
        La mayoría de las plataformas de colaboración y chat modernas, como GitHub, GitLab, 
        Slack y Discord, admiten la sintaxis de Markdown para dar formato al texto. 
        Esto hace que sea fácil escribir y compartir contenido con otros usuarios sin tener que 
        preocuparse por el diseño complejo o la estructura HTML.
        
        Streamlit nos permite ingresar este tipo de lenguaje de la siguiente forma:
    """
)
st.code(
    """
        import streamlit as st
        st.markdown("Texto en markdown")
    """,
    language = "python"
)
st.markdown(
    """ 
        ---
        ### Codigo
        
        Aunque streamlit tiene la opción code, markdown tiene esta opción en un formato simple:
        
        ``Todo esto es `código`.``
    """
)
st.markdown(
    """   
        ---      
        ### Negrita y Cursiva
        
        *Texto en cursiva*
        _Texto en cursiva_
        **Texto en negrita**
        __Texto en negrita__
        ***Texto en cursiva y negrita***
        ___Texto en cursiva y negrita___
    """
)
st.markdown(
    """
        ---
        ### Color
        Este texto está :red[coloreado en rojo], y este otro **:blue[en azul]** y además en negrita.
    """
)
st.markdown(
    """     
        ---    
        ### Tachado
        
        ~~Este texto está tachado.~~ Y este texto no.
    """
)
st.markdown(
    """ 
        ---
        ### Titulos
        
        # Título 1
        ## Título 2
        ### Título 3
        #### Título 4
        ##### Título 5
        ###### Título 6
    """
)
st.markdown(
    """ 
        ---
        ### Listas
        
        - Elemento de la lista 1
        - Elemento de la lista 2
        - Elemento de la lista 3
        
        1. Elemento de la lista 1
        2. Elemento de la lista 2
        3. Elemento de la lista 3
    """
)
st.markdown(
    """ 
        ---
        ### Links
        
        A continuación se muestra un [Link](https://ejemplo.com/ "Título opcional del enlace").
    """
)
st.markdown(
    """ 
        ---
        ### Tablas
        
        |Columna 1|Columna 2|
        |--------|--------|
        |    A    |    B    |
        |    C    |    D    |
        
    """
)    
st.markdown(    
    """    
        ---
        #### Notas al pie
        
        Puedes colocar [^1] notas en el pie de página [^2] fácilmente.
        [^1]: Aquí encuentras el texto de la nota al pie de página.
        [^2]: **Las notas de pie de página** pueden *formatearse* también.
        Estas pueden ocupar varias líneas.
    """
)
st.markdown(
    """ 
        ---
        ### Imagenes
        
        ![Imagen de Prueba](https://mma.prnewswire.com/media/1695947/IRTNTR71287.jpg)
    """
)

# Mostrar el codigo de la página
st.code(Path("pages/markdown.py").read_text(), language="python")