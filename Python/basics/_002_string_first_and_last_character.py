"""
=====================================================
Problem: Print First and Last Character of a String
=====================================================

Source: Practice
Level: Easy

Description:
Given a string, print its first and last character.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Direct Indexing:
   - First character → string[0]
   - Last character → string[-1] OR string[len(string)-1]

2. Iterative Approach:
   - Loop through string and keep updating variable
   - Last value becomes last character (inefficient)

-----------------------------------------------------
"""

# =====================================================
# Input
# =====================================================

name = "Shivam"

# =====================================================
# Approach 1: Direct Indexing (Best Practice)
# =====================================================

first_char = name[0]
last_char = name[-1]   # preferred

print("First Character:", first_char)
print("Last Character:", last_char)


# =====================================================
# Approach 2: Using Loop (Not Recommended)
# =====================================================

last_char_loop = ""

for char in name:
    last_char_loop = char

print("Last Character (Loop Method):", last_char_loop)


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Learned string indexing in Python
- Understood negative indexing ([-1] gives last element)
- Compared direct access vs iterative approach

-----------------------------------------------------
Best Practice:
-----------------------------------------------------
- Use indexing for constant time access (O(1))
- Avoid loops for simple access problems

-----------------------------------------------------
Notes:
-----------------------------------------------------
- Handle edge cases like empty string in real scenarios
"""