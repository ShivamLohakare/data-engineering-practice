"""
=====================================================
Problem: Customer Order Details using Multiple Joins
=====================================================

Source: Practice
Level: Medium

Description:
Join customer, orders, and order_items tables to extract
detailed order information including customer name,
product, quantity, and price.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Load customers, orders, and order_items tables
2. Join customers with orders using customer_id
3. Join result with order_items using order_id
4. Select relevant columns for final output

-----------------------------------------------------
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# =====================================================
# Initialize Spark Session
# =====================================================

spark = SparkSession.builder.appName("CustomerOrderDetails").getOrCreate()

# =====================================================
# Load Data
# =====================================================

df_customers = spark.table("customers")
df_orders = spark.table("orders")
df_order_items = spark.table("order_items")

# =====================================================
# Join Operations
# =====================================================

joined_df = (
    df_customers.alias("c")
    .join(df_orders.alias("o"), col("c.customer_id") == col("o.customer_id"), "inner")
    .join(df_order_items.alias("i"), col("o.order_id") == col("i.order_id"), "inner")
)

# =====================================================
# Select Required Columns
# =====================================================

result_df = joined_df.select(
    col("c.customer_name"),
    col("i.product"),
    col("i.quantity"),
    col("i.price")
)

# =====================================================
# Output
# =====================================================

result_df.show()


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Learned how to perform multiple joins in PySpark
- Understood use of alias() for handling column ambiguity
- Practiced selecting columns from joined DataFrames

-----------------------------------------------------
Best Practice:
-----------------------------------------------------
- Use aliases for readability in joins
- Chain joins for clean and readable code
- Avoid using generic variable names like df1

-----------------------------------------------------
Notes:
-----------------------------------------------------
- Inner join returns only matching records
- Ensure join keys (customer_id, order_id) are correctly indexed in real systems
"""