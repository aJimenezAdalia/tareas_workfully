

USE chinook;
/****************************************************
APARTADO 1: Facturas de Clientes de Brasil
****************************************************/
SELECT COUNT(total)
FROM invoice
WHERE billingcountry = "Brazil";

/****************************************************
APARTADO 2: Muestra cada factura asociada a cada agente de ventas con su nombre completo
****************************************************/
SELECT 
	CONCAT(e.firstname, " ", e.lastname) AS employee_name, 
    i.invoiceid as invoice_id
FROM invoice AS i
INNER JOIN customer AS c ON c.customerid = i.customerid
INNER JOIN employee AS e ON e.employeeid = c.supportrepid;

/****************************************************
APARTADO 3: Muestra el nombre del cliente, el pais, el nombre del agente y el total
****************************************************/
SELECT 
	CONCAT(c.firstname, " ", c.lastname) AS customer_name, 
    c.country AS customer_country, 
    CONCAT(e.firstname, " ", e.lastname) AS employee_name,
    SUM(i.total) AS total
FROM invoice AS i
INNER JOIN customer AS c ON c.customerid = i.invoiceid
INNER JOIN employee AS e ON e.employeeid = c.supportrepid
GROUP BY customer_name, customer_country, employee_name
ORDER BY total DESC;

/****************************************************
APARTADO 4: Muestra cada articulo de la factura con el nombre de la cancion
****************************************************/
SELECT 
	il.invoiceid AS invoice_id, 
    t.name AS track_name
FROM invoiceline AS il
INNER JOIN track AS t ON t.TrackId = il.trackid;

/****************************************************
APARTADO 5: Muestra todas las canciones con su nombre, formato, album y genero
****************************************************/
SELECT 
	t.name AS track_name, 
    m.name AS track_format, 
    al.title AS album_title, 
    g.name AS genre
FROM genre AS g
INNER JOIN track AS t ON g.genreid = t.genreid
INNER JOIN album AS al ON al.albumid = t.albumid
INNER JOIN mediatype AS m ON m.mediatypeid = t.mediatypeid;

/****************************************************
APARTADO 6: Muestra cuantas canciones hay en cada playlist y el nombre de cada playlist
****************************************************/
SELECT 
	pl.name AS playlist_name,
	COUNT(pt.trackid) AS track_count
FROM playlist AS pl
INNER JOIN playlisttrack AS pt ON pt.playlistid = pl.playlistid
GROUP BY playlist_name
ORDER BY track_count DESC;
    
/****************************************************
APARTADO 7: Muestra cuánto (Quantity) ha vendido cada empleado
****************************************************/
SELECT
	CONCAT(e.firstname, " ", e.lastname) AS employee, 
    SUM(i.total) AS total_sales
FROM invoice AS i
INNER JOIN customer AS c ON i.customerid = c.customerid
INNER JOIN employee AS e ON c.supportrepid = e.employeeid
GROUP BY employee
ORDER BY total_sales DESC;

/****************************************************
APARTADO 8: Quien ha sido el agente de ventas que más ha vendido en 2009?
****************************************************/
SELECT
	CONCAT(e.firstname, " ", e.lastname) AS employee, 
    SUM(i.total) AS total_sales
FROM invoice AS i
INNER JOIN customer AS c ON i.customerid = c.customerid
INNER JOIN employee AS e ON c.supportrepid = e.employeeid
WHERE YEAR(i.invoicedate) = 2009
GROUP BY employee
ORDER BY total_sales DESC
LIMIT 1;

/****************************************************
APARTADO 9: Quien es son los 3 grupos que más han vendido (Quantity)?
****************************************************/
SELECT 
	ar.name AS artist_name, 
    COUNT(il.quantity) AS quantity
FROM invoiceline AS il 
INNER JOIN track AS t ON il.trackid = t.trackid
INNER JOIN album AS al ON al.albumid = t.albumid
INNER JOIN artist AS ar On ar.artistid = al.artistid
GROUP BY artist_name
ORDER BY quantity DESC
LIMIT 3;
