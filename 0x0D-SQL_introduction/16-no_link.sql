-- Lists all records of the table second_table of the database hbtn_0c_
-- in your MySQL server

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
