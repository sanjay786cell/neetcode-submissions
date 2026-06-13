-- Write your query below

select name FROM customers where id not in (select customer_id
FROM orders)

