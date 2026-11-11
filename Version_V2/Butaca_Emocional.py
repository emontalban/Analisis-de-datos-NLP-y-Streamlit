"""Butaca Emocional · Análisis de reseñas cinematográficas.

Ejecutar: python -m streamlit run app.py
Los gráficos se basan en metricas_v2.json exportado por el Colab V2.
"""
from pathlib import Path
import json
import warnings

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sklearn
import streamlit as st

CARPETA = Path(__file__).resolve().parent
RUTA_MODELO = CARPETA / "butaca_emocional_modelo_v2.joblib"
RUTA_METRICAS = CARPETA / "metricas_v2.json"
# Paleta consistente: cabecera granate y sentimientos verde/rosa.
TITULO = "#65263E"
TEXTO = "#241B24"
POSITIVAS = "#20C997"
NEGATIVAS = "#FF6B81"
FONDO = "#FFF9F1"
# Colores secundarios centralizados.
TEXTO_GENERAL = "#302333"
FONDO_GRADIENTE_1 = "#fffaf3"
FONDO_GRADIENTE_2 = "#f8eee3"
FONDO_CLARO = "#fffdf8"
FONDO_LATERAL = "#f5eadf"
FONDO_TARJETA = "#fffdf9"
BORDE_TARJETA = "#d8bda4"
TEXTO_METRICA = "#51394a"
TEXTO_PESTANA = "#523747"
TITULO_HOVER = "#4c1a2e"
FONDO_CAMPO = "#fffefa"
TEXTO_CAMPO = "#2b2330"
BORDE_CAMPO = "#ae8d97"
TEXTO_PLACEHOLDER = "#766977"
BORDE_AVISO = "#caa6b5"
FONDO_AVISO = "#f7ecf0"
TEXTO_NOTA = "#30202a"
BORDE_CABECERA = "#d7b894"
FONDO_CABECERA = "#f2e0d3"
TEXTO_CEJA = "#804b28"
TEXTO_SUBTITULO = "#493543"
BLANCO = "#FFFFFF"
BORDE_GRAFICO = "#54303f"

variables_css = "\n".join([":root {"] + [
    f"  --titulo: {TITULO};",
    f"  --texto: {TEXTO};",
    f"  --positivas: {POSITIVAS};",
    f"  --negativas: {NEGATIVAS};",
    f"  --fondo: {FONDO};",
    f"  --texto-general: {TEXTO_GENERAL};",
    f"  --fondo-gradiente-1: {FONDO_GRADIENTE_1};",
    f"  --fondo-gradiente-2: {FONDO_GRADIENTE_2};",
    f"  --fondo-claro: {FONDO_CLARO};",
    f"  --fondo-lateral: {FONDO_LATERAL};",
    f"  --fondo-tarjeta: {FONDO_TARJETA};",
    f"  --borde-tarjeta: {BORDE_TARJETA};",
    f"  --texto-metrica: {TEXTO_METRICA};",
    f"  --texto-pestana: {TEXTO_PESTANA};",
    f"  --titulo-hover: {TITULO_HOVER};",
    f"  --fondo-campo: {FONDO_CAMPO};",
    f"  --texto-campo: {TEXTO_CAMPO};",
    f"  --borde-campo: {BORDE_CAMPO};",
    f"  --texto-placeholder: {TEXTO_PLACEHOLDER};",
    f"  --borde-aviso: {BORDE_AVISO};",
    f"  --fondo-aviso: {FONDO_AVISO};",
    f"  --texto-nota: {TEXTO_NOTA};",
    f"  --borde-cabecera: {BORDE_CABECERA};",
    f"  --fondo-cabecera: {FONDO_CABECERA};",
    f"  --texto-ceja: {TEXTO_CEJA};",
    f"  --texto-subtitulo: {TEXTO_SUBTITULO};",
    f"  --blanco: {BLANCO};",
    f"  --borde-grafico: {BORDE_GRAFICO};",
] + ["}"])


st.set_page_config(page_title="Butaca Emocional | Cine y sentimientos", page_icon="💺", layout="wide")

