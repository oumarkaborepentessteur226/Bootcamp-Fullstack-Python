-- -- Database: bootcamp
-- -- Création de table
-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );
-- -- Insertion de donnée
-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');
-- -- affichage des élements
-- SELECT * FROM FirstTab;
-- -- création d'une 2 ieme table

-- CREATE TABLE SecondTab (
--     id integer 
-- );
-- -- insertion de donnée
-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);
-- -- affichage des élements
-- SELECT * FROM SecondTab;

-- -- Questions
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( NULL);
-- 0
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- 2
SELECT COUNT(*) FROM FirstTab AS ft WHERE  ft.id NOT IN (SELECT id FROM SecondTab);
-- 0
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- 2
