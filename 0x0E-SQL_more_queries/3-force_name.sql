-- Creates the table force_name on the MySQL server
-- The name column can not be null

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
	);