# Diseño claro de inspiración cinematográfica, con texto grande y contrastado.
css_estilos = """
<style>
/* VARIABLES_CSS */
/* Fondo cálido; texto oscuro para facilitar la lectura. */
.stApp {
  background:
    radial-gradient(ellipse 42% 28% at 0% 0%, rgba(232,191,130,.25), transparent 90%),
    radial-gradient(ellipse 38% 26% at 100% 0%, rgba(151,78,97,.10), transparent 90%),
    linear-gradient(145deg, var(--fondo-gradiente-1) 0%, var(--fondo-gradiente-2) 55%, var(--fondo-claro) 100%);
  color: var(--texto-general);
}
[data-testid="stHeader"] {background:transparent;}
[data-testid="stSidebar"] {background:var(--fondo-lateral);}
/* Estilo general y tamaños mínimos para los textos habituales. */
.stApp p, .stApp li, .stApp label,
[data-testid="stMarkdownContainer"] p {color:var(--texto-general); font-size:1.15rem; line-height:1.6;}
.stApp h1,.stApp h2,.stApp h3 {
  font-family:Georgia,serif !important;
  color:var(--titulo) !important;
  letter-spacing:.01em;
}
.stApp h2 {font-size:2.05rem !important;}
.stApp h3 {font-size:1.65rem !important;}
/* Métricas en tarjetas claras. */
[data-testid="stMetric"] {
  padding:20px 18px; background:var(--fondo-tarjeta);
  border:1px solid var(--borde-tarjeta); border-radius:16px;
  box-shadow:0 3px 14px rgba(65,37,43,.06);
}
[data-testid="stMetricLabel"] p {color:var(--texto-metrica) !important;font-size:1.05rem !important;}
[data-testid="stMetricValue"] {color:var(--titulo) !important;font-size:2rem !important;}
/* Pestañas y botones. */
[data-testid="stTabs"] button {font-size:1.15rem !important;color:var(--texto-pestana) !important;}
[data-testid="stTabs"] button[aria-selected="true"] {
  color:var(--titulo) !important;border-bottom-color:var(--titulo) !important;font-weight:750;
}
.stButton button[kind="primary"] {
  background:var(--titulo) !important;color:var(--blanco) !important;border:0;
  font-size:1.18rem;font-weight:750;padding:.7rem 1.4rem;
}
.stButton button[kind="primary"]:hover {background:var(--titulo-hover) !important;color:var(--blanco) !important;}
/* Campo de opinión: no utilizar texto rojo sobre morado. */
[data-testid="stTextArea"] textarea {
  background:var(--fondo-campo) !important;color:var(--texto-campo) !important;
  border:2px solid var(--borde-campo);border-radius:12px;font-size:1.18rem !important;
}
[data-testid="stTextArea"] textarea::placeholder {color:var(--texto-placeholder) !important;opacity:1;}
/* Mensajes informativos y de resultados: sin fondos azul o amarillo de Streamlit. */
[data-testid="stAlert"] {
  border-radius:12px !important;
  border:1px solid var(--borde-aviso) !important;
  background:var(--fondo-aviso) !important;
  color:var(--titulo) !important;
}
[data-testid="stAlert"] svg {color:var(--titulo) !important;fill:none;}
/* Streamlit puede colorear por separado el contenedor interior de los avisos. */
[data-testid="stAlert"] > div {background:transparent !important;}
/* Garantiza texto blanco incluso en los elementos interiores del botón primario. */
.stApp .stButton button[kind="primary"],
.stApp .stButton button[kind="primary"] *,
.stApp .stButton button[data-testid="stBaseButton-primary"],
.stApp .stButton button[data-testid="stBaseButton-primary"] * {
  color:var(--blanco) !important;
}
.stApp .stButton button[kind="primary"]:hover *,
.stApp .stButton button[data-testid="stBaseButton-primary"]:hover * {
  color:var(--blanco) !important;
}
[data-testid="stAlert"] p,
[data-testid="stAlert"] div[data-testid="stMarkdownContainer"] p {
  color:var(--titulo) !important; font-size:1.16rem !important; font-weight:650;
}
/* Notas bajo los gráficos y pie de página: contraste alto. */
[data-testid="stCaptionContainer"] p,
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] * {
  font-size:1.08rem !important; color:var(--texto-nota) !important; line-height:1.55;
}
[data-testid="stSlider"] {color:var(--texto-general);}
/* Cabecera de gala clara, sin perder el carácter cinematográfico. */
.gala-hero {
  border:2px solid var(--borde-cabecera);border-radius:24px;
  background:linear-gradient(125deg,var(--fondo-claro),var(--fondo-cabecera));
  padding:32px 28px;margin:8px 0 26px;text-align:center;
  box-shadow:0 10px 26px rgba(87,38,61,.09);
}
.eyebrow {color:var(--texto-ceja);letter-spacing:3px;font-size:1rem;font-weight:800;}
.gala-hero h1 {font-size:clamp(2.4rem,5vw,4rem) !important;margin:12px 0;color:var(--titulo) !important;}
.hero-sub {color:var(--texto-subtitulo);font-size:1.25rem;line-height:1.5;}
/* Separadores y textos de widgets. */
[data-testid="stWidgetLabel"] p {font-size:1.16rem !important;font-weight:650;}
</style>
"""
st.markdown(css_estilos.replace("/* VARIABLES_CSS */", variables_css), unsafe_allow_html=True)

