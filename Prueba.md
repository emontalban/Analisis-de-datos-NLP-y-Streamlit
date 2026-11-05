## Día 1 · Investigar y descubrir

Define el problema en dos frases. Ejemplo: “Las empresas reciben miles de opiniones y no pueden leerlas todas. Mood-Insights clasifica cada comentario como positivo, negativo o neutro automáticamente.”

Define quién se beneficia: tiendas online, hoteles, restaurantes, equipos de atención al cliente.
Descarga el dataset y crea el repositorio en GitHub desde el principio (carpeta con data/, notebooks/, app/).

Carga los datos con Pandas: `read_csv`, **head()**, info(), shape.

- Explorala calidad: nulos, duplicados, textos vacíos, y si las clases están equilibradas (value_counts()).

- Limpia: elimina nulos y duplicados, pasa a minúsculas, quita espacios raros. No hace falta limpiar en exceso, porque CountVectorizer ya ayuda con parte de ello.
Formula 3 preguntas de análisis, por ejemplo:
¿Qué sentimiento es más frecuente en el dataset?
¿Los comentarios negativos son más largos que los positivos?
¿Qué palabras aparecen más en cada categoría?
EDA con 3 gráficos de Matplotlib:
Barras con la distribución de clases.
Histograma de la longitud de los comentarios por sentimiento.
Barras con las palabras más frecuentes en positivos vs. negativos.
Escribe las primeras conclusiones debajo de cada gráfico.
Boceta la app en papel: una caja de texto, un botón y el resultado.