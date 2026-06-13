-- Write your query below

SELECT employee_id, 
case 
    when employee_id % 2 <> 0 AND name NOT LIKE 'M%' THEN salary 
    else 0
END bonus
FROM employees
ORDER BY employee_id