st.markdown("""<div class="gala-hero"><div class="eyebrow">✦ LAS EMOCIONES DEL CINE ✦</div>
<h1>💺 Butaca Emocional</h1><div class="hero-sub">Tu crítica de cine, interpretada por inteligencia artificial</div></div>""", unsafe_allow_html=True)

# Los archivos tienen que permanecer junto a app.py.
if not RUTA_MODELO.is_file() or not RUTA_METRICAS.is_file():
    st.error("Faltan los archivos de la versión 2. Coloca butaca_emocional_modelo_v2.joblib y metricas_v2.json junto a app.py.")
    st.stop()

@st.cache_data
# El JSON contiene resultados de la evaluación en Colab.
def leer_metricas():
    with RUTA_METRICAS.open(encoding="utf-8") as archivo:
        return json.load(archivo)

@st.cache_resource
# Joblib solamente debe abrirse si el modelo procede de una fuente de confianza.
def leer_modelo():
    with warnings.catch_warnings():
        # La aplicación advierte de las diferencias entre versiones más abajo.
        warnings.simplefilter("ignore", category=sklearn.exceptions.InconsistentVersionWarning)
        return joblib.load(RUTA_MODELO)

try:
    metricas = leer_metricas()
except (ValueError, OSError, KeyError) as error:
    st.error(f"No se pueden leer las métricas: {error}")
    st.stop()


try:
    modelo = leer_modelo()
except Exception as error:
    st.error("No se pudo cargar el archivo .joblib. Puede existir una incompatibilidad de versiones.")
    st.code(str(error))
    st.stop()

# Formato común para todos los gráficos; los valores provienen del JSON.
def estilo_figura(figura, altura=385):
    figura.update_layout(
        height=altura, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXTO, size=18, family="Arial"),
        margin=dict(l=32, r=30, t=65, b=48),
        xaxis=dict(showgrid=True, gridcolor="rgba(59,36,48,.22)", zeroline=False,
                   tickfont=dict(color=TEXTO, size=16), title_font=dict(color=TEXTO, size=17)),
        yaxis=dict(showgrid=False, tickfont=dict(color=TEXTO, size=16),
                   title_font=dict(color=TEXTO, size=17)),
        showlegend=False,
        legend=dict(font=dict(color=TEXTO, size=16)),
        hoverlabel=dict(font_size=16),
    )
    return figura

pestana_opinion, pestana_palabras, pestana_evaluacion = st.tabs([
    "🎟️ Analiza una película", "🧠 Qué ha aprendido", "📊 Resultados del modelo"
])

