# 🎬 MOOD INSIGHTS — Analizador de sentimientos con Streamlit

**Proyecto final de análisis de datos, NLP, Machine Learning y Streamlit.**  
**Idioma de las reseñas:** español.  
**Resultado posible:** `positivo` o `negativo`.

## 1. ¿Qué hemos construido?

Una aplicación que recibe una reseña de una película y devuelve una clasificación estimada: **positiva** o **negativa**. El objetivo es aprender las fases de un proyecto de datos completo:

**Problema → Datos → Análisis exploratorio (EDA) → NLP → Modelo de Machine Learning → Aplicación → Resultados**.

No hemos programado una regla como «si aparece *bueno*, responde positivo». El modelo ha aprendido asociaciones entre palabras y etiquetas a partir de miles de reseñas. Esto **no implica que comprenda el lenguaje como una persona**: puede equivocarse.

## 2. ¿Qué hicimos cada día?

### Día 1 — Análisis exploratorio (EDA)

Archivo: `notebooks/MOOD_INSIGHTS_EDA.ipynb`.

- **Cargar datos:** leer el dataset y conocer filas y columnas.
- **Explorar:** revisar primeras reseñas, tipos de datos, valores ausentes y duplicados.
- **Preparar el texto:** pasar a minúsculas y retirar algunas etiquetas HTML y signos para los gráficos; conservar una versión original.
- **Visualizar:** distribución de reseñas positivas/negativas, longitud de las reseñas y palabras características de cada sentimiento.
- **Interpretar:** los gráficos muestran cómo son los datos. Por sí solos NO predicen el sentimiento de una nueva reseña.

### Día 2 — Procesamiento del lenguaje natural (NLP) y aprendizaje automático

Archivo: `notebooks/MOOD_INSIGHTS_NLP.ipynb`.

1. Volvimos a cargar el dataset y revisamos valores faltantes, duplicados y posibles etiquetas contradictorias.
2. Creamos `X` (textos) e `y` (etiquetas conocidas).
3. Usamos `train_test_split()` para separar **80 % de entrenamiento** y **20 % de prueba**.
4. `CountVectorizer` convirtió los textos en números, contando palabras.
5. `LogisticRegression` aprendió relaciones estadísticas entre esas palabras y las etiquetas.
6. Un `Pipeline` unió vectorizador + clasificador. Así el vocabulario se aprende solo con el conjunto de entrenamiento.
7. Comprobamos el rendimiento con predicciones, exactitud y otras métricas; también observamos errores.
8. Guardamos el **Pipeline completo** con `joblib.dump()` en `mood_insights_modelo.joblib`.

**Importante:** los resultados numéricos del entrenamiento están en el notebook. No fijamos aquí una exactitud que pudiera variar al volver a entrenar. El modelo incluido fue entrenado previamente; la aplicación no lo vuelve a entrenar.

### Día 3 — La aplicación web

Archivo: `app.py`.

- Streamlit crea el cuadro de texto, los botones y los resultados visibles.
- `joblib.load()` abre el **modelo entrenado**.
- `modelo.predict([texto])` devuelve una etiqueta (`positivo` / `negativo`).
- `modelo.predict_proba([texto])` devuelve puntuaciones para ambas clases.
- El historial permite comparar varias reseñas dentro de la sesión y descargarlo como CSV.

## 3. Estructura de carpetas

```text
MOOD_INSIGHTS_STREAMLIT/
│
├── app.py                         # Aplicación visual de Streamlit
├── requirements.txt               # Librerías necesarias para la aplicación
├── README.md                      # Esta guía
├── .gitignore                     # Archivos que Git debe ignorar
│
├── modelos/
│   └── mood_insights_modelo.joblib # Pipeline entrenado (CountVectorizer + LogisticRegression)
│
└── notebooks/
    ├── MOOD_INSIGHTS_EDA.ipynb    # Día 1: exploración y gráficos
    └── MOOD_INSIGHTS_NLP.ipynb    # Día 2: preparación, entrenamiento y evaluación
```

