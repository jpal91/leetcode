# Write your MySQL query statement below
SELECT s.seller_name
FROM seller s
LEFT JOIN orders o
    ON s.seller_id = o.seller_id
GROUP BY s.seller_name
HAVING SUM(CASE WHEN YEAR(o.sale_date) = 2020 THEN 1 ELSE 0 END) = 0
ORDER BY s.seller_name
