import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargo los datasets originales

df_mens = pd.read_csv('ebay_mens_perfume.csv')
df_womens = pd.read_csv('ebay_womens_perfume.csv')

# 2. Agrego columna género a cada DataFrame para concantenarlos

df_mens['genero'] = 'Hombre'
df_womens['genero'] = 'Mujer'

# 3. Concateno ambos DataFrames

df_global = pd.concat([df_mens, df_womens], ignore_index=True)

# 4. Verifico que tan limpia viene la base de datos

print("\n" + "="*40)
print("   AUDITORIA DE CALIDAD DE DATOS   ")
print("="*40)

## Verifico registros duplicados exactos

duplicados = df_global.duplicated().sum()
print(f"Registros completamente duplicados: {duplicados}")

print("n\--- Registro(s) Duplicado(s) Encontrado(s)---")
print(df_global[df_global.duplicated(keep=False)])

## Verifico valores nulos (columna por columna)

print("\n Valores nulos detectados por columna:")
print(df_global.isnull().sum())

## Verfico si hay precios en $0 o negativos (lo cual sería un error de datos)

precios_cero = (df_global['price'] <= 0).sum()
print(f"n\ Registros con precios menores o iguales a $0: {precios_cero}")

## Reviso si hay inconsistencias en las categorias principales

espacios_blanco = (df_global['brand'].str.strip() =='').sum() if 'brand' in df_global.columns else 0
print(f" Registros en la columna 'brand' vacía (espacios en blanco): {espacios_blanco}")

# Limpio filas duplicadas

df_global = df_global.drop_duplicates()

# Elimino filas donde precios o marca sean nulos

df_global = df_global.dropna(subset=['price', 'brand'])

# Relleno nulos en columnas secundarias

columnas_texto = ['type', 'availableText', 'lastUpdated']

df_global[columnas_texto] = df_global[columnas_texto].fillna('No Especificado')

columnas_numericas = ['available', 'sold']

df_global[columnas_numericas] = df_global[columnas_numericas].fillna(0) 

# 4. Verifico limpieza

print("\n" + "="*40)
print("   AUDITORIA DE CALIDAD DE DATOS   ")
print("="*40)

## Verifico registros duplicados exactos

duplicados = df_global.duplicated().sum()
print(f"Registros completamente duplicados: {duplicados}")

print("n\--- Registro(s) Duplicado(s) Encontrado(s)---")
print(df_global[df_global.duplicated(keep=False)])

## Verifico valores nulos (columna por columna)

print("\n Valores nulos detectados por columna:")
print(df_global.isnull().sum())

## Verfico si hay precios en $0 o negativos (lo cual sería un error de datos)

precios_cero = (df_global['price'] <= 0).sum()
print(f"n\ Registros con precios menores o iguales a $0: {precios_cero}")

## Reviso si hay inconsistencias en las categorias principales

espacios_blanco = (df_global['brand'].str.strip() =='').sum() if 'brand' in df_global.columns else 0
print(f" Registros en la columna 'brand' vacía (espacios en blanco): {espacios_blanco}")


# 5. Primer vistazo estadístico en consola

print("--- Estructura del Dataset Global---")
print(df_global.info())
print("\n--- Resumen Estadístico de Precios---")
print(df_global.groupby('genero')['price'].describe())

# Comparo la distribución de precios por género usando Boxplot
# combinado con un Swarmplot/Stripplot

# 1. Configuro el estilo del gráfico

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 2. Creo gráfico de cajas (Boxplot) para ver la dispersión y outliers

sns.boxplot(
    data=df_global,
    x='genero',
    y='price',
    palette={'Hombre': '#1f77b4', 'Mujer': '#e377c2'},
    fliersize=5
)

## personalizo el diseño

plt.title('Distribución de Precios de Perfumes en Ebay por Género', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Genero del Perfume', fontsize=12)
plt.ylabel('Precio en USD ($)', fontsize=12)

# Guardo

plt.savefig('distribucion_precios.png', dpi=300, bbox_inches='tight')
plt.show()

# LIMPIEZA

# 1. Filtro los datos para remover los outliers extremos (precios menores a 150)

df_filtrado = df_global[df_global['price'] < 150]

# 2. Configuro la nueva figura

plt.figure(figsize=(10, 6))

# 3. Creo un gráfico combinado: Boxplot + Violinplot (para ver densidad)

sns.violinplot(
    data=df_filtrado,
    x='genero',
    y='price',
    palette={'Hombre': '#1f77b4', 'Mujer': '#e377c2'},
    inner='quartile'
)

# Títulos del gráfico limpio

plt.title('Densidad de Precios en el Mercado Masivo (< $150 USD)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Género del Perfume', fontsize=12)
plt.ylabel('Precio en USD ($)', fontsize=12)

# Guardo la version limpia

plt.savefig('Densidad_precios_limpio.png', dpi=300, bbox_inches='tight')
plt.show()

# Guardo el Dataset limpio y unificado en un nuevo archivo

df_global.to_csv("ebay_perfumes_global_limpio.csv", index=False)
print("n\ Éxito! Dataset guardado como 'ebay_perfumes_global_limpio.csv'")
