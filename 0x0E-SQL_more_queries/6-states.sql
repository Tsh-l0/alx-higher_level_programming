-- Creates the database 'hbtn_0d_usa' and the table 'states'
-- The 'id' column must be unique, auto-generated, can't be null, and
-- is a primary key

-- Create a database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the new database
USE hbtn_0d_usa;

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
