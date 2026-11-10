# 💺 Butaca Emocional — Versión 2

**Proyecto didáctico de procesamiento del lenguaje natural (NLP), aprendizaje automático y visualización de datos con Streamlit.**

Butaca Emocional analiza reseñas cinematográficas escritas en español y estima si su sentimiento es **positivo** o **negativo**. Además de analizar una reseña nueva, la aplicación muestra palabras asociadas a cada sentimiento y gráficos con los resultados obtenidos durante la evaluación del modelo.

> **Importante:** el programa solo clasifica entre **positivo** y **negativo**; no dispone de una categoría neutra. Sus predicciones son estimaciones y pueden fallar ante ironías, frases ambiguas o negaciones.

## 1. ¿Qué hemos hecho en este proyecto?

1. Trabajamos con un conjunto de reseñas de películas en español.
2. Preparamos los datos y los dividimos en entrenamiento y prueba.
3. Entrenamos un modelo de clasificación de textos con `scikit-learn`.
4. Evaluamos las predicciones y guardamos las métricas.
5. Exportamos el modelo entrenado a un archivo `.joblib` y los resultados a un `.json`.
6. Construimos una aplicación con **Streamlit** para escribir reseñas y consultar los resultados.
7. Utilizamos **Plotly** para presentar gráficos interactivos de las predicciones y métricas.

El notebook `BUTACA_EMOCIONAL_MODELO_V2.ipynb` documenta el proceso de entrenamiento. **Para ejecutar la aplicación no hace falta volver a entrenar el modelo**, siempre que tengamos los archivos `.joblib` y `.json` generados.

## 2. Archivos de la versión 2

Estos son los archivos que has proporcionado:

```text
version_V2/
├── Butaca_Emocional.py
├── BUTACA_EMOCIONAL_MODELO_V2.ipynb
├── butaca_emocional_modelo_v2.joblib
├── metricas_v2.json
└── README.md
```

**¡Atención al nombre del JSON!** El código de `Butaca_Emocional.py` busca un archivo llamado exactamente `metricas_v2.json`, **sin `(1)`**. Por tanto, antes de ejecutar, cambia el nombre:

```text
metricas_v2(1).json  →  metricas_v2.json
```

El archivo Python, el `.joblib` y el JSON deben estar **en la misma carpeta**. Puedes mantener el nombre `Butaca_Emocional.py`; no necesitas renombrarlo a `app.py` si usas el comando indicado en esta guía.

| Archivo | ¿Para qué sirve? |
| --- | --- |
| `Butaca_Emocional.py` | Código de la interfaz y las visualizaciones de Streamlit. |
| `BUTACA_EMOCIONAL_MODELO_V2.ipynb` | Notebook utilizado para preparar los datos, entrenar y evaluar el modelo. |
| `butaca_emocional_modelo_v2.joblib` | Modelo ya entrenado, listo para hacer predicciones. |
| `metricas_v2.json` | Resultados de la evaluación y términos relevantes para construir los gráficos. |
| `README.md` | Instrucciones para instalar, ejecutar y comprender el proyecto. |

## 3. Requisitos previos

Necesitas **Python**, **VS Code** (o un editor equivalente) y una terminal. Los comandos siguientes están escritos para **Windows PowerShell**.

El modelo proporcionado indica que fue entrenado con **Python 3.13.18** y **scikit-learn 1.6.1**. Para reducir posibles incompatibilidades, utiliza preferiblemente Python 3.13 y scikit-learn 1.6.1 al ejecutar este modelo ya entrenado. Una versión distinta puede producir advertencias o errores.

## 4. Abrir el proyecto y reutilizar el entorno virtual original

**La versión 2 está dentro del proyecto original y comparte su entorno virtual. No hay que crear otro `venv`.**

La estructura de carpetas es la siguiente (el entorno puede llamarse `venv` o `.venv`):

```text
BUTACA-EMOCIONAL/
├── venv/                       ← entorno virtual original (compartido)
└── version_V2/
    ├── Butaca_Emocional.py
    ├── BUTACA_EMOCIONAL_MODELO_V2.ipynb
    ├── butaca_emocional_modelo_v2.joblib
    ├── metricas_v2.json
    └── README.md
```

1. Abre en **VS Code la carpeta principal `BUTACA-EMOCIONAL`**, no es necesario crear ningún proyecto nuevo.
2. Abre **Terminal → Nuevo terminal**.
3. Si el entorno original todavía no está activado, actívalo desde la carpeta principal:

```powershell
.\venv\Scripts\Activate.ps1
```

