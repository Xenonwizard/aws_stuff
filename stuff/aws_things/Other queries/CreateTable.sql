CREATE DATABASE myDBName;

USE myDBName;

CREATE TABLE mytable (id VARCHAR(100),hash VARCHAR(200));

CREATE USER 'master'@'%' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON myDBName.* TO 'master'@'%';