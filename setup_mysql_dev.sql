-- creates the MySQL server user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
SET GLOBAL validate_password_policy
=LOW;
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
