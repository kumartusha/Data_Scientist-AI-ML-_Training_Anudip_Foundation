# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
# Declare a square() function with one parameter. Then call the function and pass one number and display the square of that number.
# Using max() and min() functions, display the maximum and minimum of 5 random numbers.
# Accept a name from the user and display that in lowercase using the lower() function.


# Solution 1.
def div(num1, num2):
    # division and display the result
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} by {num2} is: {result}")
    else:
        print("Division by zero is not allowed!")

# Call the function
div(10, 2)
div(15, 0)  


#Solution 2.
def square(num):
    # Calculate and display the square of a number
    result = num ** 2
    print(f"The square of {num} is: {result}")

# Call the square function
square(5)
square(12)


# Solution 3.
import random

# Generate 5 random numbers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)
num4 = random.randint(1, 100)
num5 = random.randint(1, 100)

# Find maximum and minimum
maximum = max(num1, num2, num3, num4, num5)
minimum = min(num1, num2, num3, num4, num5)

# Display the numbers, maximum, and minimum
print("Random numbers:", num1, num2, num3, num4, num5)
print("Maximum number:", maximum)
print("Minimum number:", minimum)

#Solution 4
# Accept a name from the user
name = input("Enter your name: ")

# Convert the name to lowercase and display it
lower_name = name.lower()
print(f"Your name in lowercase: {lower_name}")


