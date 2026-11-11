# 🎬 Butaca Emocional — Análisis de sentimientos con Python y Streamlit

**Proyecto final de análisis de datos, procesamiento del lenguaje natural (NLP), Machine Learning y desarrollo de aplicaciones con Streamlit.**

- **Idioma:** español.
- **Clasificación:** sentimiento `positivo` o `negativo`.
- **Entorno de trabajo principal:** Visual Studio Code, con notebooks Jupyter (`.ipynb`).
- **Datos:** reseñas de películas del dataset IMDb en español publicado en Kaggle.

## 1. ¿Qué hemos construido?

**Butaca Emocional** es una aplicación que recibe una reseña de una película y estima si expresa un sentimiento **positivo** o **negativo**.

El repositorio documenta todo el proceso de construcción, no solo la aplicación final, y contiene una segunda versión independiente dentro de `version_V2/`:

**Problema → Datos → Análisis exploratorio (EDA) → CSV limpio → NLP → Modelo de Machine Learning → Streamlit → Resultados.**

El clasificador no aplica reglas escritas a mano, como «si aparece *bueno*, el sentimiento es positivo». Aprende asociaciones estadísticas entre las palabras de miles de reseñas y sus etiquetas. Eso no significa que comprenda el lenguaje como una persona: puede equivocarse.

## 2. Fases del proyecto

### Día 1 — Exploración, limpieza y visualización (EDA)

**Notebook:** `notebook/MOOD_INSIGHTS_EDA.ipynb` 

1. Descargamos el dataset original desde Kaggle con `kagglehub`.
2. Exploramos su estructura: columnas, tipos, valores ausentes y duplicados.
3. Limpiamos y normalizamos las reseñas, conservando una versión original para consultar.
4. Visualizamos la distribución de sentimientos, longitudes de las reseñas y palabras características.
5. Preparamos un dataset para el modelo, con las columnas `reseña` y `sentimiento`.
6. Exportamos el dataset limpio como `mood_insights_limpio.csv.gz`, utilizando compresión GZIP para reducir su tamaño de aproximadamente 67 MB a 25 MB. Descargamos el archivo generado desde Google Colab y lo guardamos en la carpeta `data/` del repositorio.

La limpieza se realiza principalmente en esta fase. Después de normalizar, podemos encontrar textos coincidentes que antes no eran duplicados; también comprobamos si un mismo texto está asociado a etiquetas opuestas.

**Resultado del EDA:** un CSV limpio e independiente para entrenar el modelo, además de los gráficos y conclusiones exploratorias.

### Día 2 — NLP y aprendizaje automático

**Notebook:** `notebook/MOOD_INSIGHTS_NLP.ipynb`.

1. Abrimos el proyecto en **VS Code**.
2. Cargamos `data/mood_insights_limpio.csv.gz`, generado previamente en el EDA. Pandas permite leer el archivo comprimido directamente, sin descomprimirlo manualmente ni repetir la limpieza de los datos.
3. Verificamos que el archivo contiene las columnas y etiquetas esperadas.
4. Creamos `X` (reseñas) e `y` (sentimientos).
5. Dividimos los datos en **80 % para entrenamiento y 20 % para prueba** con `train_test_split()`.
6. `CountVectorizer` transforma los textos en características numéricas.
7. `LogisticRegression` aprende a clasificar las reseñas.
8. Un `Pipeline` une ambos pasos y asegura que el vocabulario se aprenda solo con los datos de entrenamiento.
9. Evaluamos predicciones, exactitud, errores y otras métricas.
10. Guardamos el Pipeline entrenado como archivo `.joblib` y conservamos las métricas generadas por NLP en la carpeta **`modelos/`**.


### Día 3 — Aplicación web con Streamlit

**Archivo:** `app.py`.

- Streamlit presenta el cuadro de texto, los botones y los resultados.
- `joblib.load()` carga el Pipeline ya entrenado, sin volver a entrenarlo.
- `modelo.predict([texto])` predice `positivo` o `negativo`.
- `modelo.predict_proba([texto])` calcula puntuaciones asociadas a ambas categorías.
- La aplicación permite conservar un historial de reseñas analizadas durante la sesión y exportarlo a CSV.

