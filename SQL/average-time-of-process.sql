# Write your MySQL query statement below
WITH cte1 AS (
    SELECT machine_id, process_id, timestamp
    FROM activity
    WHERE activity_type = 'start'
),

cte2 AS (
    SELECT machine_id, process_id, timestamp
    FROM activity
    WHERE activity_type = 'end'
)

SELECT c1.machine_id, ROUND(AVG(c2.timestamp - c1.timestamp), 3) AS processing_time
FROM cte1 c1
JOIN cte2 c2
    ON c1.machine_id = c2.machine_id
    AND c1.process_id = c2.process_id
GROUP BY c1.machine_id
