-- Lists all cities of California from the database 'hbtn_0d_usa',
-- sorted by 'cities.id'.

-- Switch to the desired database
USE hbtn_0d_usa;

-- Without using the JOIN keyword to list all the cities of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
