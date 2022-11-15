-- Practica DDL
CREATE DATABASE practica_13;
GO
USE practica_13;
GO

CREATE TABLE Alumno(
	legajo INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(80) DEFAULT 'NN',
	apellido VARCHAR(80) DEFAULT 'NN',
	fecha_nac date
);
GO

CREATE TABLE Materia(
	cod_mat INT IDENTITY(1,1) PRIMARY KEY,
	descripcion VARCHAR(200) DEFAULT 'Sin Descripcion'
);
GO

CREATE TABLE Cursa(
	cod_cursa INT IDENTITY(1,1) PRIMARY KEY,
	legajo INT FOREIGN KEY REFERENCES Alumno(legajo),
	cod_mat INT FOREIGN KEY REFERENCES Materia(cod_mat)
);
GO

-- A Continuación voy a insertar datos en las tablas
-- Alumno
INSERT INTO Alumno 
VALUES('Pepito', 'Pepito', '1990-06-21'),
('Honguito', 'Pepito', '1970-06-30'),
('Mengano', 'Pepito', '1982-02-20'),
('SUltano', 'Pepito', '1998-11-21'),
('Fulano', 'Pepito', '2002-12-31');
GO
-- Materia
INSERT INTO Materia 
VALUES('Descripcion-1'),
('Descripcion-2'),
('Descripcion-3'),
('Descripcion-4'),
('Descripcion-5');
GO
-- Cursa
INSERT INTO Cursa 
VALUES(1,1),
(2,5),
(3,2),
(1,2),
(4,4);
GO

-- Por ultimo exporto el script y luego borro la DB para crearla desde el script