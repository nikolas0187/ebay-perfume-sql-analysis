-- Creo tabla para perfumes de hombres
CREATE TABLE mens_perfume (
    brand VARCHAR(255),
    title TEXT,
    type VARCHAR(100),
    price NUMERIC,
    priceWithCurrency VARCHAR(50),
    available INT,
    availableText VARCHAR(255),
    sold INT,
    last_updated VARCHAR(100),
    itemLocation VARCHAR(255)
);

--Creo tabla para perfumes de mujeres
CREATE TABLE womens_perfume (
    brand VARCHAR(255),
    title TEXT,
    type VARCHAR(100),
    price NUMERIC,
    priceWithCurrency VARCHAR(50),
    available INT,
    availableText VARCHAR(255),
    sold INT,
    last_updated VARCHAR(100),
    itemLocation VARCHAR(255)
);

-- Copio la información de los archivos CSV a la base de datos
COPY mens_perfume
FROM 'C:\Users\Public\SQL PROJECT\ebay_mens_perfume.csv'
DELIMITER ','
CSV HEADER;

COPY womens_perfume
FROM 'C:\Users\Public\SQL PROJECT\ebay_womens_perfume.csv'
DELIMITER ','
CSV HEADER;

-- Reto 1: Descubrir las 10 marcas de perfume para hombre con mayor 
-- volumen de productos listados en plataforma y además saber el precio promedio de sus productos.

SELECT
    brand,
    COUNT(brand) AS total_productos,
    ROUND(AVG(price), 2) AS precio_promedio
FROM
    mens_perfume
GROUP BY brand
ORDER BY total_productos DESC
LIMIT 10;

-- Reto 2: Evaluar el volumen de mercado y la distribución de precios (Mín, Máx, Prom) 
-- para las presentaciones con mayor presencia en la plataforma (>100 anuncios).

SELECT
    type AS presentacion,
    COUNT(type) AS cantidad_total,
    ROUND(MIN(price), 2) AS precio_minimo,
    ROUND(MAX(price), 2) AS precio_maximo,
    ROUND(AVG(price), 2) AS precio_promedio
FROM
    mens_perfume
WHERE
    type IS NOT NULL
GROUP BY
    type
HAVING
    COUNT(type) >= 100
ORDER BY cantidad_total DESC;
    
-- Reto 3: Crear un reporte unificado que diga cuántos perfumes hay listados en total
-- en toda la plataforma (juntando hombres y mujeres), pero pudiendo distinguir
-- a qué género pertenece cada producto en el resultado final.

SELECT
    'hombre' AS genero,
    brand,
    price
FROM
    mens_perfume

UNION ALL

SELECT
    'mujer' AS GENERO,
    brand,
    price
FROM
    womens_perfume;

SELECT
    genero,
    COUNT(*) AS total_perfumes,
    ROUND(AVG(price), 2) AS precio_promedio
FROM (
    SELECT
    'hombre' AS genero,
    brand,
    price
FROM
    mens_perfume

UNION ALL

SELECT
    'mujer' AS GENERO,
    brand,
    price
FROM
    womens_perfume
) AS mercado_global

GROUP BY genero
ORDER BY precio_promedio DESC;
