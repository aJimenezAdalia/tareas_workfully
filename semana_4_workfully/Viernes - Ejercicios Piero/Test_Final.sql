

use hr;

/*
Muestre los nombres y apellidos (es una sola columna), nombre del departamento y el nombre del puesto de 
todos los empleados cuyo código de ubicación de departamento (LOCATION_ID) es 1700. 
El resultado del reporte debe mostrarse en orden ascendente por el apellido del empleado.
*/

SELECT
	CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
    d.department_name AS department_name, 
    j.job_title AS job_name, 
    d.location_id AS location_id
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN jobs AS j ON e.job_id = j.job_id
WHERE d.location_id = 1700;


/*
Generar un reporte que muestre la cantidad de empleados que ingresaron en cada año, 
el costo del salario mensual, anual y el salario promedio por cada año.
*/

SELECT
	DISTINCT(YEAR(jh.start_date)) AS year, 
    COUNT(jh.employee_id) AS total_hires, 
	ROUND(SUM(e.salary)) AS total_salary_cost, 
    ROUND(AVG(e.salary)) AS average_salary
FROM job_history AS jh
INNER JOIN employees AS e ON e.job_id = jh.job_id
GROUP BY 1
ORDER BY 1;


/*
Desarrolle una consulta donde muestre el código de empleado, el apellido, salario, nombre de región, nombre de país,
estado de la provincia , código de departamento, nombre de departamento donde cumpla las siguientes condiciones:
a. Que los empleados que seleccione su salario sea mayor al promedio de su departamento.
b. Que no seleccione los del estado de la provincia de Texas
c. Que ordene la información por código de empleado ascendentemente.
d. Que no escoja los del departamento de finanzas (Finance)
*/

SELECT
	e.employee_id AS employee_id, 
    e.last_name AS last_name, 
    e.salary AS salary, 
    r.region_name AS region_name, 
    c.country_name AS country, 
    l.state_province AS state_province, 
    d.department_id AS department_id, 
    d.department_name AS department
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN locations AS l ON d.location_id = l.location_id
INNER JOIN countries AS c ON c.country_id = l.country_id
INNER JOIN regions AS r ON r.region_id = c.region_id
WHERE
	e.salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id)
	AND UPPER(l.state_province) <> 'TEXAS' 
    AND UPPER(d.department_name) <> 'FINANCE'
ORDER BY 1 ASC;
	
    
/*
Generar un reporte que muestre los nombres y apellidos, salario del empleado, el salario mínimo 
según el cargo del empleado, de aquellos cuya diferencia del salario y el salario mínimo sea menor a $500
y además que indique si merece un aumento sólo si la diferencia entre hoy y la fecha de contratación es mayor 
a 5,000 días. El mismo reporte debe mostrar el nuevo salario que corresponde a un aumento del 15% .
*/

SELECT
	CASE
		WHEN (jh.end_date - jh.start_date) > 5000 THEN 'Yes'
        ELSE 'No'
        END AS Deserves_salary_raise, 
	CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
    e.salary AS salary, 
    (	
	SELECT MIN(salary)
	FROM employees
	WHERE job_id = e.job_id
	) AS minimum_jobID_salary, 
	e.salary - (
				SELECT(MIN(salary))
				FROM employees
                WHERE job_id = e.job_id
                ) AS difference, 
	CASE
		WHEN (jh.end_date - jh.start_date) > 5000 THEN e.salary + (0.15 * e.salary)
        ELSE e.salary
        END AS New_salary
FROM job_history AS jh 
INNER JOIN employees AS e ON e.department_id = jh.department_id
WHERE e.salary - (
				 SELECT(MIN(salary))
				 FROM employees
				 WHERE job_id = e.job_id
                 ) < 500
ORDER BY 5;
	





