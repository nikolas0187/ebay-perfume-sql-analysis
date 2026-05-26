# Análisis de Mercado de Perfumes en eBay usando SQL (PostgreSQL)

# Descripción del Proyecto
Este proyecto consiste en el diseño, carga y análisis de un conjunto de datos reales de perfumes (hombres y mujeres) listados en eBay. El objetivo es extraer insights comerciales sobre el volumen de productos, estrategias de precios y preferencias del mercado utilizando consultas avanzadas en PostgreSQL de extremo a extremo en un único script.

# Tecnologías Utilizadas
* **Base de Datos:** PostgreSQL
* **Editor/IDE:** VS Code / pgAdmin 4
* **Lenguaje:** SQL

# Retos Resueltos & Insights Clave

## Reto 1: Top 10 Marcas con Mayor Volumen y su Precio Promedio
* **Objetivo:** Identificar las marcas líderes en stock y evaluar su posicionamiento de precio.
* **Insight Extraído:** (Aquí puedes anotar un par de marcas líderes de tu resultado).

## Reto 2: Análisis por Tipo de Concentración (Eau de Toilette vs. Eau de Parfum)
* **Objetivo:** Comparar métricas de precio (Mín, Máx, Prom) filtrando por categorías con alta presencia (>100 anuncios).
* **Insight Extraído:** El *Eau de Parfum* mantiene un precio promedio significativamente mayor ($58.83) frente al *Eau de Toilette* ($40.12), confirmando que el mercado está dispuesto a pagar un premium por mayor concentración de fragancia.

## Reto 3: Consolidación del Mercado Global (Hombres vs. Mujeres)
* **Objetivo:** Unificar los catálogos mediante subconsultas y `UNION ALL` para un benchmark de género.
* **Insight Extraído:** A pesar de tener un volumen de oferta idéntico en la muestra (1,000 anuncios cada uno), la categoría masculina promedia precios más altos ($46.48) que la femenina ($39.89).

---
## 📂 Estructura del Repositorio
* `perfume_project.sql`: Script único y estructurado de extremo a extremo. Contiene la creación de las tablas, la importación de datos (`COPY`) y los 3 bloques de consultas analíticas organizados con comentarios.
