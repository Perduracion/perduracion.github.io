USE MANJAR;

/* Create tables with IF NOT EXISTS checks */
CREATE TABLE IF NOT EXISTS user (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  user_name VARCHAR(60) NOT NULL UNIQUE,
  user_mail VARCHAR(255) NOT NULL,
  user_password VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
  cat_id INT PRIMARY KEY AUTO_INCREMENT,
  cat_desc VARCHAR(60)
);

CREATE TABLE IF NOT EXISTS product (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(60) NOT NULL,  
  product_desc VARCHAR(155) NOT NULL,
  product_image_path VARCHAR(15) NULL, 
  product_price DECIMAL(10,2) NULL, 
  product_cat_id INT,
  CONSTRAINT fk_cat_id FOREIGN KEY (product_cat_id) REFERENCES category (cat_id)
);

/* Poblar categorías con bebidas y alimentos */
INSERT INTO category (cat_desc)
VALUES
  ('Bebidas'),
  ('Alimentos');

/* Poblar productos con ejemplos de bebidas */
INSERT INTO product (product_name, product_desc, product_price, product_cat_id)
VALUES
  ('Coca-Cola', 'Refresco carbonatado', 2.50, 1),
  ('Sprite', 'Gaseosa de limón y lima', 2.50, 1),
  ('Jugo de Naranja', 'Jugo de naranja 100% puro', 3.00, 1),
  ('Café', 'Café caliente recién hecho', 2.00, 1),
  ('Té', 'Té caliente recién hecho', 2.00, 1);

/* Poblar productos con ejemplos de alimentos */
INSERT INTO product (product_name, product_desc, product_price, product_cat_id)
VALUES
  ('Hamburguesa', 'Hamburguesa de carne con lechuga, tomate y cebolla', 5.99, 2),
  ('Pizza', 'Salsa de tomate, queso y toppings sobre una base de masa', 7.99, 2),
  ('Ensalada', 'Mezcla de verduras, hortalizas y aderezo', 4.99, 2),
  ('Pasta', 'Pasta cocida con salsa y toppings', 6.99, 2),
  ('Frutas', 'Surtido de frutas frescas', 3.99, 2);