with pestana_opinion:
    st.subheader("Tu opinión merece una alfombra roja")
    st.write("Escribe una reseña y el modelo estimará si transmite un sentimiento positivo o negativo.")
    opinion = st.text_area(
        "¿Qué te ha parecido la película?",
        placeholder="Ejemplo: Una historia emocionante, personajes inolvidables y un final magnífico.",
        height=125,
    )
    if st.button("✨ Analizar mi reseña", type="primary"):
        texto = opinion.strip()
        if not texto:
            st.warning("Primero escribe una opinión.")
        else:
            try:
                prediccion = str(modelo.predict([texto])[0])
                probabilidades = modelo.predict_proba([texto])[0]
                clases = list(modelo.classes_)
                if prediccion == "positivo":
                    st.success("🌟 El modelo interpreta tu reseña como POSITIVA")
                else:
                    st.error("🎭 El modelo interpreta tu reseña como NEGATIVA")
                figura = go.Figure(go.Bar(
                    x=[float(probabilidades[clases.index("negativo")]) * 100,
                       float(probabilidades[clases.index("positivo")]) * 100],
                    y=["Negativo", "Positivo"], orientation="h",
                    marker_color=[NEGATIVAS, POSITIVAS], texttemplate="%{x:.1f}%", textposition="inside",
                    textfont=dict(color=TEXTO, size=17),
                    hovertemplate="%{y}: %{x:.1f}%<extra></extra>",
                ))
                figura.update_xaxes(range=[0, 100], title="Probabilidad estimada (%)")
                st.plotly_chart(estilo_figura(figura, 245), use_container_width=True)
                st.caption("Estas son probabilidades estimadas por el modelo, no garantías de acierto. La aplicación no clasifica opiniones neutras.")
            except Exception as error:
                st.error("No se pudo realizar la predicción.")
                st.code(str(error))
    st.info("El programa ha aprendido de reseñas de películas en español. Algunas frases irónicas, ambiguas o con negaciones pueden clasificarse incorrectamente.")

with pestana_palabras:
    st.subheader("¿Qué palabras inclinan la balanza?")
    st.write("Durante el entrenamiento, el clasificador aprendió **pesos** para palabras y parejas de palabras. Un peso más alto indica una asociación mayor con un sentimiento, **no** más repeticiones.")
    cantidad = st.slider("¿Cuántos términos mostramos por sentimiento?", min_value=5, max_value=12, value=10)
    izquierda, derecha = st.columns(2)
    for columna, clave, titulo, color in [
        (izquierda, "terminos_positivos", "🌟 Asociados a positivo", POSITIVAS),
        (derecha, "terminos_negativos", "🎭 Asociados a negativo", NEGATIVAS),
    ]:
        with columna:
            st.markdown(f"**{titulo}**")
            tabla = pd.DataFrame(metricas[clave]).head(cantidad).copy()
            tabla["magnitud"] = tabla["peso"].abs()
            tabla = tabla.sort_values("magnitud", ascending=True)
            figura = px.bar(tabla, x="magnitud", y="termino", orientation="h", color_discrete_sequence=[color],
                            custom_data=["peso"])
            figura.update_traces(hovertemplate="%{y}<br>Peso del modelo: %{customdata[0]:.3f}<extra></extra>")
            figura.update_layout(xaxis_title="Magnitud del peso", yaxis_title="")
            st.plotly_chart(estilo_figura(figura, 430), use_container_width=True)
    st.caption("Estos términos provienen directamente de metricas_v2.json. Una expresión como «un poco» puede estar asociada estadísticamente con opiniones positivas en estos datos; eso no la convierte en positiva en cualquier frase.")