## 3. Estructura del repositorio

La organización acordada es la siguiente. **La carpeta `data/` es una incorporación propuesta:** todavía hay que crearla y copiar allí el CSV descargado del EDA. Los nombres de los archivos de métricas pueden variar según lo exportado desde el notebook.

```text
mood-insights/
│
├── app.py                             # Aplicación de Streamlit
├── README.md                          # Documentación del repositorio
├── requirements.txt                   # Dependencias del proyecto
├── .gitignore                         # Exclusiones de Git
│
├── data/                               # Carpeta para datasets
│   └── mood_insights_limpio.csv.gz    # Dataset limpio y comprimido 
│
├── notebook/
│   ├── MOOD_INSIGHTS_EDA_ACTUALIZADO.ipynb
│   └── MOOD_INSIGHTS_NLP_VSCODE.ipynb
│
├── modelos/
│   ├── mood_insights_modelo.joblib    # Pipeline entrenado
│
└── version_V2/
    ├── Butaca_Emocional.py                # Aplicación Streamlit V2
    ├── BUTACA_EMOCIONAL_MODELO_V2.ipynb # Entrenamiento y evaluación V2
    ├── butaca_emocional_modelo_v2.joblib # Modelo entrenado V2
    ├── metricas_v2.json              # Resultados y términos para gráficos
    └── README_BUTACA_EMOCIONAL_V2.md # Documentación detallada V2
```


## 4. Clonar el repositorio de GitHub y abrirlo en VS Code


1. Abre la página del repositorio en GitHub y pulsa **Code**.
2. Selecciona **HTTPS** y copia la URL del repositorio.
3. Abre **Visual Studio Code**, selecciona **Terminal → Nuevo terminal** y sitúate en el directorio donde quieras guardar el proyecto.
4. Ejecuta el siguiente comando, sustituyendo la URL de ejemplo por la que has copiado:

```bash
git clone URL_DE_TU_REPOSITORIO
```

5. Entra en la carpeta clonada (su nombre normalmente coincide con el del repositorio):

```bash
cd NOMBRE_DE_LA_CARPETA_CLONADA
```

6. Selecciona **Archivo → Abrir carpeta** en VS Code y abre esa carpeta. Desde ella podrás ejecutar los comandos de esta guía.



## 5. Comprobar Python y crear el entorno virtual

Se recomienda utilizar una versión de Python compatible con las dependencias del proyecto. Si reutilizas un `.joblib` ya entrenado, conviene mantener la misma versión de `scikit-learn` con la que fue generado (en la documentación original se utilizó la **1.6.1**).

Comprueba la versión instalada:

```powershell
python --version
```

Crea el entorno virtual desde la raíz del proyecto:

```powershell
python -m venv .venv
```

Actívalo en **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea los scripts, puedes usar **CMD**:

```cmd
.venv\Scripts\activate.bat
```

O permitir temporalmente los scripts en esa sesión de PowerShell, si la política de tu equipo lo permite:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

En **macOS o Linux**:

```bash
source .venv/bin/activate
```

## 6. Instalar las librerías

Con el entorno virtual activado, instala las dependencias declaradas en el repositorio:

```powershell
python -m pip install -r requirements.txt
```

Este comando **sí lee** `requirements.txt` y permite reproducir las versiones incluidas en ese archivo. Para trabajar con los notebooks también puedes necesitar paquetes como `ipykernel`, `kagglehub`, `numpy`, `seaborn` y `matplotlib`, si no están ya especificados en los requisitos. Las celdas de instalación de cada notebook indican sus dependencias.

| Librería | Para qué se utiliza |
|---|---|
| `pandas` | Cargar y trabajar con los datos. |
| `scikit-learn` | Vectorización, entrenamiento y evaluación. |
| `joblib` | Guardar y cargar el modelo entrenado. |
| `streamlit` | Crear la aplicación web. |
| `matplotlib` / `seaborn` | Representar gráficos de exploración y evaluación. |
| `kagglehub` | Descargar el dataset original en el EDA. |