Si tu entorno se llama `.venv`, utiliza ` .\.venv\Scripts\Activate.ps1 ` en su lugar. Si ya ves `(venv)` o `(.venv)` al comienzo de la terminal, omite este paso.

4. Desde la carpeta principal, entra en la versión 2:

```powershell
cd version_V2
```

**Atención:** si ya estás dentro de `version_V2`, no repitas `cd version_V2`.

## 5. Instalar solamente la librería nueva: Plotly

La versión original ya dispone de su propio entorno y sus librerías. En la versión 2 hemos incorporado **Plotly** para representar gráficos interactivos. Si no estaba instalada en el entorno compartido, ejecuta:

```powershell
python -m pip install plotly
```

Este comando añade Plotly **al mismo entorno virtual original**; no instala las librerías en una carpeta independiente. Comprueba que se puede importar:

```powershell
python -c "import plotly; print(plotly.__version__)"
```

Si aparece un número de versión, Plotly ya está disponible. No es necesario volver a instalar `streamlit`, `pandas`, `joblib` y `scikit-learn` si funcionaban en ese entorno.

## 6. Ejecutar Butaca Emocional V2

**Estando dentro de `version_V2` y usando el entorno original**, ejecuta:

```powershell
python -m streamlit run Butaca_Emocional.py
```

No utilices `python Butaca_Emocional.py` directamente: las aplicaciones Streamlit deben arrancarse con `streamlit run`.

**Comandos habituales, resumidos** (desde la carpeta principal):

```powershell
.\venv\Scripts\Activate.ps1
cd version_V2
python -m pip install plotly
python -m streamlit run Butaca_Emocional.py
```

La instalación de Plotly solo hace falta la primera vez que se añade al entorno; después puedes omitir esa línea.

**Antes de ejecutar**, comprueba que el archivo se llama exactamente `metricas_v2.json`, no `metricas_v2(1).json`.

### ¿Por qué necesitamos cada librería?

| Librería | Función en nuestra aplicación |
| --- | --- |
| `streamlit` | Construye la página, las pestañas, el cuadro de texto, el botón y los mensajes. |
| `pandas` | Organiza en tablas los datos de términos y métricas que usamos para graficar. |
| `plotly` | Crea gráficos **interactivos y personalizables**. |
| `joblib` | Abre el archivo `.joblib` que contiene el modelo entrenado. |
| `scikit-learn` | Proporciona los componentes de aprendizaje automático que necesita el modelo guardado para predecir. |

## 7. Plotly: la nueva librería de la versión 2

En nuestro archivo Python encontramos estas instrucciones:

```python
import plotly.express as px
import plotly.graph_objects as go
```

**¿Qué significa `import`?** Pide a Python que cargue una librería para poder utilizar sus herramientas.

**¿Qué significa `as px` o `as go`?** Le damos un nombre corto a cada módulo para escribir menos código.

### `plotly.express` (`px`)

Sirve para crear gráficos con pocas líneas. En Butaca Emocional lo usamos para mostrar **qué palabras o expresiones están más asociadas con reseñas positivas y negativas**.

```python
# px.bar() construye un gráfico de barras.
# x indica la columna con los valores numéricos.
# y indica la columna con las palabras que aparecerán como etiquetas.
figura = px.bar(tabla, x="magnitud", y="termino", orientation="h")
```

En este caso, `orientation="h"` significa **horizontal**.

### `plotly.graph_objects` (`go`)

Permite controlar con detalle el aspecto de cada gráfico. En nuestro proyecto lo usamos para:

- Mostrar las probabilidades estimadas de una reseña nueva con barras horizontales (`go.Bar`).
- Dibujar la **matriz de confusión** con cuatro casillas (`go.Heatmap`).
- Representar **aciertos y errores** en un gráfico circular (`go.Pie`).
- Comparar **precisión y recall** en barras agrupadas (`go.Bar`).

Por ejemplo:

```python
# Creamos un gráfico circular a partir de dos cantidades.
figura = go.Figure(
    go.Pie(labels=["Aciertos", "Errores"], values=[8694, 1226])
)
```

Los números del ejemplo corresponden a los resultados guardados en las métricas de esta versión. **Plotly no entrena el modelo ni calcula las predicciones**: representa visualmente los datos que ya tenemos.

### ¿Qué ventajas aporta Plotly?

Permite consultar valores al pasar el ratón, trabajar con barras y diagramas interactivos y personalizar colores, fuentes, tamaños y etiquetas. En nuestra aplicación usamos **verde `#20C997`** y **rosa `#FF6B81`** para diferenciar visualmente las categorías o los resultados.

### ¿Por qué aparece `ModuleNotFoundError: No module named 'plotly'`?

