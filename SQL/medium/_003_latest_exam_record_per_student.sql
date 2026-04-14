-- =====================================================
-- Problem: Get Latest Exam Record per Student
-- =====================================================

-- Source: Practice
-- Level: Medium

-- Description:
-- Retrieve the most recent exam record for each student
-- based on exam_date.

-- =====================================================
-- Approach:
-- =====================================================
-- 1. Use ROW_NUMBER() window function
-- 2. Partition data by student_id
-- 3. Order records by exam_date in descending order
-- 4. Assign row number to each record within partition
-- 5. Filter records where row_number = 1 (latest record)

-- =====================================================
-- SQL Query:
-- =====================================================

SELECT 
    student_id,
    student_name,
    marks,
    exam_date
FROM (
    SELECT 
        student_id,
        student_name,
        marks,
        exam_date,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY exam_date DESC
        ) AS rn
    FROM exam_results
) t
WHERE rn = 1;

-- =====================================================
-- Alternative Approach (Using RANK)
-- =====================================================

-- This approach handles ties differently (if same exam_date exists)

SELECT 
    student_id,
    student_name,
    marks,
    exam_date
FROM (
    SELECT 
        student_id,
        student_name,
        marks,
        exam_date,
        RANK() OVER (
            PARTITION BY student_id
            ORDER BY exam_date DESC
        ) AS rnk
    FROM exam_results
) t
WHERE rnk = 1;

-- =====================================================
-- Learning:
-- =====================================================
-- - Learned ROW_NUMBER() window function
-- - Understood PARTITION BY for grouping data
-- - Used ORDER BY within window functions
-- - Extracted latest record per group

-- =====================================================
-- Notes:
-- =====================================================
-- - ROW_NUMBER() gives unique ranking (no duplicates)
-- - RANK() can return multiple rows if ties exist
-- - Useful in scenarios like latest transactions, logs, or updates