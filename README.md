Explorando los factores que influyeron en la supervivencia de los pasajeros del Titanic
---

## Introducción

El Titanic, conocido como el "Barco de los Sueños", se hundió el 15 de abril de 1912 durante su viaje inaugural, dejando una huella imborrable en la historia marítima. Este desastre se ha convertido en un caso emblemático para el análisis de datos debido a la rica información demográfica y socioeconómica de sus pasajeros.

### Objetivo del Proyecto

Este proyecto busca responder preguntas clave sobre los factores que influyeron en la supervivencia de los pasajeros. En concreto, se examinan aspectos como la clase social, el género, la edad, y el costo del boleto para entender cómo estos factores afectaron las probabilidades de supervivencia.

### Alcance del Proyecto

- **Exploración del dataset**: Análisis descriptivo y visual de las características de los pasajeros.
- **Identificación de patrones**: Relación entre variables como género, edad y clase con la supervivencia.
- **Visualizaciones interactivas**: Representación gráfica de los datos para facilitar la comprensión de los resultados.

---

## Datos Utilizados

### Fuente de los Datos

El dataset utilizado en este proyecto proviene de [Kaggle](https://www.kaggle.com/competitions/titanic), uno de los recursos más populares para análisis de datos y aprendizaje automático.

### Descripción General del Dataset

- **Número de filas**: 891
- **Número de columnas**: 12
- **Variables principales**:
  - `Survived`: Indica si un pasajero sobrevivió (1) o no (0).
  - `Pclass`: Clase del pasajero (1ª, 2ª, 3ª).
  - `Sex`: Género del pasajero.
  - `Age`: Edad del pasajero.
  - `Fare`: Costo del boleto.
  - `Embarked`: Puerto de embarque (C = Cherburgo, Q = Queenstown, S = Southampton).

### Limpieza y Preprocesamiento

Se realizaron las siguientes tareas para preparar los datos para el análisis:

- **Manejo de valores faltantes**:
  - Imputación de edades faltantes basadas en la mediana por clase.
  - Asignación del puerto de embarque más frecuente para valores nulos en `Embarked`.
- **Transformación de variables**:
  - Codificación de variables categóricas como `Sex` y `Embarked`.
  - Normalización del costo del boleto (`Fare`) para análisis de correlaciones.
- **Generación de nuevas variables**:
  - Agrupación de edades en rangos.
  - Creación de una columna "Familia" que combina `SibSp` y `Parch`.

---

## Funcionalidades de la Aplicación

### Visualizaciones

El proyecto incluye una amplia gama de gráficos interactivos y estáticos que facilitan la exploración de los datos:

- **Histogramas** para analizar la distribución de variables como edad y costo del boleto.
- **Gráficos de barras** que muestran tasas de supervivencia según clase, género y puerto de embarque.
- **Diagramas de dispersión** para examinar la relación entre edad y costo del boleto.
- **Diagramas de pastel** para proporciones de supervivencia.

### Interactividad

La aplicación, construida con Streamlit, permite a los usuarios interactuar con los datos de diversas maneras:

- Filtros dinámicos para seleccionar pasajeros por clase, género o rango de edad.
- Selectores de puerto de embarque para analizar diferencias geográficas.
- Opciones para destacar patrones en gráficos, como diferencias en las tasas de supervivencia.

### Análisis Clave

A partir del análisis, se identificaron los siguientes hallazgos:

1. **El género fue un factor clave**:
   - El 74% de las mujeres sobrevivieron, en comparación con solo el 19% de los hombres.
   
2. **La clase social influyó significativamente**:
   - Los pasajeros de 1ª clase tuvieron una tasa de supervivencia del 63%, mientras que los de 3ª clase solo alcanzaron el 24%.

3. **Los niños tuvieron mayores probabilidades de sobrevivir**:
   - Los menores de 15 años presentaron una tasa de supervivencia significativamente mayor que los adultos.

4. **El puerto de embarque también fue un factor relevante**:
   - Los pasajeros que embarcaron en Cherburgo (`C`) mostraron tasas de supervivencia más altas que aquellos de Southampton (`S`) o Queenstown (`Q`).

---
