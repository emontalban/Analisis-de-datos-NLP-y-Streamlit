"""Butaca Emocioal — Día 3: interfaz Streamlit para clasificar reseñas IMDb.

El entrenamiento se realizó previamente en el notebook de NLP.
Esta aplicación SOLO carga el Pipeline guardado y lo utiliza para predecir.
"""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# La ruta se calcula respecto de ESTE archivo, independientemente de
# la carpeta desde la que abramos el terminal.
CARPETA_PROYECTO = Path(__file__).resolve().parent
RUTA_MODELO = CARPETA_PROYECTO / "modelos" / "mood_insights_modelo.joblib"

# Este texto sirve para que cualquier persona entienda qué puede escribir.
EJEMPLOS = {
    "😊 Ejemplo positivo": "Me encantó la película. La historia es preciosa y las actuaciones son excelentes.",
    "😞 Ejemplo negativo": "La película es aburrida, demasiado larga y el final me decepcionó.",
    "🤔 Opinión mixta": "La fotografía es muy buena, pero la historia me pareció aburrida.",
}

st.set_page_config(
    page_title="Butaca Emocioal | Analizador de reseñas",
    page_icon="💺",
    layout="centered",
)


@st.cache_resource(show_spinner="Cargando el modelo entrenado…")
def cargar_modelo():
    """Cargar el modelo una vez y reutilizarlo entre interacciones.

    joblib.load puede ejecutar código al abrir archivos: usar SOLO el modelo
    propio incluido en este proyecto, nunca un archivo subido por terceros.
    """
    if not RUTA_MODELO.is_file():
        raise FileNotFoundError(f"No se encuentra el archivo: {RUTA_MODELO}")
    return joblib.load(RUTA_MODELO)


st.title("💺 Butaca Emocioal")
st.subheader("¿Qué sentimiento transmite una reseña de cine?")
st.write(
    "Escribe una opinión sobre una película y nuestro modelo de Machine Learning "
    "intentará clasificar el texto como **positivo** o **negativo**."
)

with st.expander("📚 ¿Qué aprendió el modelo y cómo funciona?"):
    st.markdown(
        """
        **Día 1 · EDA:** exploramos y limpiamos las reseñas en español de IMDb.

        **Día 2 · NLP + Machine Learning:** usamos `CountVectorizer` para contar
        palabras y `LogisticRegression` para aprender patrones asociados a
        opiniones positivas y negativas. Un `Pipeline` conecta los dos pasos.

        **Día 3 · Streamlit:** cargamos el modelo ya entrenado con `joblib`.
        Cuando pulsas **Analizar reseña**, usamos `predict()` para obtener la
        etiqueta y `predict_proba()` para consultar la puntuación del modelo.

        **Importante:** el modelo no sabe clasificar textos como «neutros» y
        no mide las emociones reales de una persona.
        """
    )

try:
    modelo = cargar_modelo()
except Exception as error:
    st.error("No se ha podido abrir el modelo. Revisa la carpeta `modelos` y las dependencias.")
    st.code(str(error), language="text")
    st.stop()

# El modelo guardado debe reconocer exactamente estas dos etiquetas.
clases = list(modelo.classes_)
if set(clases) != {"positivo", "negativo"}:
    st.error(f"Las clases del modelo no son las esperadas: {clases}")
    st.stop()

# Guardamos la entrada actual entre las interacciones de Streamlit.
if "texto_resena" not in st.session_state:
    st.session_state.texto_resena = ""
if "ultimo_resultado" not in st.session_state:
    st.session_state.ultimo_resultado = None

st.markdown("### ✍️ Prueba el analizador")
seleccion = st.selectbox(
    "¿Quieres cargar una reseña de ejemplo?",
    ["Escribir mi propia reseña", *EJEMPLOS.keys()],
)

# El botón permite volver a cargar un ejemplo sin perder el control sobre el texto.
if seleccion != "Escribir mi propia reseña":
    if st.button("Usar este ejemplo"):
        st.session_state.texto_resena = EJEMPLOS[seleccion]
        st.session_state.ultimo_resultado = None
        st.rerun()

with st.form("formulario_resena"):
    texto = st.text_area(
        "Escribe aquí tu reseña en español:",
        key="texto_resena",
        height=150,
        placeholder="Ejemplo: Me encantó la historia y el final fue emocionante…",
    )
    enviar = st.form_submit_button("🔎 Analizar reseña", type="primary", use_container_width=True)

if enviar:
    texto_limpio = texto.strip()
    if not texto_limpio:
        st.session_state.ultimo_resultado = None
        st.warning("Primero escribe una reseña para poder analizarla.")
    else:
        # El Pipeline incluye la transformación a números.
        prediccion = str(modelo.predict([texto_limpio])[0])
        probabilidades = modelo.predict_proba([texto_limpio])[0]

        # Las probabilidades se identifican por classes_, NUNCA por su posición supuesta.
        puntuaciones = {
            clase: float(valor) for clase, valor in zip(clases, probabilidades)
        }
        st.session_state.ultimo_resultado = {
            "texto": texto_limpio,
            "prediccion": prediccion,
            "puntuaciones": puntuaciones,
        }

resultado = st.session_state.ultimo_resultado
if resultado is not None:
    st.divider()
    st.markdown("### 📊 Resultado del análisis")

    etiqueta = resultado["prediccion"]
    puntuaciones = resultado["puntuaciones"]
    if etiqueta == "positivo":
        st.success("😊 El modelo clasifica esta reseña como POSITIVA")
    else:
        st.error("😞 El modelo clasifica esta reseña como NEGATIVA")

    st.write("**Puntuaciones estimadas por el modelo:**")
    st.progress(puntuaciones["positivo"], text=f"😊 Positivo: {puntuaciones['positivo']:.1%}")
    st.progress(puntuaciones["negativo"], text=f"😞 Negativo: {puntuaciones['negativo']:.1%}")

    st.caption(
        "Estas puntuaciones reflejan las estimaciones del clasificador, "
        "no una certeza sobre la opinión ni una probabilidad necesariamente calibrada."
    )
    st.info(
        "¿Por qué ha elegido esta etiqueta? El modelo compara patrones de palabras "
        "aprendidos durante el entrenamiento. Puede equivocarse con ironías, "
        "negaciones y opiniones mixtas."
    )

    if "historial" not in st.session_state:
        st.session_state.historial = []
    # Solo añadimos al historial cuando se envía un análisis nuevo.
    if enviar and texto.strip():
        st.session_state.historial.append(
            {
                "Reseña": resultado["texto"],
                "Predicción": etiqueta,
                "Puntuación positiva": round(puntuaciones["positivo"], 3),
                "Puntuación negativa": round(puntuaciones["negativo"], 3),
            }
        )

if st.session_state.get("historial"):
    st.divider()
    st.markdown("### 📝 Historial de esta sesión")
    st.write("Las reseñas anteriores se mantienen mientras dura la sesión activa.")
    tabla_historial = pd.DataFrame(st.session_state.historial)
    st.dataframe(tabla_historial, hide_index=True, use_container_width=True)

    csv = tabla_historial.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "⬇️ Descargar historial CSV",
        data=csv,
        file_name="mood_insights_resultados.csv",
        mime="text/csv",
    )
    if st.button("🗑️ Borrar historial"):
        st.session_state.historial = []
        st.session_state.ultimo_resultado = None
        st.rerun()

st.divider()
st.caption(
    "Proyecto educativo · Dataset IMDb en español (Kaggle: luisdiegofv97) "
    "· Clasificación binaria de reseñas de cine."
)
