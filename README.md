# Pokemon
Este proyecto realiza un análisis descriptivo de los datos históricos de Pokémon para identificar patrones y factores clave que influyen en sus estadísticas de combate.

Dataset
Nombre del dataset: Pokémon Dataset

Fuente: (https://www.kaggle.com/datasets/abcsds/pokemon)

Descripción breve: El conjunto de datos contiene información detallada sobre las características de los Pokémon (puntos de salud, ataque, defensa, ataque especial, defensa especial, velocidad, generación, tipos primarios y secundarios, y condición de legendario).

Objetivo
El objetivo principal es analizar las estadísticas de los Pokémon para identificar patrones relacionados con su poder y distribución mediante análisis estadístico y visualización de datos. Se busca responder preguntas clave de negocio y analíticas, como la distribución de poder por tipos de Pokémon o la evolución de sus estadísticas a lo largo de las generaciones.

Requisitos
Para ejecutar este proyecto se requiere Python 3 y las siguientes dependencias principales, las cuales están detalladas con sus versiones exactas en el archivo requirements.txt:

pandas

matplotlib

Instalación
Para obtener una copia funcional de este proyecto en tu máquina local, sigue estos pasos:

Clonar el repositorio:

Bash
git clone https://github.com/DanCro21/Pokemon
Entrar al directorio del proyecto:

Bash
cd analisis-pokemon-descriptivo
Crear el entorno virtual:

Bash
python -m venv .venv
Activar el entorno e instalar dependencias:

En Linux/macOS:

Bash
source .venv/bin/activate
pip install -r requirements.txt
En Windows:

Bash
.venv\Scripts\activate
pip install -r requirements.txt
Ejecución
Para ejecutar el análisis completo y generar las visualizaciones automáticamente, ejecuta el siguiente comando desde la raíz del proyecto:

Bash
python src/main.py
Análisis realizados
Durante la ejecución del script, se aplican los siguientes procesos:

Limpieza y Preprocesamiento: Estandarización de nombres de columnas y tratamiento de valores nulos lógicos (como los tipos secundarios vacíos).

Estadísticas Descriptivas: Resumen numérico y cálculo de métricas clave sobre las estadísticas base de combate.

Análisis Agrupados (Insights):

Cálculo del promedio de ataque agrupado por el tipo principal (Type 1) del Pokémon.

Análisis de la tendencia del poder total promedio (Total) a lo largo de las diferentes generaciones.

Identificación de la relación analítica entre las variables de ataque y defensa.

Resultados y conclusiones
A partir de los análisis y las 3 visualizaciones generadas, se destacan los siguientes hallazgos principales:

Abundancia de tipos: Los tipos Agua y Normal son los más numerosos dentro del ecosistema de datos, representando una parte significativa del total de registros.

Tipos más poderosos: Los tipos Dragón y Acero concentran los promedios más altos de ataque y estadísticas base de combate, posicionándose por encima del promedio general.

Impacto de los legendarios: Los Pokémon legendarios se ubican de forma consistente en el extremo superior de la distribución de poder, generando un sesgo positivo en las métricas globales del dataset.