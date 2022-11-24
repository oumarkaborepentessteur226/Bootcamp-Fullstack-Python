-- -- Database: public
-- ---- Exercice 1 : Articles Et Clients1
-- -- 1
-- SELECT * FROM items ORDER BY prix ASC; 
-- -- 2
-- SELECT * FROM items WHERE prix >=80 ORDER BY prix DESC; 
-- -- 3
-- SELECT first_name,last_name FROM customers  ORDER BY first_name ASC LIMIT 3; 
-- -- 4
-- SELECT last_name FROM customers  ORDER BY last_name DESC;

-- Database: dvdrental
-- Exercice 2 : Base De Données Dvdrental
-- 1
SELECT * FROM customer;
-- 2
SELECT (first_name, last_name) as full_name FROM customer;
-- 3
SELECT DISTINCT create_date FROM customer;
-- 4
SELECT * FROM customer ORDER BY first_name DESC;
-- 5
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;
-- 6
SELECT address,phone FROM address WHERE district='Texas';
-- 7
SELECT * FROM film WHERE film_id IN (15,150) ;
-- 8
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title='African Egg';
-- 9
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'Af%';
-- 10
SELECT  film_id,title,description,film.length,rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
-- 11
SELECT  film_id,title,description,film.length,rental_rate FROM film  ORDER BY rental_rate ASC  OFFSET 10 FETCH FIRST 10 ROWS ONLY;
-- 12
SELECT p.amount, p.payment_date FROM payment p INNER JOIN customer c ON p.customer_id=c.customer_id ORDER BY c.customer_id ASC;
-- 13
SELECT f.film_id,f.title,f.description,f.length,f.rental_rate FROM film f WHERE f.film_id NOT IN (SELECT film_id FROM inventory);
-- 14
SELECT o.country, i.city FROM country o INNER JOIN city i ON i.country_id=o.country_id;


