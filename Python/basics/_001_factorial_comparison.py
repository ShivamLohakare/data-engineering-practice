"""
=====================================================
Problem: Factorial of a Number (Recursive vs Iterative)
=====================================================

Source: Practice
Level: Easy

Description:
Calculate the factorial of a number using both recursive
and iterative approaches, and compare their behavior.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Recursive Approach:
   - Function calls itself until base condition is met
   - Uses call stack

2. Iterative Approach:
   - Uses loop to calculate factorial
   - More memory efficient

-----------------------------------------------------
"""

# =====================================================
# Recursive Approach
# =====================================================

def factorial_recursive(n):
    if n < 0:
        return "Not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# =====================================================
# Iterative Approach
# =====================================================

def factorial_iterative(n):
    if n < 0:
        return "Not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


# =====================================================
# Example Usage
# =====================================================

num = 5

print(f"Recursive: Factorial of {num} is {factorial_recursive(num)}")
print(f"Iterative: Factorial of {num} is {factorial_iterative(num)}")


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Recursion is easy to understand but uses extra memory
- Iteration is more efficient and avoids stack overflow
- Both approaches solve the same problem differently

-----------------------------------------------------
Best Approach:
-----------------------------------------------------
- Iterative approach is preferred in production due to:
  ✔ Lower memory usage
  ✔ Better performance for large inputs
  ✔ No risk of stack overflow

-----------------------------------------------------
Notes:
-----------------------------------------------------
- Recursion is useful for problems like trees and graphs
- Iteration is better for simple repetitive calculations
"""