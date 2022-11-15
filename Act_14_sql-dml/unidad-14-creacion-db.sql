-- SELECCIONAR DESDE ESTE PUNTO
-- Creación de la base de datos
create database SQL_DML;
GO
--creación de las tablas
use SQL_DML;
GO
create table Almacen (Nro int primary key, Responsable varchar(50))
create table Articulo (CodArt int primary key, Descripcion varchar(50),
Precio decimal(12, 3))
create table Material (CodMat int primary key, Descripcion
varchar(50))
create table Proveedor (CodProv int primary key, Nombre varchar(50),
Domicilio varchar(50), Ciudad varchar(50), fecha_alta date)
create table Tiene (NroAlmacen int foreign key references
almacen(Nro), CodArt int foreign key references articulo(codArt))
create table Compuesto_Por (CodArt int foreign key references
articulo(codArt), CodMat int foreign key references material(codMat))
create table Provisto_Por (CodMat int foreign key references
material(codMat), CodProv int foreign key references
proveedor(codProv))
GO

-- carga de datos
insert into Almacen values (1, 'Juan Perez'), (2, 'Jose Basualdo'), (3,
'Pablo Mancineli'), (4, 'Rogelio Funes Mori'), (5, 'Jonathan Maidana'), (6,
'Anita Martinez'), (7, 'Patricio Gonzalez'), (8, 'Diego Salaberry')
insert into Articulo values (1, 'Articulo Uno', 60), (2, 'Articulo Dos', 60),
(3, 'Articulo Tres', 180), (4, 'Articulo Cuatro', 250), (5, 'Articulo Cinco',
350), (6, 'Articulo Seis', 450), (7, 'Articulo Siete', 650), (8, 'Articulo Ocho',
850), (9, 'Articulo Nueve', 1250)
insert into Material values (1, 'Material A'), (2, 'Material B'), (3, 'Material
C'), (4, 'Material D'), (5, 'Material E'), (6, 'Material F'), (7, 'Material G'), (8,
'Material H'), (9, 'Material I'), (10, 'Material J'), (11, 'Material K'), (12,
'Material L'), (13, 'Material M'), (14, 'Material P')

insert into Proveedor values
(1, 'Proveedor Uno', 'Carlos Calvo 1212', 'CABA','01-01-1990'),
(2, 'Proveedor Dos', 'San Martin 121', 'Pergamino','01-01-1990'),
(3, 'Proveedor Tres', 'San Pedrito 1244', 'CABA','01-01-1992'),
(4, 'Proveedor Cuatro', 'Av. Boedo 3232', 'CABA','01-01-1993'),
(5, 'Proveedor Cinco', '5 3232', 'La Plata','01-01-1994'),
(6, 'Proveedor Seis', 'Av 7 287', 'La Plata','01-01-1995'),
(7, 'Proveedor Siete', 'Italia 954', 'San Fernando','01-01-1996'),
(8, 'Proveedor Ocho', 'María de Carmen 765', 'San Fernando del Valle
de Catamarca','01-01-1997'),


(9, 'Proveedor Nueve', 'Av Corrientes 1200', 'Corrientes
Capital','01-01-1998'),
(10, 'Proveedor Diez', 'Av Juan Manuel de Rosas', 'San
Justo','01-01-1999'),
(11, 'Proveedor Once', 'Av Marite García 220', 'Ramos
Mejía','01-01-1990'),
(12, 'Proveedor Doce', 'La Plata 343', 'Ciudadela','01-01-2007'),
(13, 'Proveedor Trece', 'Independencia 1343', 'Mar del
Plata','01-01-2008'),
(14, 'Proveedor Catorce', 'Varela 343', 'San Justo','01-01-2009'),
(15, 'Proveedor Quince', 'Santander 943', 'Ituzaingó','01-01-2010')

insert into Tiene values (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2),
(3, 3), (3, 4), (4, 1), (4, 3), (4, 5), (4, 8), (5, 2), (5, 7), (5, 8), (5, 9), (8, 1), (8, 2),
(8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9)

insert into Compuesto_Por values (1, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 1), (3,
6), (4, 1), (4, 6), (4, 7), (4, 8), (9,12)
insert into Provisto_Por values (1, 1), (1, 3), (1, 6), (2, 2), (2, 3), (2, 4),(2, 6),
(3, 2), (3, 3),(3, 6), (4, 3), (4, 4),(4, 6), (5, 1), (5, 3),(5, 6), (6, 3), (6, 4),(6, 6),
(7, 3), (7, 5),(7, 6), (8, 3), (8, 5), (8, 6),(8, 10),(8, 15), (9, 6),(10, 6),(11, 6),(12,
6),(13, 6),(13, 10), (14, 10),(14, 6),(14, 15)

-- SELECCIONAR HASTA ESTE PUNTO