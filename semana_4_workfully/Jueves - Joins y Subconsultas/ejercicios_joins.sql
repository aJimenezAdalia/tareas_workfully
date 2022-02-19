

use hr;

/*
1. From the following tables, write a SQL query to find 
the first name, last name, department number, and department 
name for each employee.
- TABLES: departments, employees
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee, 
    d.department_id AS department_number, 
    d.department_name AS department_name
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
;
    

/*
2. From the following tables, write a SQL query to find 
the first name, last name, department, city, and state 
province for each employee.
- TABLES: departments, employees, locations
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee, 
    d.department_name AS department_name, 
    l.city AS city, 
    l.state_province AS state
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN locations AS l ON l.location_id = d.location_id;


/*
3. From the following table, write a SQL query to find the first name, 
last name, salary, and job grade for all employees.
- TABLES: employees, job_grades
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee, 
    e.salary AS salary, 
    j.job_title as job_grade 
FROM employees AS e
INNER JOIN jobs AS j
	ON e.salary BETWEEN j.min_salary AND j.max_salary;
	

/*
4. From the following tables, write a SQL query to find all those employees 
who work in department ID 80 or 40. Return first name, last name, department 
number and department name.
- TABLES: departments, employees
*/

SELECT
	CONCAT(e.first_name, " ", e.last_name) AS employee, 
    d.department_id AS department_id, 
    d.department_name AS department_name
FROM departments AS d
INNER JOIN employees AS e ON e.department_id = d.department_id
WHERE d.department_id IN (40, 80);


/*
5. From the following tables, write a SQL query to find those employees whose 
first name contains a letter ‘z’. Return first name, last name, department, city, and state province.
- TABLES: departments, employees, locations
*/

SELECT 
	e.first_name AS name, 
    e.last_name AS last_name, 
    d.department_name AS department_name, 
    l.city AS city, 
    l.state_province AS state
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN locations AS l ON l.location_id = d.location_id
WHERE e.first_name LIKE ("%z%");


/*
7. From the following table, write a SQL query to find those employees who earn less than the 
employee of ID 182. Return first name, last name and salary.
- TABLES: employees
*/

SELECT 
	CONCAT(first_name, " ", last_name) AS name, 
	salary
FROM employees
WHERE salary < (
	SELECT salary
    FROM employees
    WHERE employee_id = 182);


/*
8. From the following table, write a SQL query to find the employees and their managers. 
Return the first name of the employee and manager.
- TABLES: employees
*/

SELECT 
	e.first_name AS employee, 
    m.first_name AS manager
FROM employees AS e
INNER JOIN employees AS m ON e.manager_id = m.employee_id;


/*
9. From the following tables, write a SQL query to display the department name, city, and state province 
for each department.
- TABLES: departments, locations
*/

SELECT 
	d.department_name AS department_name, 
    l.city AS city, 
    l.state_province AS state
FROM departments AS d
INNER JOIN locations AS l ON l.location_id = d.location_id;


/*
10. From the following tables, write a SQL query to find those employees who have or not any department. 
Return first name, last name, department ID, department name.
- TABLES: departments, employees
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
    d.department_id AS department_id, 
    d.department_name AS department_name,
CASE
	WHEN d.department_name IS NULL THEN 'No'
    ELSE 'Yes'
END AS has_department
FROM departments AS d
INNER JOIN employees AS e ON e.department_id = d.department_id;


/*
11. From the following table, write a SQL query to find the employees and their managers. 
These managers do not work under any manager. Return the first name of the employee and manager. 
- TABLES: employees
*/

SELECT 
	e.first_name AS employee, 
    m.first_name AS manager
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.employee_id;


/*
12. From the following tables, write a SQL query to find those employees who work in a department 
where the employee of last name 'Taylor' works. Return first name, last name and department ID.
- TABLES: employees
*/

SELECT
	CONCAT(first_name, " ", last_name) AS employee, 
    department_id
