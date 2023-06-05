# Importar dependencias

import openai
import streamlit as st
from streamlit_chat import message

# accesar a GPT-3 Por medio de la API
openai.api_key = st.secrets["clave"]
st.header("Asistente de Soporte Tecnico")

 # temp = st.slider("temperature", 0.0, 1.0, 0.5)
#funcion que interactua con la API de openia
def respuesta_B(prompt):
    respuesta_bot = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.3
    )
    mensaje=respuesta_bot["choices"][0]["text"]
    return mensaje


if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]    

def obteniendo_texto():
    texto_ingresado= st.text_input("Tu: ","Hola, como estas",key="entrada") 
    return texto_ingresado   



entrada_usuario=obteniendo_texto()

if entrada_usuario:
    salida=respuesta_B(entrada_usuario)

    #debemos almacenar la salida
    st.session_state.past.append(entrada_usuario)
    st.session_state.generated.append(salida)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state["generated"][i],key=str(i))
        message(st.session_state['past'][i],is_user=True,key=str(i)+'_user')    