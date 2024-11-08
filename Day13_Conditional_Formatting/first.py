# 1. If-Else Statements
# The basic form of conditional formatting, where you check a condition and execute code based on whether it’s True or False.

# python
# Copy code
# x = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is 5 or less")
# 2. If-Elif-Else
# To check multiple conditions, use elif (short for "else if"). Only the first True condition's block will execute.

# python
# Copy code
# x = 7
# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is 5 or less")
# 3. Nested If Statements
# You can place one if statement inside another to create complex conditions.

# python
# Copy code
# x, y = 10, 20
# if x > 5:
#     if y > 15:
#         print("x is greater than 5 and y is greater than 15")
# 4. Ternary (Conditional) Operator
# A shorthand for if-else statements, especially useful for single-line conditionals.

# python
# Copy code
# x = 15
# result = "Greater than 10" if x > 10 else "10 or less"
# print(result)  # Output: Greater than 10
# 5. Logical Operators (and, or, not)
# Use and to check if both conditions are True, or if either is True, and not to reverse the condition.

# python
# Copy code
# x, y = 8, 12
# if x > 5 and y > 10:
#     print("Both conditions are true")
# if x > 10 or y > 10:
#     print("At least one condition is true")
# if not x > 10:
#     print("x is not greater than 10")
# 6. Using in for Membership Testing
# You can check if a value is part of a list, tuple, or set.

# python
# Copy code
# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#     print("Banana is in the list of fruits")
# 7. Switch Case (Python 3.10+)
# Python 3.10 introduced match statements, which act like switch-case.

# python
# Copy code
# def fruit_color(fruit):
#     match fruit:
#         case "apple":
#             return "red"
#         case "banana":
#             return "yellow"
#         case "cherry":
#             return "red"
#         case _:
#             return "unknown"

# print(fruit_color("apple"))  # Output: red
# 8. Using assert for Conditions in Testing
# assert helps to ensure a condition is True. If it’s False, it raises an AssertionError.

# python
# Copy code
# x = 10
# assert x > 5, "x should be greater than 5"
# 9. Lambda Functions with Conditional Logic
# You can use lambda with if-else for simple conditional expressions.

# python
# Copy code
# is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(is_even(10))  # Output: Even
# 10. Using List Comprehensions with Conditions
# Conditional expressions inside list comprehensions provide a concise way to filter and modify lists.

# python
# Copy code
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6]
# These examples cover common ways to implement conditional formatting in Python, from basic if statements to more advanced use cases with match and list comprehensions.