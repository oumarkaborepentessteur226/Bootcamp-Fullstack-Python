-- Database: public

CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	element VARCHAR (100) NOT NULL,
	prix SMALLINT NOT NULL
);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
 	first_name VARCHAR (50) NOT NULL,
 	last_name VARCHAR (100) NOT NULL
);

INSERT INTO items(element,prix)
VALUES
	('Petit bureau',100),
	('Grand bureau',300),
	('Ventilateur',80);
	
INSERT INTO customers(first_name,last_name)
VALUES
	('Greg','Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Vert'),
	('Mélanie','Johnson');

-- 1
SELECT * FROM items
-- 2
SELECT * FROM items WHERE prix > 80
-- 3
SELECT * FROM items WHERE prix <= 300
-- 4
SELECT * FROM customers WHERE last_name = 'Smith'
-- 5
SELECT * FROM customers WHERE last_name = 'Jones'
-- 6
SELECT * FROM customers WHERE last_name != 'Scott'