with pestana_evaluacion:
    st.subheader("La noche de los resultados")
    ensayos = int(metricas["n_prueba"])
    matriz = metricas["matriz_confusion"]
    aciertos = int(matriz[0][0] + matriz[1][1])
    errores = ensayos - aciertos
    a,b,c,d = st.columns(4)
    a.metric("Exactitud", f"{metricas['exactitud']:.2%}")
    b.metric("Reseñas de prueba", f"{ensayos:,}".replace(",", "."))
    c.metric("Aciertos", f"{aciertos:,}".replace(",", "."))
    d.metric("Errores", f"{errores:,}".replace(",", "."))
    st.caption("La exactitud mide el porcentaje de reseñas clasificadas correctamente en el conjunto de prueba, no el rendimiento garantizado con cualquier comentario nuevo.")

    primera, segunda = st.columns([1.08, 1])
    with primera:
        st.markdown("**Matriz de confusión — aciertos y errores**")
        fig = go.Figure(go.Heatmap(
            # Verde: acierto (diagonal). Rosa: error (resto).
            # Los recuentos reales se conservan en text/customdata.
            z=[[1, 0], [0, 1]],
            customdata=matriz,
            x=["Predijo negativo", "Predijo positivo"],
            y=["Real negativo", "Real positivo"],
            text=matriz, texttemplate="%{text:,}",
            zmin=0, zmax=1,
            colorscale=[[0,NEGATIVAS],[0.4999,NEGATIVAS],
                        [0.5,POSITIVAS],[1,POSITIVAS]],
            textfont=dict(color=TEXTO, size=22),
            xgap=5, ygap=5,
            showscale=False,
            hovertemplate="%{y}<br>%{x}<br>%{customdata:,} reseñas<extra></extra>"
        ))
        fig.update_yaxes(autorange="reversed")
        fig = estilo_figura(fig, 385)
        # Recuadro visible y separación entre casillas para diferenciarlo del fondo beige.
        fig.update_layout(
            plot_bgcolor=TITULO,
            paper_bgcolor=FONDO_TARJETA,
            shapes=[dict(type="rect", xref="paper", yref="paper",
                         x0=0, y0=0, x1=1, y1=1,
                         line=dict(color=TITULO, width=2), fillcolor="rgba(0,0,0,0)")],
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Las casillas verdes de la diagonal representan los aciertos. Las rosas muestran los errores. Los números indican cuántas reseñas hay en cada caso.")
    with segunda:
        st.markdown("**¿Cuántas reseñas acertó y falló?**")
        fig = go.Figure(go.Pie(
            labels=["Aciertos", "Errores"], values=[aciertos, errores],
            hole=.66, marker=dict(colors=[POSITIVAS, NEGATIVAS],
                                      line=dict(color=BLANCO, width=3)),
            textinfo="percent+label", textposition="outside",
            textfont=dict(color=TEXTO, size=18),
            hovertemplate="%{label}: %{value:,} reseñas<extra></extra>"
        ))
        st.plotly_chart(estilo_figura(fig, 385), use_container_width=True)

    st.markdown("**Evaluación por sentimiento**")
    st.write("**Precisión:** de las reseñas que el modelo llama positivas o negativas, ¿cuántas lo son de verdad? **Recall (sensibilidad):** de las reseñas que realmente pertenecen a esa clase, ¿cuántas identifica?")
    registros = []
    for etiqueta in ["negativo", "positivo"]:
        registros.extend([
            {"Sentimiento": etiqueta.capitalize(), "Métrica": "Precisión", "Valor": 100 * metricas["precision_por_clase"][etiqueta]},
            {"Sentimiento": etiqueta.capitalize(), "Métrica": "Recall", "Valor": 100 * metricas["recall_por_clase"][etiqueta]},
        ])
    datos = pd.DataFrame(registros)
    # El color representa el sentimiento; el patrón distingue Precisión de Recall.
    # Así evitamos asociar el verde a una métrica y el rosa a otra.
    fig = go.Figure()
    for metrica, patron in [("Precisión", ""), ("Recall", "/")]:
        valores = [float(datos.loc[(datos["Sentimiento"] == sentimiento) &
                                  (datos["Métrica"] == metrica), "Valor"].iloc[0])
                   for sentimiento in ["Negativo", "Positivo"]]
        fig.add_trace(go.Bar(
            name=metrica, x=["Negativo", "Positivo"], y=valores,
            marker=dict(color=[NEGATIVAS, POSITIVAS],
                        pattern=dict(shape=patron, fgcolor=BORDE_GRAFICO, size=8, solidity=0.18),
                        line=dict(color=BORDE_GRAFICO, width=1)),
            text=[f"{valor:.1f}%" for valor in valores],
            textposition="outside", textfont=dict(color=TEXTO, size=17),
            hovertemplate="%{x}<br>" + metrica + ": %{y:.1f}%<extra></extra>",
        ))
    fig = estilo_figura(fig, 385)
    fig.update_layout(barmode="group", yaxis_title="Porcentaje (%)",
                      yaxis_range=[0, 112], showlegend=True,
                      legend=dict(orientation="h", y=1.18, x=0,
                                  font=dict(color=TEXTO, size=17)))
    st.plotly_chart(fig, use_container_width=True)
    st.info("Se entrenó con 39.679 reseñas y se evaluó con otras 9.920. El vocabulario contiene 40.000 términos. La evaluación utiliza exclusivamente las cifras exportadas del Colab, no resultados simulados.")

st.divider()
st.caption("💺 Butaca Emocional · Versión 2 · Proyecto didáctico de NLP y análisis de sentimientos en reseñas de cine.")
