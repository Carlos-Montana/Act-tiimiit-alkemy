-- En esta parte del codigo creo una base de datos de practica 
-- para conectarme con sqlalchemy

-- ## EN CONSOLA ##
-- # DCL(data control lenguage)
-- # Creando users y roles
-- create user develop;
-- # asignandole rol al nuevo user
-- alter role test createdb;
-- \du --> para ver los usuarios y roles

-- ## EN DBEAVER O PGADMIN
-- DDL(data definition lenguage)
-- create database test;
-- # Como saber en db y user nos encontramos
-- select current_database(), session_user;  

create table customer (
	id serial primary key,
	name TEXT,
	age INTEGER,
	email CHARACTER(255),
	address CHARACTER(400),
	zip_code CHARACTER(20)
);

-- DML(data manipulation lenguage)
INSERT INTO customer(name,age,email,address,zip_code)
VALUES
('Paul',23,'paul@gmail.com','address from paul','2321LL'),
('Felipe',32,'felipegarcia@gmail.com','address from felipe','3413MS'),
('Teddy',90,'teddy@gmail.com','address from teddy','3423PO'),
('Mark',17,'mark@gmail.com','address from mark','9423MA'),
('David',35,'david@gmail.com','address from david','2341DA'),
('Allen',56,'allen@gmail.com','address from allen','3423PO'),
('James',56,'james@gmail.com','address from james','3423PO');



