import streamlit as st 
from pathlib import Path
from datetime import date

# Contenido de la página
st.title("Entradas")


st.write(
    """
    ---
    ## st.button
    """
    )
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button('Haz clic aquí'):
    st.session_state.count += 1
if st.session_state.count > 0:
    st.write(f'¡El botón ha sido pulsado **{st.session_state.count}** veces!')
else:
    st.write("El boton no ha sido pulsado!!")




st.write(
    """
    ---
    ## st.selectbox
    """
)
option = st.selectbox(
    'Que te parece esta sencilla documentación?',
    ('Esta muy buena', 'Esta bien', 'Mas o menos', 'Lo puedo mejorar'))
st.write(f'Has seleccionado la opción: **{option}**')
st.write("OJO: Tu opinion no será tomada en cuenta...  pero si lo puedes mejorar, espero tu aporte en [GitHub](https://github.com/Mezano85/streamlit-workspace)")



st.write(
    """
    ---
    ## st.multiselect
    """
)
options = st.multiselect(
    'Elige tus animales favoritos:',
    ["🦄", "🐲", "🐶", "🐱", "🐭", "🐹", "🐰", "🐻", "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐙", "🐬", "🐠", "🐳"]
)
st.write('Has seleccionado:', options)



st.write(
    """
    ---
    ## st.radio
    """
    )
radio = st.radio(
    "¿Cuantas horas duermes al día?",
    ('8 horas, como debe ser.', '6 horas, pero bien dormidas.', '4 horas, estoy enganchado con una serie de Netflix.'))
st.write(f'Has seleccionado la opción: **{radio}**')




st.write(
    """
    ---
    ## st.slider
    """
    )
personality = st.slider('¿Qué tan valiente eres?', min_value=0, max_value=10, value=5, step=1)
if personality < 3:
    st.write('Eres el superhéroe "Chickeneer". Tu habilidad especial es correr tan rápido como puedas para escapar de cualquier peligro.')
elif personality >= 3 and personality < 7:
    st.write('Eres el superhéroe "Slightly-Man". Tu habilidad especial es ser un poco mejor que el promedio en todo lo que haces.')
else:
    st.write('Eres el superhéroe "Captain Procrastination". Tu habilidad especial es postergar cualquier tarea hasta el último minuto posible y aún así lograr hacerla.')





st.write(
    """
    ---
    ## st.date_input
    """
    )
# Establecemos la fecha mínima y máxima
fecha_min = date(2000, 1, 1)
fecha_max = date.today()
# Creamos el selector de fecha con la fecha mínima y máxima establecidas
fecha_seleccionada = st.date_input('Selecciona la fecha de cumpleaños de mi unicornio', value=fecha_max, min_value=fecha_min, max_value=fecha_max)
# Mostramos la fecha seleccionada
if fecha_seleccionada.month == 1 and fecha_seleccionada.day == 3:
    st.write('¡Esa es la fecha correcta! Mi unicornio cumple años ese día. 🦄🎉')
else:
    st.write('Lo siento, esa no es la fecha correcta. Por favor, vuelve a intentarlo. 🤔')
    

st.write(
    """
    ---
    ## Documentación...
    La documentación de streamlit es muy buena, por acá solo puse las que me ha tocado utilizar, pero puedes consultar más [por acá](https://docs.streamlit.io/library/api-reference/widgets).
    """
    )

# Mostrar el codigo de la página
st.write("---")
st.code(Path("pages/inputs.py").read_text(), language="python")