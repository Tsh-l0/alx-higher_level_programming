-- Creates the table id_not_null on MySQL server
-- The id column has a default value of 1

-- Create a table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