FROM employees
WHERE department_id IN (
	SELECT department_id
    FROM employees
    WHERE UPPER(last_name) = "TAYLOR"); 


/*
13. From the following tables, write a SQL query to find those employees who joined on 1st January 1993 
and leave on or before 31 August 1997. Return job title, department name, employee name, and joining date of the job.
- TABLES: job_history, employees, jobs
*/

SELECT 
	j.job_title AS job_title,
    d.department_name AS department,
	CONCAT(e.first_name, " ", e.last_name) AS employee_name,
    jh.start_date AS joining_date
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN jobs AS j ON j.job_id = e.job_id
INNER JOIN job_history AS jh ON jh.department_id = d.department_id
WHERE jh.start_date = "1993-01-01" AND jh.end_date < "1997-08-31";


/*
14. From the following tables, write a SQL query to find the difference between maximum salary of the job 
and salary of the employees. Return job title, employee name, and salary difference.
- TABLES: employees, jobs
*/

SELECT
	j.job_title AS job_title, 
    CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
    (SELECT
		MAX(salary)
        FROM employees) - e.salary AS salary_difference
FROM employees AS e
INNER JOIN jobs AS j ON e.job_id = j.job_id
ORDER BY salary_difference ASC;


/*
15. From the following table, write a SQL query to compute the average salary, number of employees 
received commission in that department. Return department name, average salary and number of employees. 
- TABLES: employees, departments
*/

SELECT
	d.department_name AS department, 
    ROUND(AVG(e.salary)) AS average_salary, 
    (COUNT(DISTINCT(e.employee_id))) AS number_of_employees_commission
FROM departments AS d
INNER JOIN employees AS e ON e.department_id = d.department_id
WHERE e.commission_pct > 0
GROUP BY d.department_name
ORDER BY 3 DESC;


/*
16. From the following tables, write a SQL query to compute the difference between maximum salary and 
salary of all the employees who works the department of ID 80. Return job title, employee name and salary difference.
- TABLES: employees, jobs
*/

SELECT 
	j.job_title AS job_title, 
    CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
	- e.salary + (SELECT MAX(salary) 
				  FROM employees
				  WHERE department_id = 80) AS salary_difference
FROM employees AS e
INNER JOIN jobs AS j ON j.job_id = e.job_id
WHERE e.department_id = 80
ORDER BY salary_difference ASC;
    

/*
17. From the following table, write a SQL query to find the name of the country, city, 
and departments, which are running there.
- TABLES: countries, locations, departments
*/

SELECT 
	c.country_name AS country, 
    l.city AS city, 
    d.department_name AS department
FROM countries AS c
INNER JOIN locations AS l ON l.country_id = c.country_id
INNER JOIN departments AS d ON l.location_id = d.location_id
ORDER BY country, city;


/*
18. From the following tables, write a SQL query to find the department name and the 
full name (first and last name) of the manager.
- TABLES: departments, employees
*/

SELECT
	CONCAT(e.first_name, " ", e.last_name) AS name, 
    d.department_name AS department
FROM employees AS e
INNER JOIN departments AS d ON d.manager_id = e.employee_id;


/*
19. From the following table, write a SQL query to compute the average salary of employees for each job title.
- TABLES: employees, jobs
*/

SELECT
	j.job_title AS job_title, 
    ROUND(AVG(e.salary)) AS avg_salary
FROM jobs AS j
INNER JOIN employees AS e ON e.job_id = j.job_id
GROUP BY job_title
ORDER BY avg_salary DESC;


/*
20. From the following table, write a SQL query to find those employees who earn $12000 and above. 
Return employee ID, starting date, end date, job ID and department ID. 
- TABLES: employees, job_history
*/
	
SELECT 
	e.employee_id AS employee_id, 
    j.start_date AS starting_date, 
    j.end_date AS end_date, 
    e.job_id AS job_id, 
    e.department_id AS department_id
FROM employees AS e
INNER JOIN job_history AS j ON e.department_id = j.department_id
WHERE e.salary > 12000;    


