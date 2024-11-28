
#  Some system funtion.
import sys

num1 = 30
num2 = 0

try:
  
  result = num1 / num2
  print(result)
except Exception as e:
    print(e)
    print(e.__class__)
    print(sys.exc_info())


#   Explicitely throw the error.

# age = 10

# try:
#     if(age < 18):
#         raise ValueError
#     else:
#         print("ELIGIBLE")
# except Exception as e:
#     print(e)        
        
        

# age = 10

# try:
#     if(age < 18):
#         raise Exception("NOT ELIGIBLE")
#     else:
#         print("ELIGIBLE")
# except Exception as e:
#     print(e)        
                


#  Customize Exception / User Defined Exception ************************************************************************************************************

# => 1st Method
# class UnderAgeException(Exception):
#     pass

# class Tushar:
#     age = 20
    
#     try:
#         if(age < 18):
#             raise UnderAgeException("You are Under Age")
#         else:
#             print("You are Eligible")
#     except UnderAgeException as uae:
#         print(uae)
             
             
# => 2nd Method
# class SevenDivisionError(Exception):
#     def __init__(self):
#         print("You cannot divide by seven")
#         pass

# class Main:
#     num1 = int(input("Enter the First Number: "))
#     num2 = int(input("Enter the Second Number: "))

#     try:
#         if num2 == 7:
#             raise SevenDivisionError
#         else:
#             result = num1 / num2
#             print(result)
#     except SevenDivisionError as sde:
#         print(sde)

    
        
