
/****************************************************
APARTADO 1: Muestra los clientes de brasil
****************************************************/
SELECT CONCAT(FirstName, " ", LastName) AS customer_name, country
FROM customer
WHERE Country = "Brazil";

/****************************************************
APARTADO 2: Muestrame los empleados que son agentes de ventas
****************************************************/
SELECT CONCAT(FirstName, " ", LastName) as employee_name, title
FROM employee
WHERE title = "Sales Support Agent";

/****************************************************
APARTADO 3: Muestrame las canciones de AC/DC
****************************************************/
SELECT t.Name AS track_name, ar.Name as artist_name
FROM track as t
INNER JOIN album as a ON t.albumid = a.albumid
INNER JOIN artist as ar ON ar.artistid = a.albumid
WHERE ar.Name = "AC/DC"; 

/****************************************************
APARTADO 4: Muestra los clientes que no sean de USA: Nombre completo, ID, Pais
****************************************************/
SELECT CONCAT(FirstName, " ", LastName) as customer_name, CustomerId, country
FROM customer
WHERE country NOT IN ("USA");

/****************************************************
APARTADO 5: Muestrame los empleados que son agentes de ventas: Nombre completo, Dirección
(Ciudad, Estado, Pais) y email
****************************************************/
SELECT CONCAT(FirstName, " ", LastName) as employee_name, title, 
	   CONCAT(city,", ",state,", ",country) as address, email
FROM employee
WHERE title = "Sales Support Agent";

/****************************************************
APARTADO 6: Muestra una lista con los paises que aparecen a los que se ha facturado, la lista no
debe contener paises repetidos
****************************************************/
select distinct billingcountry 
from invoice;

/****************************************************
APARTADO 7: Muestra una lista con los estados de USA de donde son los clientes, la lista no debe
contener estados repetidos
****************************************************/
select distinct billingstate
from invoice
WHERE billingcountry = "USA";

/****************************************************
APARTADO 8: Cuantos articulos tiene la factura 37
****************************************************/
select 
    sum(quantity) as article_number
from
    invoiceline
where
    invoiceid = 37;

/****************************************************
APARTADO 9: Cuantas canciones tiene AC/DC
****************************************************/
select count(t.trackid)
from track as t
inner join album as a on a.albumid=t.albumid
inner join artist as ar on ar.artistid=a.artistid
where ar.name = "AC/DC";

/****************************************************
APARTADO 10: Cuantos articulos tiene cada factura
****************************************************/
select invoiceid, sum(quantity)
from invoiceline
group by invoiceid;

/****************************************************
APARTADO 11: Muestrame cuantos facturas hay de cada pais
****************************************************/
select count(invoiceid) as total, billingcountry
from invoice
group by billingcountry
order by total desc;

/****************************************************
APARTADO 12: Cuantas facturas ha habido en 2009 y 2011
****************************************************/
select count(invoiceid)
from invoice
where year(invoicedate) IN (2009, 2011);

/****************************************************
APARTADO 13: Cuantos clientes hay de españa y de Brazil
****************************************************/
select country, count(customerid)
from customer
where country in ("Spain", "Brazil")
group by country;

/****************************************************
APARTADO 14: Muestrame las canciones que su titulo empieza por ‘You’
****************************************************/
select name
from track
where name like ("You%");