Porque el Python que está ejecutando la aplicación **no tiene instalado Plotly en su entorno**. Es posible que la versión 1 utilizara otro sistema de gráficos o que estés utilizando un entorno virtual distinto.

Solución, con el entorno correcto activado:

```powershell
python -m pip install plotly
```

Para comprobar la instalación:

```powershell
python -c "import plotly; print(plotly.__version__)"
```

Si devuelve un número de versión, Plotly se importa correctamente desde ese Python.

## 8. ¿Qué verás al ejecutar la versión 2?

Streamlit mostrará una dirección local, normalmente `http://localhost:8501`, donde podrás abrir la aplicación en el navegador.

### ¿Qué encontrarás en la aplicación?

**🎟️ Analiza una película:** escribe una reseña y pulsa **«✨ Analizar mi reseña»**. El modelo devuelve una clasificación positiva o negativa y muestra sus probabilidades estimadas.

**🧠 Qué ha aprendido:** consulta los términos con mayor asociación estadística a cada categoría. El peso de una palabra **no es el número de veces que aparece**.

**📊 Resultados del modelo:** consulta exactitud, número de pruebas, aciertos, errores, matriz de confusión y medidas de precisión y recall.

## 9. Resultados reales del modelo V2

Según el archivo de métricas adjunto:

| Medida | Resultado |
| --- | ---: |
| Reseñas para entrenar | 39.679 |
| Reseñas para probar | 9.920 |
| Tamaño del vocabulario | 40.000 términos |
| Exactitud | 87,64 % |
| Aciertos | 8.694 |
| Errores | 1.226 |

**¿Qué significa 87,64 % de exactitud?** Que el modelo acertó aproximadamente 88 de cada 100 reseñas en el **conjunto de prueba**. No significa que vaya a acertar siempre con reseñas nuevas.

La **matriz de confusión** permite separar los tipos de aciertos y errores. La **precisión** indica la proporción de predicciones de una clase que fueron correctas; el **recall** indica qué proporción de ejemplos reales de esa clase encontró el modelo.

## 10. Guardar las dependencias en `requirements.txt`

Cuando hayas instalado las librerías en el entorno correcto, puedes guardar la lista exacta de paquetes y versiones que contiene:

```powershell
python -m pip freeze > requirements.txt
```

Esto crea o sustituye `requirements.txt` en la carpeta desde la que ejecutas el comando.

Si otra persona quiere reproducir el proyecto en su propio equipo, podrá instalar las dependencias con:

```powershell
python -m pip install -r requirements.txt
```

> Este archivo **no se genera solo**: el comando anterior debes ejecutarlo en tu equipo, dentro del entorno que realmente funciona. Es normal que la lista incluya dependencias indirectas instaladas junto a las principales.

## 11. Errores frecuentes y soluciones

**`ModuleNotFoundError: No module named 'plotly'`**  
Ejecuta `python -m pip install plotly` en el entorno virtual que usa la aplicación.

**No sabes qué Python está ejecutando la aplicación**  
Compruébalo con:

```powershell
python -c "import sys; print(sys.executable)"
```

**La aplicación dice que falta `metricas_v2.json`**  
Comprueba que no se llama `metricas_v2(1).json`. Debe estar en la misma carpeta que el archivo `.py`.

**La aplicación dice que falta el `.joblib`**  
Verifica que su nombre sea exactamente `butaca_emocional_modelo_v2.joblib` y que esté junto a `Butaca_Emocional.py`.

**Aparece una advertencia sobre la versión de scikit-learn**  
El archivo de métricas registra la versión **1.6.1** durante el entrenamiento. Utiliza preferiblemente esa versión en el entorno de ejecución. Si el modelo se entrenó con una versión distinta de la que utilizas, la compatibilidad no está garantizada.

**Streamlit no se abre al ejecutar el archivo con el botón normal de Python**  
Lánzalo desde la terminal con `python -m streamlit run Butaca_Emocional.py`, no con `python Butaca_Emocional.py`.

## 12. Resumen del proceso

```text
Abrir el proyecto original en VS Code
        ↓
Activar el venv original (si no está activado)
        ↓
Entrar en version_V2 e instalar Plotly si falta
        ↓
Comprobar nombres y ubicación del .joblib y el .json
        ↓
Ejecutar Streamlit
        ↓
Escribir una reseña y explorar los gráficos
        ↓
Guardar requirements.txt para reproducir el entorno
```

---

**Butaca Emocional V2** es un proyecto de aprendizaje que integra preparación de datos, NLP, clasificación automática, evaluación de modelos y presentación visual de resultados con Python.