**Atención:** la carpeta `modelos` y su `.joblib` son imprescindibles. Sin ese archivo la aplicación no puede realizar predicciones. Para **ejecutar la app** no es necesario descargar otra vez el dataset de Kaggle: solo hace falta para **reproducir los notebooks y volver a entrenar**.

## 4. Paso 1 — Descargar y descomprimir el proyecto

1. Descarga el ZIP del proyecto.
2. Haz clic derecho y **Extraer todo**.
3. Comprueba que dentro está la carpeta `MOOD_INSIGHTS_STREAMLIT` con `app.py`, `requirements.txt`, `modelos` y `notebooks`.
4. No cambies de carpeta el archivo `mood_insights_modelo.joblib`: `app.py` busca el modelo dentro de `modelos/`.

## 5. Paso 2 — Abrir la carpeta con Visual Studio Code

1. Abre **Visual Studio Code**.
2. Selecciona **Archivo → Abrir carpeta**.
3. Escoge la carpeta `MOOD_INSIGHTS_STREAMLIT`.
4. Abre el terminal integrado: **Terminal → Nuevo terminal**.
5. Comprueba que el terminal está situado en la carpeta del proyecto (donde está `app.py`).

> Si al abrir el terminal ves una ruta distinta, entra en la carpeta del proyecto antes de ejecutar los comandos. No escribas los símbolos `PS C:\...>` de los ejemplos de PowerShell: son solo la línea de tu terminal.

## 6. Paso 3 — Comprobar Python

Recomendación: **Python 3.11 o 3.12** por compatibilidad con el modelo guardado en scikit-learn 1.6.1.

En el terminal de VS Code, escribe:

```powershell
python --version
```

**¿Qué hace?** Pregunta qué versión de Python está instalada. Si aparece un error, instala Python y reinicia VS Code. Si tu ordenador utiliza el lanzador de Windows, puedes consultar `py --version`.

## 7. Paso 4 — Crear el entorno virtual

Con el terminal situado dentro del proyecto:

```powershell
python -m venv .venv
```

**¿Qué significa cada parte?**

- `python`: ejecutamos Python.
- `-m venv`: pedimos que utilice el módulo que crea entornos virtuales.
- `.venv`: nombre de la nueva carpeta con el entorno.

**¿Por qué?** Porque instalaremos las librerías solo para este proyecto sin mezclarlas con otras instalaciones de Python.

## 8. Paso 5 — Activar el entorno virtual

### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando se active, el terminal suele mostrar `(.venv)` al principio de la línea.

**Si PowerShell indica «la ejecución de scripts está deshabilitada»:**

Opción sencilla (sin cambiar la política): abre un terminal **Símbolo del sistema (CMD)** en VS Code y escribe:

```cmd
.venv\Scripts\activate.bat
```

Alternativa para PowerShell, solo si comprendes el cambio y tu política de seguridad lo permite, limita el permiso al proceso actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Este ajuste temporal afecta solamente a esa sesión de PowerShell; no es necesario hacerlo si utilizas CMD.

### macOS o Linux

```bash
source .venv/bin/activate
```

## 9. Paso 6 — Instalar las librerías

Con `(.venv)` activo, ejecuta:

instalamos las librerias

```powershell
python -m pip install streamlit pandas scikit-learn joblib matplotlib
```

**¿Qué hace?** Lee `requirements.txt` e instala las librerías indicadas. `python -m pip` ejecuta el instalador asociado al Python activo; suele ser más fiable que usar `pip` solo cuando hay varias instalaciones de Python.

| Librería | Para qué la utilizamos |
|---|---|
| `streamlit` | Diseña la aplicación web con Python. |
| `scikit-learn` | Contiene el vectorizador, el clasificador y el Pipeline entrenado. |
| `joblib` | Abre el modelo guardado. |
| `pandas` | Muestra y exporta el historial de resultados. |

