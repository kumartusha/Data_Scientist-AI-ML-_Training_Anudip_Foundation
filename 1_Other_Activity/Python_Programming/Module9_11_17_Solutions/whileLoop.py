# Assignment:

# Write a Python program to reverse a number using a while loop.
# Write a Python program to check whether a number is a palindrome or not.
# Write a Python program to find the factorial of a given number using a while loop.
# Accept numbers using the input() function until the user enters 0. If the user inputs 0, then break the while loop and display the sum of all the numbers.



# 1. Solution..
# number = 1234
# #  We need the number is 321
# ans = 0
# while(number):
#     remainder = number % 10
#     ans = ans * 10 + remainder
#     number = number // 10

# print(ans)    


# 2. Solution...
# number = 1212
# store = number

# ans = 0
# while(number):
#     remainder = number % 10
#     ans = ans * 10 + remainder
#     number = number // 10

# if(ans == store):
#     print("Palindrome") 
# else:
#     print("Not Palindrome")


# 3. Solution....(Factorial Program Using the While Loop)

# number = 5

# fact = 1
# while number:
#     fact *= number
#     number = number - 1

# print(fact)    

# 4. Solution....
# sum = 0
# while True:
#     number = int(input("Enter the Number"))
#     if(number == 0):
#         break
#     sum = sum + number

# print(sum)