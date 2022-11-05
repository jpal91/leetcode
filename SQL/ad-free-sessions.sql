# Write your MySQL query statement below
SELECT p.session_id
FROM playback p
LEFT JOIN ads a
    ON a.customer_id = p.customer_id
    AND a.timestamp BETWEEN start_time AND end_time
WHERE a.customer_id IS NULL
