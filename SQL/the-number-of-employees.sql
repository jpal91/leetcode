# Write your MySQL query statement below
SELECT a.employee_id, a.name, COUNT(b.name) AS reports_count, ROUND(AVG(b.age)) AS 
    average_age
FROM employees a
RIGHT JOIN employees b
    ON b.reports_to = a.employee_id
WHERE a.employee_id IS NOT NULL
GROUP BY a.employee_id
ORDER BY a.employee_id