**Compatibilidad:** el archivo de modelo suministrado se guardó con **scikit-learn 1.6.1**. Por ello `requirements.txt` fija esa versión, para evitar cargarlo con una distinta. No sustituyas esta versión por otra sin comprobar que funciona o volver a generar el modelo.

## 10. Paso 7 — Ejecutar la aplicación

En el mismo terminal, dentro de la carpeta del proyecto:

```powershell
python -m streamlit run app.py
```

**¿Qué sucede?** Streamlit inicia un pequeño servidor local, muestra una dirección parecida a `http://localhost:8501` y suele abrir automáticamente el navegador. Si no se abre, copia en el navegador la URL local que aparezca en el terminal.

**No ejecutes `python app.py`** para abrir esta interfaz: las apps de Streamlit se lanzan con `streamlit run` o `python -m streamlit run`.

## 11. Paso 8 — Probar la aplicación

1. Escribe: **«Me encantó la película, es preciosa y emocionante»**.
2. Pulsa **🔎 Analizar reseña**.
3. Observa la categoría predicha y las dos puntuaciones.
4. Cambia el texto por: **«Qué película tan aburrida, no la recomiendo»** y vuelve a analizar.
5. Prueba una opinión mixta, por ejemplo: **«La fotografía es preciosa, pero la historia es muy aburrida»**.
6. Consulta el **historial**, descarga el CSV si quieres guardarlo y utiliza el botón de borrado si deseas empezar de nuevo.

**Importante:** los ejemplos no garantizan una predicción concreta. El modelo decide basándose en las asociaciones aprendidas y puede fallar, especialmente con ironía, negaciones y mensajes mixtos.

## 12. ¿Qué ocurre cuando pulsamos «Analizar reseña»?

```text
1. Escribimos una reseña
          ↓
2. Streamlit recoge el texto
          ↓
3. Pipeline: CountVectorizer transforma palabras en números
          ↓
4. Pipeline: LogisticRegression calcula una predicción
          ↓
5. La aplicación muestra «positivo» o «negativo»
          ↓
6. Guarda ese resultado en el historial de la sesión
```

**Detalle de Python importante:** `modelo.predict([texto])` lleva el texto entre corchetes porque espera una **lista de textos**, aunque solo queramos analizar uno. Y `modelo.classes_` permite relacionar correctamente las puntuaciones con cada categoría, sin suponer cuál ocupa la primera columna.

## 13. Conceptos básicos usados en `app.py`

| Código | Explicación sencilla |
|---|---|
| `import streamlit as st` | Importa Streamlit y le damos el nombre corto `st`. |
| `Path(__file__).resolve().parent` | Localiza la carpeta en la que está `app.py`. |
| `st.set_page_config(...)` | Configura el título y la disposición de la página. |
| `@st.cache_resource` | Evita volver a cargar el modelo en cada interacción. |
| `joblib.load(...)` | Recupera el Pipeline que guardamos el día 2. |
| `st.title(...)` | Muestra el título principal. |
| `st.text_area(...)` | Permite escribir una reseña larga. |
| `st.form(...)` | Agrupa el cuadro de texto y el botón. |
| `st.form_submit_button(...)` | Ejecuta el análisis al pulsar el botón. |
| `modelo.predict(...)` | Estima la categoría de la reseña. |
| `modelo.predict_proba(...)` | Devuelve puntuaciones para las dos categorías. |
| `st.progress(...)` | Dibuja una barra de progreso para cada puntuación. |
| `st.session_state` | Guarda temporalmente resultados e historial durante la sesión. |
| `st.dataframe(...)` | Enseña el historial como una tabla. |
| `st.download_button(...)` | Descarga el historial en formato CSV. |

## 14. Detener la aplicación y salir del entorno

Para **detener Streamlit**, ve al terminal donde se ejecuta y pulsa:

```text
Ctrl + C
```

Para **desactivar el entorno virtual**, escribe:

```powershell
deactivate
```

