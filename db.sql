CREATE DATABASE GeirPetter

USE GeirPetter

CREATE TABLE Brukere (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    passord varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Bestilling (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    message varchar(255) NOT NULL,
    PRIMARY KEY (id)
);



INSERT INTO Brukere (username, email, passord) VALUES ("Bob", "Bob@gmail.com", "Bob123")
INSERT INTO Brukere (username, email, passord) VALUES ("max", "max@gmail.com", "max123456")
INSERT INTO Brukere (username, email, passord) VALUES ("Sigma", "Ligma@gmail.com", "Balls555")

