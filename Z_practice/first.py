# # print("Tushar Kumar");

# x = y = z = "Arun"

# # print(x)
# # print(y)
# # print(z)

# x = "f"
# y = "g" 
# z = "Tushar"
# # print(x)

# # @tudhhd = 20;

# # print(@tudhhd)

# val = 10
# # print(x)
# # print(y)
# # print(z)


# # a = 5 + 3j
# # b = 10 
# # c = 20

# # d = "Tushar"
# # e = "Kumar"

# # print(a + b + c)
# # print(d + e)
# # print(d - e)
# # print(d * e)
# # print(d / e)


# # a = 5 + 3j
# # b = "Kumar"
# # print(a + b)
# # print(a * b)
# # print(a / b)
# # print(a - b)


# print(12.79 ** 5)


# x = input("Enter the Value")
# print(x)

# print(type(x))


# labs1 = eval(input("Enter the First Lab Score:- "))
# labs2 = eval(input("Enter the Second Lab Score:- "))
# labs3 = eval(input("Enter the Third Lab Score:- "))
# labs4 = eval(input("Enter the Fourth Lab Score:- "))
# labs5 = eval(input("Enter the Fifth Lab Score:- "))

# total = labs1 + labs2 + labs3 + labs4 + labs5


#  Find the Average of the Labs..
# average = ( total ) / 5
# print("The Average of the Labs:- ",average)


# percentage = (total / 500) * 100
# print("The Percentage of the Labs are:- ",round(percentage, 2))


# #  Different Functions..

# floatVal = float(input("Enter the Float Value"))
# stringVal = float(input("Enter the String Value"))
# intVal = float(input("Enter the int Value"))


#  FInd the area of a circle..
# AOC:-  PI * r * r
# AOT:-  1 / 2 * base * height
# AOR:-  length * width
# AOS:-  side * side


# value = 18

# if(value >= 20):
#     print("Yes Eligible for the Vote")
# else:
#     print("Not Eligible")    
    
    
# attendence = eval(input("Enter the Attendence"))

# if(attendence >= 80):
#     print("Green Mark")
# if(attendence >= 50 and attendence < 80):
#     print("Yellow Mark")
# if(attendence >= 0 and attendence < 50):
#     print("Red Mark")            
    
    
    
# percentage = 89

# if(percentage >= 80):
#     print("Yes Eligible for the Vote")
# else:
#     print("Not Eligible")   
    
    
# score = eval(input("Enter the score"))

# if(score >= 90):
#     print("Grade A")
# elif(score >= 70 and score < 90):
#     print("Grade B")
# elif(score >= 50 and score < 70):
#     print("Grade C")  
# elif(score >= 30 and score < 50):
#     print("Grade D")           
# else:
#     print("Grade E")     
    
    
    
#     # 1. Area of a Circle
# radius = eval(input("Enter the radius of the circle: "))
# circle_area = eval("3.14159 * radius ** 2")  # Using 3.14159 as an approximation for pi
# print("Area of Circle:", circle_area)

# # 2. Area of a Triangle
# base = eval(input("Enter the base of the triangle: "))
# height = eval(input("Enter the height of the triangle: "))
# triangle_area = eval("0.5 * base * height")
# print("Area of Triangle:", triangle_area)

# # 3. Area of a Rectangle
# length = eval(input("Enter the length of the rectangle: "))
# width = eval(input("Enter the width of the rectangle: "))
# rectangle_area = eval("length * width")
# print("Area of Rectangle:", rectangle_area)

# # 4. Area of a Square
# side = eval(input("Enter the side length of the square: "))
# square_area = eval("side ** 2")
# print("Area of Square:", square_area)


"""Python demo for sorting using VS Code Debug Visualizer."""


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return formatted


arr = [6, 9, 3, 12, 1, 11, 5, 13, 8, 14, 2, 4, 10, 0, 7]

# Put serialized into the Debug Visualizer console
serialized = serialize(arr)

# Set a breakpoint on the line below and go through the code in debug mode to
# watch it update
for target_idx in range(1, len(arr)):
    target_value = arr[target_idx]
    compare_idx = target_idx - 1

    while compare_idx >= 0 and arr[compare_idx] > target_value:
        arr[compare_idx + 1] = arr[compare_idx]
        serialized = serialize(arr)
        compare_idx -= 1

    arr[compare_idx + 1] = target_value
    serialized = serialize(arr)

assert arr == sorted(arr)
