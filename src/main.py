import pandas as pd
import matplotlib.pyplot as plt
import os


#CARGAR Y LIMPIEZA BÁSICA DEL DATASET
print("LIMPIEZA")
df = pd.read_csv('data/Pokemon.csv')

# Limpiar espacios en los nombres de las columnas
df.columns = df.columns.str.strip()

# Tratar valores nulos: Los Pokémon sin 'Type 2' se rellenan con 'None'
df['Type 2'] = df['Type 2'].fillna('None')

# Eliminar duplicados si los hubiera
df = df.drop_duplicates()

print(f"Dimensiones del dataset limpio: {df.shape}")
print("Valores nulos después de la limpieza:\n", df.isnull().sum().head())

#ESTADÍSTICAS DESCRIPTIVAS

print("\nESTADÍSTICAS DESCRIPTIVAS")
# Resumen numérico de las estadísticas base de los Pokémon
print(df[['Total', 'HP', 'Attack', 'Defense', 'Speed']].describe())


#AGRUPACIONES 
print("\nAGRUPACIONES")
# Agrupar por Tipo Principal (Type 1) para ver el promedio de ataque de cada tipo
promedio_ataque_tipo = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)
print("\nPromedio de Ataque por Tipo Principal (Top 5):")
print(promedio_ataque_tipo.head())


#IDENTIFICACIÓN DE TENDENCIAS
print("\nIDENTIFICACIÓN DE TENDENCIAS")
# Tendencia del poder total promedio por Generación
tendencia_generacion = df.groupby('Generation')['Total'].mean()
print("\nPoder Total Promedio por Generación:")
print(tendencia_generacion)


# VISUALIZACIONES
# Configuramos una figura con 3 subgráficos para mostrar las visualizaciones
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Gráfico 1: Cantidad de Pokémon por Tipo Principal (Gráfico de Barras)
conteo_tipos = df['Type 1'].value_counts()
axes[0].bar(conteo_tipos.index, conteo_tipos.values, color='skyblue')
axes[0].set_title('Cantidad de Pokémon por Tipo Principal')
axes[0].set_xlabel('Tipo Principal (Type 1)')
axes[0].set_ylabel('Cantidad')
axes[0].tick_params(axis='x', rotation=90)

# Gráfico 2: Relación entre Ataque y Defensa (Gráfico de Dispersión / Scatter)
axes[1].scatter(df['Attack'], df['Defense'], alpha=0.6, color='coral')
axes[1].set_title('Relación: Ataque vs Defensa')
axes[1].set_xlabel('Ataque (Attack)')
axes[1].set_ylabel('Defensa (Defense)')

# Gráfico 3: Distribución del Poder Total por Generación (Gráfico de Líneas / Tendencia)
axes[2].plot(tendencia_generacion.index, tendencia_generacion.values, marker='o', color='green', linewidth=2)
axes[2].set_title('Tendencia del Poder Total Promedio por Generación')
axes[2].set_xlabel('Generación')
axes[2].set_ylabel('Poder Total Promedio (Total)')
axes[2].grid(True)

ruta_carpeta = os.path.join('docs', 'evidencias')
ruta_imagen = os.path.join(ruta_carpeta, 'graficos_pokemon.png')
plt.savefig(ruta_imagen, dpi=300, bbox_inches='tight')
print(f"\n✅ Visualizaciones guardadas exitosamente en: {ruta_imagen}")

plt.tight_layout()
plt.show()
