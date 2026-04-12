"""
=====================================================
Problem: Filter Employees by Department
=====================================================

Source: Practice
Level: Easy

Description:
Filter employee records where department is 'IT'
from a given dataset using PySpark.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Load data from Spark table
2. Apply filter condition on department column
3. Display the filtered result

-----------------------------------------------------
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("FilterDepartment").getOrCreate()

# Load Data
df = spark.table("employees")

# Apply Filter
filtered_df = df.filter(col("department") == "IT")

# Show Result
filtered_df.show()


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Learned how to filter data using PySpark DataFrame API
- Understood usage of col() function for column operations

-----------------------------------------------------
Notes:
-----------------------------------------------------
- spark.table() assumes table is registered in Spark catalog
- Alternative: spark.read.csv() or parquet() for external data
"""