La próxima vez que abras el proyecto no tienes que instalar todo de nuevo: solo abrir la carpeta, activar `.venv` y ejecutar `python -m streamlit run app.py`.

## 15. Si algo falla: errores frecuentes

| Problema | Posible causa y solución |
|---|---|
| `No module named streamlit` | No se instalaron los requisitos en el Python activo. Activa `.venv` y repite `python -m pip install -r requirements.txt`. |
| `FileNotFoundError` relacionado con el modelo | Comprueba que existe `modelos/mood_insights_modelo.joblib`. |
| PowerShell bloquea `Activate.ps1` | Usa CMD con `activate.bat` o la alternativa temporal de PowerShell indicada arriba. |
| `streamlit` no se reconoce | Usa `python -m streamlit run app.py` en lugar de `streamlit run app.py`. |
| Incompatibilidad de versión de scikit-learn | Usa el entorno indicado y `scikit-learn==1.6.1` tal como aparece en los requisitos. |
| `Port 8501 is already in use` | Cierra la otra aplicación Streamlit o ejecuta `python -m streamlit run app.py --server.port 8502`. |
| La predicción parece equivocada | Es una clasificación estadística, no una respuesta garantizada. Comprueba varios ejemplos y recuerda que hay limitaciones de vocabulario y contexto. |

## 16. ¿Y si quiero repetir el entrenamiento desde cero?

La aplicación **no necesita** que entrenes otra vez. Si quieres reproducir los días 1 y 2, abre los notebooks de `notebooks/` en Colab o Jupyter, ejecuta sus celdas en orden y descarga el dataset que utilizan:

**Kaggle:** [IMDb Dataset of 50K Movie Reviews (Spanish)](https://www.kaggle.com/datasets/luisdiegofv97/imdb-dataset-of-50k-movie-reviews-spanish).

El notebook de NLP utiliza `kagglehub.dataset_download("luisdiegofv97/imdb-dataset-of-50k-movie-reviews-spanish")`. Sus dependencias de análisis son adicionales a las de esta app: por ejemplo, `kagglehub` y `matplotlib`. Para reproducir también los gráficos del EDA puede hacer falta `seaborn` y `numpy`. En los notebooks se indican las instalaciones correspondientes.

Cuando generes un modelo nuevo desde el notebook de NLP, **coloca el archivo resultante dentro de `modelos/` con el nombre `mood_insights_modelo.joblib`**. Reinicia la app de Streamlit para que cargue la versión nueva.

## 17. Subir el proyecto a GitHub

1. Crea un repositorio nuevo en GitHub, por ejemplo `mood-insights-streamlit`.
2. Abre el terminal de VS Code desde la carpeta del proyecto.
3. Ejecuta `git init`, `git add .` y `git commit -m "Proyecto Mood Insights completo"`.
4. En GitHub, copia los comandos para enlazar tu repositorio y enviar la rama. Si la rama principal se llama `main`, normalmente serán `git branch -M main`, `git remote add origin URL_DEL_REPOSITORIO` y `git push -u origin main`.

No subas `.venv`: ya está excluida por `.gitignore`. El modelo `.joblib` **sí forma parte del proyecto**, pues es necesario para predecir, pero nunca cargues modelos desconocidos por razones de seguridad.

## 18. Conclusión del proyecto

Con Mood Insights hemos conectado todo el proceso: primero **estudiamos los datos**, después **enseñamos al clasificador con ejemplos**, finalmente **lo integramos en una aplicación real** que cualquier persona puede probar.

**Limitaciones:** clasificación binaria, dominio de reseñas de cine, posibles errores ante ironías o textos ambiguos, y puntuaciones que no deben interpretarse como certezas ni como medida del estado emocional humano. Una mejora futura sería evaluar textos de otros ámbitos con datos apropiados y, si se necesita la categoría neutra, reunir ejemplos etiquetados de esa clase y volver a entrenar/evaluar.

---

**Proyecto educativo · Dataset de reseñas IMDb en español, publicado en Kaggle por `luisdiegofv97`.**
