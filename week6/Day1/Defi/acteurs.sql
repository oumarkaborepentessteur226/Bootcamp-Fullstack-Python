-- Database: Hollywood
-- 1
SELECT COUNT(*) FROM actors;
-- 2 
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('','','', );
-- Cette commande crée une erreur. En effet nous avons eu as spécifier 
-- lors de la création la contrainte NOT NULL 

