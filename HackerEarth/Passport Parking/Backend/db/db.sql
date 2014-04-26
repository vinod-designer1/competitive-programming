
CREATE DATABASE IF NOT EXISTS Calculator;

USE Calculator;

CREATE TABLE IF NOT EXISTS User
(
	u_id int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	ip varchar(23) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Operations
(
	op_id int(20) AUTO_INCREMENT PRIMARY KEY,
	u_id int(20) NOT NULL FOREIGN KEY REFERENCES User(u_id) ON DELETE CASCADE,
	operation varchar(200) NOT NULL,
	answer varchar(100) NOT NULL,
	op_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);