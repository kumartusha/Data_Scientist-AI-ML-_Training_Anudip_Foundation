# Assignment:

# Print the first 10 natural numbers using a for loop.
# Python program to check if the given string is a palindrome.
# Python program to check if a given number is an Armstrong number.
# Python program to get the Fibonacci series between 0 to 50.
# Python program to check the validity of password input by users.


# 1. Solution... (natural Number)

# for i in range(1,11):
#     print(i)

# 2. Solution.. (String Palindrome)
#  There the different Approaches for Solving this Question.

# => First Approach
# name = "TusharKumar"
# rev_name = name[::-1]

# # print(rev_name)

# # => Using the For Loop (Second Approach)
# size = len(name)
# print(size)

# for i in range(0, len(name), 1):
#     if(name[i] != name[size - i - 1]):
#         print("String is Not Palindrome")
#         break
# else:
#     print("String is Palindrome")

# 3. Solution.. (Armstrong)
# number = int(input("Enter a number: "))
# total = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     total = total + digit * digit * digit  
#     temp //= 10

# if total == number:
#     print(f"{number} is a armstromg number")
# else:
#     print(f"{number} is not Armstrong number.")

# 4. Solution... (Fibonacci Sequence)
# def fibonacci(number):
#     a, b = 0, 1
#     while a <= number:
#         print(a, end=" ")
#         a, b = b, a + b

# fibonacci(500)

# 5 Solution..
#  Finding the Valid Password Solution for the Given Problem..
# Function to check password validity
# def validPass(password):
  
#     if len(password) < 8:
#         return "Password must be at least 8 characters long."
    
#     # at least one digit
#     isDigit = False
#     for char in password:
#         if char.isdigit():
#             isDigit = True
#             break
#     if not isDigit:
#         return "Password must contain at least one digit."
    
#     # at least one uppercase
#     isUpper = False
#     for char in password:
#         if char.isupper():
#             isUpper = True
#             break
#     if not isUpper:
#         return "Password must contain at least one uppercase letter."
    
#     # at least one lowercase
#     isLower = False
#     for char in password:
#         if char.islower():
#             isLower = True
#             break
#     if not isLower:
#         return "Password must contain at least one lowercase letter."
    
#     # at least one special Case Symbol
#     special_characters = "!@#$%^&*()-_+=<>?/|~"
#     isSpecial = False
#     for char in password:
#         if char in special_characters:
#             isSpecial = True
#             break
#     if not isSpecial:
#         return "Password must contain at least one special character (!@#$%^&*()-_+=<>?/|~)."
    
#     return "Password is valid."

# password = input("Enter a password: ")
# print(validPass(password))