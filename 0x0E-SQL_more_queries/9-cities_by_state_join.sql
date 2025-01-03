-- Lists all cities contained in the database hbtn_0d_usa
-- Sorted by 'cities.id'

-- Switch to the desired database
USE hbtn_0d_usa;

-- List all cities with corresponding state names
SELECT
	cities.id, cities.name, states.name
FROM
	cities
JOIN
	states
ON
	cities.state_id = states.id
ORDER BY
	cities.id ASC;
