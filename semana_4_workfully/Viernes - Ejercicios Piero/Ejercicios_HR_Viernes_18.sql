
USE hr;

/*
1. Because of budget issues, the HR department needs a report that displays the 
last name and salary of employees earning more than $12,000.
*/
SELECT last_name, salary
FROM employees 
WHERE salary > 12000;


/*
2. The HR department needs to find high-salary and low-salary employees. Display the last name and salary 
for all employees whose salary is not in the range $5,000 through $12,000.
*/

SELECT
	last_name, 
    salary
FROM employees
WHERE salary NOT BETWEEN 5000 AND 12000
ORDER BY 2 ASC;


/*
3. Display the last name, job ID, and hire date for employees with the last names of Matos and Taylor. 
Order the query in ascending order by hire date
*/

SELECT
	e.last_name AS last_name, 
    e.job_id AS job_id, 
    jh.start_date AS hire_date
FROM employees AS e
INNER JOIN job_history AS jh ON jh.job_id = e.job_id
WHERE UPPER(last_name) IN ("MATOS", "TAYLOR")
ORDER BY 3 ASC;


/*
4. Display the last name, salary, and commission for all employees who earn commissions (comission_pct). 
Sort data in descending order of salary and commissions. Use the column’s numeric position in the ORDER BY clause.
*/

SELECT 
	last_name, 
    salary, 
    commission_pct
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY 2, 3 DESC;


/*
5. Display the manager number and the salary of the lowest-paid employee 
for that manager. Exclude anyone whose manager is not known. 
Exclude any groups where the minimum salary is $6,000 or less. 
Sort the output in descending order of salary. 
*/

SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id IS NOT NULL 
GROUP BY manager_id
HAVING MIN(salary) > 6000
ORDER BY MIN(salary) DESC;


/*
6. The HR department needs a report of employees in Toronto. Display the last name, job, 
department number, and department name for all employees who work in Toronto.
*/

SELECT
	e.last_name AS last_name, 
    j.job_title AS job, 
    e.department_id AS department_number, 
    d.department_name AS department_name, 
    l.city AS city
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
INNER JOIN jobs AS j ON j.job_id = e.job_id
INNER JOIN locations AS l ON l.location_id = d.location_id
WHERE UPPER(l.city) = 'TORONTO'; 


/*
7. Display employee last names, department numbers, and all 
the employees who work in the same department as a given employee. 
Give each column an appropriate label. 
*/

SELECT 
    department_id, 
    COUNT(employee_id) AS department_workers
FROM employees
GROUP BY department_id;

/*
8. Display the employee number, last name, and salary of all 
employees who earn more than the average salary. Sort the results 
in order of ascending salary.
*/

SELECT employee_id, last_name, salary
FROM employees
WHERE salary > 
	(SELECT AVG(salary)
    FROM employees)
ORDER BY salary ASC;





