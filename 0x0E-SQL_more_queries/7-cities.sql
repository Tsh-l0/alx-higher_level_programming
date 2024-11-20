-- Creates the database hbtn_0d_usa and the table cities (in the database
-- hbtn_0d_usa) on your MySQL server.


-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- sWITCH TO THE DATABASE 
USE hbtn_0d_usa;

-- Create the table 'states'
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);

-- Create the table 
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
