-- Analisis kenaikan harga RAM dan SSD tahun 2026

SELECT 
    product_type,
    brand,
    capacity,
    MIN(price) AS harga_awal,
    MAX(price) AS harga_akhir,
    (MAX(price) - MIN(price)) AS kenaikan_harga
FROM price_history
GROUP BY product_type, brand, capacity;