En VS Code, para ejecutar los `.ipynb`, selecciona el kernel asociado al entorno virtual.


## 7. Ejecutar el EDA y generar el CSV limpio

**Notebook:** `notebook/MOOD_INSIGHTS_EDA.ipynb`

En esta fase realizamos el análisis exploratorio y preparamos los datos que utilizaremos posteriormente para entrenar el modelo.

### Pasos del proceso

1. Abrimos el notebook EDA desde VS Code o Google Colab.
2. Ejecutamos las celdas en orden, comenzando por la descarga del dataset original desde Kaggle.
3. Exploramos las columnas, los tipos de datos, los valores nulos y los duplicados.
4. Analizamos la distribución de sentimientos y visualizamos los resultados.
5. Limpiamos y normalizamos las reseñas.
6. Preparamos el DataFrame `df_nlp` con las columnas `reseña` y `sentimiento`.
7. Exportamos el dataset limpio y comprimido.

### Exportación y compresión del dataset

El CSV limpio original ocupaba aproximadamente **67 MB**. Para facilitar su almacenamiento en GitHub utilizamos compresión GZIP, reduciendo su tamaño a aproximadamente **25 MB**.

```python
# Nombre del archivo de salida
nombre_csv_limpio = "mood_insights_limpio.csv.gz"

# Guardamos el dataset limpio y comprimido
df_nlp.to_csv(
    nombre_csv_limpio,
    index=False,
    encoding="utf-8-sig",
    compression="gzip"
)
```

### Explicación de los métodos y parámetros

| Método o parámetro | ¿Qué hace? |
|---|---|
| `to_csv()` | Exporta el DataFrame a un archivo CSV. |
| `index=False` | Evita guardar el índice como una columna adicional. |
| `encoding="utf-8-sig"` | Establece la codificación del texto. |
| `compression="gzip"` | Comprime el archivo sin eliminar información. |
| `.csv.gz` | Identifica un archivo CSV comprimido mediante GZIP. |

### Descargar el archivo desde Google Colab

Una vez generado el archivo comprimido, lo descargamos:

```python
from google.colab import files

files.download("mood_insights_limpio.csv.gz")
```

Después guardamos el archivo descargado dentro de la carpeta `data/` de nuestro repositorio.

