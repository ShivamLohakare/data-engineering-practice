-- =====================================================
-- Problem: Find Customers with Total Order Amount > 6000
-- =====================================================

-- Source: Practice
-- Level: Medium

-- Description:
-- Identify customers whose total order amount exceeds 6000.
-- This involves joining customer and order data, aggregating
-- order amounts, and filtering based on total spend.

-- =====================================================
-- Approach:
-- =====================================================
-- 1. Join customer and orders tables using customer_id
-- 2. Group records by customer_id and customer_name
-- 3. Calculate total order amount using SUM()
-- 4. Filter results using HAVING clause

-- =====================================================
-- SQL Query:
-- =====================================================

SELECT 
    t1.customer_id,
    t1.customer_name,
    SUM(t2.order_amount) AS total_order_amount
FROM customer t1
JOIN orders t2 
    ON t1.customer_id = t2.customer_id
GROUP BY 
    t1.customer_id, 
    t1.customer_name
HAVING SUM(t2.order_amount) > 6000;

-- =====================================================
-- Alternative Approach (Using CTE)
-- =====================================================

WITH customer_totals AS (
    SELECT 
        t1.customer_id,
        t1.customer_name,
        SUM(t2.order_amount) AS total_order_amount
    FROM customer t1
    JOIN orders t2 
        ON t1.customer_id = t2.customer_id
    GROUP BY 
        t1.customer_id, 
        t1.customer_name
)

SELECT *
FROM customer_totals
WHERE total_order_amount > 6000;

-- =====================================================
-- Learning:
-- =====================================================
-- - Understood JOIN operation between tables
-- - Learned GROUP BY with multiple columns
-- - Used HAVING clause for filtering aggregated data
-- - Practiced using CTE for cleaner query structure

-- =====================================================
-- Notes:
-- =====================================================
-- - HAVING is used instead of WHERE for aggregated conditions
-- - Ensure all selected non-aggregated columns are included in GROUP BY