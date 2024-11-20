-- Creates the table unique_id on MySQL server
-- unique_id has the columns 'id' and 'name'. The 'id' column has a
-- default value of 1 and it is unique

-- Create a table if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