**Fuente original:** [IMDb Dataset of 50K Movie Reviews (Spanish) — Kaggle](https://www.kaggle.com/datasets/luisdiegofv97/imdb-dataset-of-50k-movie-reviews-spanish).

**Resultado del EDA:** un dataset limpio y comprimido que podemos reutilizar directamente en NLP, evitando repetir todo el proceso de limpieza.


## 8. Ejecutar el NLP desde VS Code

**Notebook:** `notebook/MOOD_INSIGHTS_NLP.ipynb`

En esta fase utilizamos el dataset limpio generado en el EDA para entrenar nuestro modelo de análisis de sentimientos.

**No necesitamos descargar otra vez el dataset original ni repetir la limpieza**, porque los datos ya están preparados.

### Pasos del proceso

1. Comprobamos que el archivo `mood_insights_limpio.csv.gz` está dentro de `data/`.
2. Abrimos el notebook NLP en VS Code.
3. Seleccionamos el kernel de Python asociado al entorno virtual del proyecto.
4. Cargamos el dataset comprimido utilizando Pandas.
5. Verificamos las columnas y etiquetas.
6. Creamos las variables `X` (reseñas) e `y` (sentimientos).
7. Dividimos los datos en entrenamiento (80 %) y prueba (20 %).
8. Transformamos los textos en características numéricas con `CountVectorizer`.
9. Entrenamos el modelo `LogisticRegression` mediante un `Pipeline`.
10. Evaluamos las predicciones, la exactitud y las demás métricas.
11. Guardamos el modelo entrenado y sus resultados en la carpeta `modelos/`.

### Cargar el dataset comprimido

El archivo se encuentra en:

`data/mood_insights_limpio.csv.gz`

Pandas permite leerlo directamente sin tener que descomprimirlo manualmente.

**Si ejecutamos el notebook desde la raíz del repositorio:**

```python
import pandas as pd

# Cargamos el dataset comprimido
df = pd.read_csv(
    "data/mood_insights_limpio.csv.gz",
    compression="gzip"
)

# Comprobamos los datos
print(df.shape)
display(df.head())
```

**Si el directorio de trabajo es `notebook/`:**

```python
import pandas as pd

df = pd.read_csv(
    "../data/mood_insights_limpio.csv.gz",
    compression="gzip"
)
```

Para conocer nuestro directorio de trabajo podemos ejecutar:

```python
from pathlib import Path

print(Path.cwd())
```

### Explicación de los métodos

| Método o parámetro | ¿Qué hace? |
|---|---|
| `pd.read_csv()` | Lee un archivo CSV y lo convierte en un DataFrame. |
| `compression="gzip"` | Descomprime los datos durante la lectura. |
| `df.shape` | Muestra el número de filas y columnas. |
| `df.head()` | Muestra las primeras cinco filas. |
| `Path.cwd()` | Indica el directorio desde el que se está ejecutando Python. |

### ¿Y si utilizamos Google Colab?

Google Colab utiliza un entorno independiente de nuestro ordenador.

Para ejecutar el NLP en Colab debemos subir el archivo `mood_insights_limpio.csv.gz` o acceder a él mediante Google Drive u otra ubicación disponible.

Después adaptamos la ruta de lectura a la ubicación del archivo.

### Entrenamiento del modelo

Una vez cargados los datos, continuamos con el procesamiento del lenguaje natural.

Utilizamos `CountVectorizer` para transformar las reseñas en vectores numéricos y `LogisticRegression` para aprender a clasificarlas como positivas o negativas.

Ambos procesos están conectados mediante un `Pipeline` de Scikit-learn.

Finalmente, evaluamos el modelo y guardamos el resultado entrenado mediante `joblib`.

**Resultado del NLP:** un modelo de Machine Learning entrenado y evaluado que puede utilizarse desde nuestra aplicación Streamlit.


### ¿Y si utilizamos Google Colab?

Google Colab es una alternativa, pero no el entorno principal de este repositorio. En una sesión nueva normalmente debes **subir de nuevo `mood_insights_limpio.csv`** al entorno temporal (o montarlo desde Google Drive) antes de ejecutar el NLP. Después ajusta la ruta de `pd.read_csv()` a la ubicación del archivo. Si exportas el modelo desde Colab, descarga los resultados y colócalos en `modelo/` dentro de tu proyecto local.

## 9. Ejecutar la aplicación Streamlit

La aplicación utiliza el modelo entrenado; **no necesita ejecutar el EDA ni el NLP cada vez que se inicia**.

Con el entorno activado y desde la raíz del repositorio:

```powershell
python -m streamlit run app.py
```

Streamlit muestra una dirección local, normalmente `http://localhost:8501`. Abre esa dirección en el navegador si no se abre automáticamente.

**No uses `python app.py`** para iniciar Streamlit. Comprueba también que la ruta de carga del modelo en `app.py` coincide con `modelo/mood_insights_modelo.joblib`.

### Prueba rápida

1. Escribe «Me encantó la película, es preciosa y emocionante» y analiza la reseña.
2. Prueba «Qué película tan aburrida, no la recomiendo».
3. Introduce una opinión mixta: «La fotografía es preciosa, pero la historia es muy aburrida».
4. Consulta las predicciones y el historial; exporta el CSV si deseas conservarlo.

Estos ejemplos no garantizan una clasificación determinada. La ironía, las negaciones y los textos ambiguos son difíciles para un clasificador de este tipo.

## 10. ¿Qué ocurre al analizar una reseña?

```text
Reseña escrita en Streamlit
          ↓
Carga del Pipeline guardado (.joblib)
          ↓
CountVectorizer: convierte palabras en características numéricas
          ↓
LogisticRegression: predice el sentimiento
          ↓
Streamlit: muestra positivo/negativo y puntuaciones
          ↓
Historial temporal de la sesión
```

`modelo.predict([texto])` recibe una **lista de textos**, aunque solo analicemos uno. `modelo.classes_` permite asociar correctamente las puntuaciones a sus categorías.

## 11. Funciones relevantes de Streamlit

| Código | Función |
|---|---|
| `st.set_page_config(...)` | Configura la página. |
| `st.title(...)` | Muestra el título. |
| `st.text_area(...)` | Permite introducir una reseña. |
| `st.form(...)` | Agrupa el formulario. |
| `st.form_submit_button(...)` | Envía la reseña para analizarla. |
| `@st.cache_resource` | Evita recargar el modelo innecesariamente. |
| `joblib.load(...)` | Recupera el Pipeline entrenado. |
| `modelo.predict(...)` | Obtiene la categoría estimada. |
| `modelo.predict_proba(...)` | Calcula puntuaciones por categoría. |
| `st.session_state` | Conserva el historial durante la sesión. |
| `st.dataframe(...)` | Presenta los resultados en tabla. |
| `st.download_button(...)` | Permite descargar el historial. |

## 12. Detener la aplicación

En el terminal donde se ejecuta Streamlit, pulsa **Ctrl + C**. Para salir del entorno virtual:

```powershell
deactivate
```

La próxima vez basta con abrir el proyecto, activar `.venv` y ejecutar `python -m streamlit run app.py`.

## 13. Problemas frecuentes

| Problema | Comprobación o solución |
|---|---|
| `No module named streamlit` | Activa `.venv` e instala `python -m pip install -r requirements.txt`. |
| No se encuentra el CSV en NLP | Comprueba que está en `data/` y que `pd.read_csv()` utiliza la ruta relativa correcta. |
| No se encuentra el modelo en Streamlit | Comprueba que existe `modelo/mood_insights_modelo.joblib` y que `app.py` busca esa ruta. |
| PowerShell bloquea `Activate.ps1` | Usa CMD con `activate.bat` o el cambio temporal de política indicado antes. |
| `streamlit` no se reconoce | Ejecuta `python -m streamlit run app.py`. |
| Error por versión de `scikit-learn` | Revisa la versión con la que se generó el `.joblib` y reinstala las dependencias compatibles. |
| `Port 8501 is already in use` | Cierra la otra instancia o usa `python -m streamlit run app.py --server.port 8502`. |
| La predicción parece incorrecta | El modelo es estadístico y puede equivocarse. |

**Seguridad:** carga únicamente archivos `.joblib` de procedencia fiable. Deserializar modelos desconocidos puede ejecutar código no seguro.

## 14. Actualizar un repositorio de GitHub existente

Si ya tienes creado el repositorio y configurado el remoto, desde la raíz del proyecto:

```bash
git status
git add .
git commit -m "Actualizar documentación y flujo EDA-NLP"
git push
```

Revisa `.gitignore` para que excluya `.venv/`, archivos temporales y secretos. Decide expresamente si vas a publicar el CSV derivado, atendiendo a las condiciones de la fuente, y asegúrate de que el modelo y las métricas que deseas compartir figuran en el repositorio.

## 15. Evolución del NLP: V1 y V2

**V1** permite aprender los fundamentos: transformar palabras en números, entrenar un clasificador y evaluar los resultados.

**V2** amplía la representación del texto mediante unigramas y bigramas, filtrado del vocabulario y análisis de coeficientes asociados a cada sentimiento.

Ambas versiones emplean técnicas clásicas de **Bag of Words** y **regresión logística**; no son modelos profundos de comprensión del lenguaje. Una representación más amplia no garantiza por sí sola mejores resultados: es necesario comparar ambas versiones con el mismo conjunto de prueba.

## 16. Conclusiones y limitaciones

Con Butaca Emocional hemos conectado un flujo completo de trabajo: explorar y limpiar los datos, exportar un dataset reutilizable, entrenar un clasificador y utilizarlo desde una aplicación.

La clasificación es **binaria** y está entrenada para reseñas de películas. Puede fallar ante ironías, dobles negaciones, textos mixtos y vocabulario poco frecuente. Las puntuaciones del clasificador no equivalen a certezas ni describen el estado emocional real de una persona. Para incorporar la clase **neutra**, sería necesario disponer de ejemplos etiquetados y volver a entrenar y evaluar el modelo.

---

**Proyecto educativo · Fuente de datos: IMDb Dataset of 50K Movie Reviews (Spanish), publicado en Kaggle por `luisdiegofv97`.**


## 17. 💺 Versión 2 — Butaca Emocional (`version_V2/`)


### Archivos de la versión 2

| Archivo | Función |
|---|---|
| `version_V2/Butaca_Emocional.py` | Aplicación Streamlit V2: análisis de reseñas y visualizaciones con Plotly. |
| `version_V2/BUTACA_EMOCIONAL_MODELO_V2.ipynb` | Notebook del entrenamiento y la evaluación del modelo V2. |
| `version_V2/butaca_emocional_modelo_v2.joblib` | Pipeline entrenado para realizar predicciones. |
| `version_V2/metricas_v2.json` | Exactitud, matriz de confusión, precisión, recall y términos asociados a cada sentimiento. |
| `version_V2/README_BUTACA_EMOCIONAL_V2.md` | Guía detallada de funcionamiento y ejecución de la versión 2. |

**Importante:** `Butaca_Emocional.py` busca el `.joblib` y `metricas_v2.json` **en su misma carpeta**. No los muevas a `modelos/`, que corresponde a la versión principal.

### ¿Qué cambia respecto a la primera versión?

En V2 seguimos usando **CountVectorizer** y **regresión logística**, pero incluimos **unigramas y bigramas** (palabras individuales y parejas de palabras), con un vocabulario máximo de **40.000 términos**. La aplicación incorpora gráficos interactivos con **Plotly** y tres pestañas:

1. **Analiza una película:** introduce una reseña y consulta la clasificación positiva o negativa y sus probabilidades estimadas.
2. **Qué ha aprendido:** muestra palabras y expresiones con mayor peso estadístico en cada sentimiento.
3. **Resultados del modelo:** presenta exactitud, aciertos, errores, matriz de confusión y precisión/recall por clase.

El notebook V2 proporcionado **descarga el dataset original de Kaggle para su propio entrenamiento**. No debe confundirse con el flujo actualizado del NLP principal, que utiliza `data/mood_insights_limpio.csv` exportado desde el EDA.

### Resultados de la evaluación V2

Los valores siguientes proceden de `version_V2/metricas_v2.json` y describen el conjunto de prueba usado en esa versión:

| Indicador | Resultado |
|---|---:|
| Reseñas de entrenamiento | 39.679 |
| Reseñas de prueba | 9.920 |
| Tamaño del vocabulario | 40.000 términos |
| Exactitud | **87,64 %** |
| Aciertos | 8.694 |
| Errores | 1.226 |

Este resultado no demuestra por sí solo que V2 sea mejor que V1: para una comparación rigurosa hay que evaluarlas sobre el mismo conjunto de prueba.

### Ejecutar la versión 2 después de clonar el repositorio

Desde la **carpeta raíz del repositorio**, con el entorno virtual del proyecto activado (el mismo que utiliza V1):

```powershell
# Instala las dependencias generales, si todavía no lo has hecho.
python -m pip install -r requirements.txt

# Plotly se utiliza para los gráficos interactivos de V2.
python -m pip install plotly

# Inicia la aplicación V2 desde la raíz del repositorio.
python -m streamlit run version_V2/Butaca_Emocional.py
```

No necesitas crear otro entorno virtual ni volver a entrenar el modelo si los archivos `.joblib` y `.json` de V2 están disponibles. El modelo fue evaluado con `scikit-learn` **1.6.1**, según su JSON de métricas; utilizar otra versión puede causar incompatibilidades.

Para conocer el procedimiento de entrenamiento y las explicaciones sobre los gráficos, consulta [la documentación específica de V2](version_V2/README_BUTACA_EMOCIONAL_V2.md).
