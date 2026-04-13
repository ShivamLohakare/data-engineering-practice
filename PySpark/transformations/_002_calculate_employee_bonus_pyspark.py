"""
=====================================================
Problem: Calculate Employee Bonus
=====================================================

Source: Practice
Level: Easy–Medium

Description:
Calculate a 10% bonus for each employee based on their salary
and display employee name along with bonus amount.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Load employee data from Spark table
2. Create a new column 'bonus_amount' using withColumn()
3. Calculate bonus as 10% of salary
4. Select required columns for output

-----------------------------------------------------
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# =====================================================
# Initialize Spark Session
# =====================================================

spark = SparkSession.builder.appName("EmployeeBonusCalculation").getOrCreate()

# =====================================================
# Load Data
# =====================================================

df = spark.table("employees")

# =====================================================
# Transformation Logic
# =====================================================

result_df = (
    df.withColumn("bonus_amount", col("salary") * 0.1)
      .select("emp_name", "bonus_amount")
)

# =====================================================
# Output
# =====================================================

result_df.show()


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Learned how to create new columns using withColumn()
- Understood column expressions using col()
- Practiced selecting specific columns from DataFrame

-----------------------------------------------------
Best Practice:
-----------------------------------------------------
- Use meaningful variable names (result_df instead of df1)
- Chain transformations for better readability

-----------------------------------------------------
Notes:
-----------------------------------------------------
- spark.table() assumes table exists in Spark catalog
- Bonus percentage can be parameterized for flexibility
"""