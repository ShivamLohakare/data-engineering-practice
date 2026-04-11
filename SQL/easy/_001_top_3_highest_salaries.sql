-- Problem: Find top 3 highest salaries
-- Note: This problem can be interpreted in multiple ways

--------------------------------------------------
-- Approach 1: Top 3 employees (simple LIMIT)
--------------------------------------------------
SELECT employee_id, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

--------------------------------------------------
-- Approach 2: Top 3 DISTINCT salaries
--------------------------------------------------
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

--------------------------------------------------
-- Approach 3: Using DENSE_RANK (handles ties)
--------------------------------------------------
SELECT employee_id, salary
FROM (
    SELECT employee_id, salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employees
) t
WHERE rnk <= 3;

--------------------------------------------------
-- Learning:
-- LIMIT gives top rows
-- DISTINCT removes duplicates
-- DENSE_RANK handles real-world ranking scenarios