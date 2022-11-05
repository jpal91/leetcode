# Write your MySQL query statement below
SELECT COUNT(s.account_id) AS accounts_count
FROM subscriptions s
LEFT JOIN streams st
    ON s.account_id = st.account_id
WHERE YEAR(s.end_date) = 2021 AND YEAR(st.stream_date) != 2021
