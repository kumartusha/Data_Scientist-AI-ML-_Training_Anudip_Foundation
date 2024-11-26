# Assignment:

# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.   
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.   


# 1. Solution.. (ZeroDivision Error)

# number = int(input("Enter First Number"))
# number2 = int(input("Enter Second Number"))

# try:
#     result = number / number2
#     print(result)
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print("Execute when except not Execute")
# finally:
#     print("Always Print")      

# 2. Solution..  (Raise Exception)

# try:
#     # Bydefault return the string..
#    number1 = input("Enter the Number")
   
#    if not number1.isdigit():
#        raise ValueError("The Number is not the Integer")
#    else:
#        num = int(number1)
#        print(f"{number1} are integer") 

# except ValueError as ve:
#     print(ve)    

# 3. Solution.. (File Handling)

# try:
#     f = open("C:/Users/USER/OneDrive/Desktop/demo.txt", "r")
#     # print(f.readline())
#     # f.write("Hello My name is tushar Kumar, And I want to Become the M. L. Engineer")
#     print(f.readline())
    
# except FileNotFoundError as fer:
#     print(fer)
# finally:
#     # Safely close the file if it was successfully opened
#     try:
#         f.close()
#     except NameError:
#         pass 


# 4. Solution..  (Raise Exception)

# try:
#     # Bydefault return the string..
#    number1 = input("Enter First Number")
#    number2 = input("Enter Second Number")
   
#    if not number1.isdigit():
#        raise TypeError("The Numbers is not the Integer")
#    else:
#        num = int(number1)
#        num2 = int(number2)
#        print(f"{number1} are integer") 
#        print(f"{number2} are integer") 

# except TypeError as ve:
#     print(type(ve).__name__)
#     print(ve)    