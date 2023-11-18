-- Create a new database for the Kraal Web Application
CREATE DATABASE IF NOT EXISTS kraal_dev_db;
CREATE DATABASE IF NOT EXISTS kraal_test_db;

-- Create a dedicated development user with limited privileges
CREATE USER IF NOT EXISTS 'dev_user'@'localhost' IDENTIFIED BY 'dev_user_pwd';

-- GRANT permission on the development and testing databases
GRANT ALL PRIVILEGES ON kraal_dev_db.* TO 'dev_user'@'localhost';
GRANT ALL PRIVILEGES ON kraal_test_db.* TO 'dev_user'@'localhost';
