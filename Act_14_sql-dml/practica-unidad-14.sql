-- use SQL_DML;
-- GO

-- Listar nombres de proveedores, donde ciudad contenga "Ramos"
select p.Nombre
from Proveedor p
where p.Ciudad LIKE '%Ramos%';

-- Listar codigos de materiales que provea el proveedor 4 y no los provea el proveedor 5(resolver de 3 formas)
-- 1
select pp.CodMat
from Provisto_Por pp
where pp.CodProv = 4 and pp.CodMat not in (select CodMat from Provisto_Por where CodProv = 5);
-- 2
select pp.CodMat
from Provisto_Por pp
where pp.CodProv = 4 and not exists (select CodMat from Provisto_Por where CodProv = 5 and pp.CodMat = CodMat);
--3
select pp.CodMat
from Provisto_Por pp
where pp.CodProv = 4
except
select CodMat
from Provisto_Por
where CodProv = 5;

-- Listar materiales, codigo y descripcion provistos por proveedores de Ramos Mejía.
select m.CodMat, m.Descripcion
from Material m join Provisto_Por pp on (m.CodMat = pp.CodMat)
join Proveedor p on (pp.CodProv = p.CodProv)
where p.Ciudad like '%Ramos%';
-- listo todos proveedores y el de ramos no coincide con ningun material
select * from Provisto_Por pp full outer join Proveedor p on (pp.CodProv = p.CodProv);

-- Listar proveedores y materiales
select p.Nombre as Proveedor,
p.Ciudad,
m.Descripcion as Material
from Proveedor p left join Provisto_Por pp on (p.CodProv = pp.CodProv)
left join Material m on (pp.CodMat = m.CodMat);

-- Listar articulos que cuestemas mas de 30 o esten compuestos por el material 2
select distinct a.Descripcion as Articulos, 
a.Precio
from Articulo a join Compuesto_Por cp on (a.CodArt = cp.CodArt)
where a.Precio > 30 or cp.CodMat = 2;

-- Listar articlos de mayor precio
select TOP 5 a.precio,
a.Descripcion as nombre
from Articulo a
order by a.Precio desc;

-- Listar proveedores con mas de tres materiales
select p.CodProv as Codigo_Provincia,
count(pp.CodMat) as materiales
from Proveedor p join Provisto_Por pp on (p.CodProv = pp.CodProv)
group by p.CodProv
having count(pp.CodMat) > 3
order by p.CodProv;

-- Crear Vista para proveedores que provean mas de 4 materiales
create view [codProv CodMat] as
select p.CodProv as Provincia,
count(pp.CodMat) as Cantidad
from Proveedor p join Provisto_Por pp on (p.CodProv = pp.CodProv)
group by p.CodProv
having count(pp.CodMat) > 4
-- llamar a la vista
select * 
from [codProv CodMat];