/*
21. From the following tables, write a SQL query to find those departments where at least 2 employees work. 
Group the result set on country name and city. Return country name, city, and number of departments. 
- TABLES: countries, locations, employees, departments
*/

SELECT
	c.country_name AS country, 
    l.city AS city, 
    COUNT(DISTINCT(d.department_id)) AS number_of_departments
FROM countries AS c
INNER JOIN locations AS l ON l.country_id = c.country_id
INNER JOIN departments AS d ON d.location_id = l.location_id
INNER JOIN employees AS e ON e.department_id = d.department_id
WHERE d.department_id IN (
	SELECT 
		DISTINCT(department_id) AS dept_id
	FROM employees
	GROUP BY 1
	HAVING COUNT(employee_id) > 1)
GROUP BY country, city;


/*
22. From the following tables, write a SQL query to find the department name, full name 
(first and last name) of the manager and their city. 
- TABLES: employees, locations, departments
*/

SELECT 
	d.department_name AS department_name, 
    CONCAT(e.first_name, " ", e.last_name) AS manager_name, 
    l.city AS city
FROM departments AS d
INNER JOIN employees AS e ON d.manager_id = e.employee_id
INNER JOIN locations AS l ON l.location_id = d.location_id;


/*
23. From the following tables, write a SQL query to compute the number of days worked by employees 
in a department of ID 80. Return employee ID, job title, number of days worked.
- TABLES: jobs, job_history
*/

SELECT
	jh.employee_id AS employee_id, 
    j.job_title AS job_title, 
    jh.end_date - jh.start_date AS days_worked
FROM job_history AS jh
INNER JOIN jobs AS j ON j.job_id = jh.job_id
WHERE jh.department_id = 80;


/*
24. From the following tables, write a SQL query to find full name (first and last name), 
and salary of those employees who work in any department located in 'London' city.
- TABLES: departments, locations, employees
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee, 
    e.salary AS salary, 
    l.city AS city
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN locations AS l ON l.location_id = d.location_id
WHERE d.department_id IN (
	SELECT 
		DISTINCT(d.department_id) AS dept_id 
	FROM departments AS d
	INNER JOIN locations AS l ON l.location_id = d.location_id
	WHERE UPPER(l.city) = 'LONDON');
    

/*
25. From the following tables, write a SQL query to find full name (first and last name), job title, 
starting and ending date of last jobs of employees who worked without a commission percentage.
- TABLES: jobs, job_history, employees
*/
    
SELECT 
	DISTINCT(CONCAT(e.first_name, " ", e.last_name)) AS employee_name, 
    j.job_title AS job_title, 
    MAX(jh.start_date) AS starting_date, 
    MAX(jh.end_date) AS end_date
FROM employees AS e
INNER JOIN job_history AS jh ON jh.department_id = e.department_id
INNER JOIN jobs AS j ON j.job_id = jh.job_id
WHERE e.commission_pct IS NULL
GROUP BY employee_name, job_title;


/*
26. From the following tables, write a SQL query to find the department name, 
department ID, and number of employees in each department.
- TABLES: departments, employees
*/

SELECT 
	d.department_name AS department, 
    d.department_id AS department_id, 
    COUNT(DISTINCT(e.employee_id)) AS empl_number
FROM departments AS d
INNER JOIN employees AS e ON e.department_id = d.department_id
GROUP BY 1, 2
ORDER BY 3;


/*
27. From the following tables, write a SQL query to find the full name (first and last name) 
of the employee with ID and name of the country presently where he/she is working.
- TABLES: countries, locations, departments, employees
*/

SELECT 
	CONCAT(e.first_name, " ", e.last_name) AS employee_name, 
    e.employee_id AS employee_id, 
    c.country_name AS country
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN locations AS l ON d.location_id = l.location_id
INNER JOIN countries AS c ON l.country_id = c.country_id
ORDER BY 3;




