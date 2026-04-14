"""
=====================================================
Problem: Remove Duplicates from a List (Multiple Approaches)
=====================================================

Source: Practice
Level: Easy–Medium

Description:
Given a list of elements, remove duplicates and return
a list containing only unique elements.

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Loop with result list (basic approach)
2. Using set() (fast but unordered)
3. Using dict.fromkeys() (preserves order)
4. Using set() with list comprehension
5. Using set() with loop (efficient + readable)
6. Using index-based loop

-----------------------------------------------------
"""

# =====================================================
# Input
# =====================================================

l = [1, 2, 3, 3, 4, 5, 6, 6]

# =====================================================
# Approach 1: Basic Loop (Preserves Order)
# =====================================================

result1 = []
for num in l:
    if num not in result1:
        result1.append(num)

print("Approach 1:", result1)

# =====================================================
# Approach 2: Using set() (Fast but Unordered)
# =====================================================

result2 = list(set(l))
print("Approach 2:", result2)

# =====================================================
# Approach 3: Using dict.fromkeys() (Best Practice)
# =====================================================

result3 = list(dict.fromkeys(l))
print("Approach 3:", result3)

# =====================================================
# Approach 4: List Comprehension with set()
# =====================================================

seen = set()
result4 = [x for x in l if not (x in seen or seen.add(x))]

print("Approach 4:", result4)

# =====================================================
# Approach 5: Loop with set() (Efficient + Readable)
# =====================================================

seen = set()
result5 = []

for num in l:
    if num not in seen:
        seen.add(num)
        result5.append(num)

print("Approach 5:", result5)

# =====================================================
# Approach 6: Index-based Loop
# =====================================================

result6 = []
for i in range(len(l)):
    if l[i] not in result6:
        result6.append(l[i])

print("Approach 6:", result6)


"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Understood different ways to remove duplicates
- Learned trade-offs between performance and order
- Practiced set(), dictionary, and list operations

-----------------------------------------------------
Best Practice:
-----------------------------------------------------
- Use dict.fromkeys() for clean and ordered result
- Use set() when order does not matter
- Avoid nested loops for large datasets

-----------------------------------------------------
Notes:
-----------------------------------------------------
- set() does not preserve order (in older Python versions)
- dict.fromkeys() preserves insertion order (Python 3.7+)
"""