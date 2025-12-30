-- Membuat tabel harga hardware tahun 2026

CREATE TABLE price_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(10),
    brand VARCHAR(50),
    capacity VARCHAR(20),
    month VARCHAR(20),
    year INT,
    price INT
);
