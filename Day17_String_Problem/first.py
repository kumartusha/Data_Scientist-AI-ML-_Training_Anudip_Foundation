# Day 17 Python Problem Solving.


#   List Problems in Python...
# list = [6,2,3,4,5]
# # print(max(list))
# # print(min(list))

# min = list[0]
# for i in list:
#     if(i < min):
#         min = i

# print("The minimum element are:- ",min)

# max = list[0]
# for i in list:
#     if(i > min):
#         max = i

# print("The maximum value are:- ",max)



#  Tuple in Python..

# tuple = (1,True, "tushar", 87.4)
# tuple[0] = "Tushar"

# print(tuple)

# tuple = ("string",)
# print(tuple[-1])
# print(type(tuple))

# tp = (1,2,3,4,5,6,7,8,9)

# print(tp[2:6])
# print(tp[:6])
# print(tp[2:])
# print(tp[:])
# print(tp[-2:-6])

# tp.remove(19)
# print(tp)

# my_tuple = ( 1, 2, 3)
# my_list = []
 
# for i in my_tuple:
#     my_list.append(i)
     
# print(my_list)     
# my_tuple = tuple(my_list)
# print(my_tuple)

# my_list[1] = 34
# print(my_list)


# tp1 = (1,2,3,4)
# tp2 = (5,6,7,8)
# print(tp1 + tp2 + (9,))

# Count Function for the Tuple....
# tp1 = (1,1,2,3,3,3,4)
# print(tp1.count(3))

#  Loops in the Tuple..

# tp1 = (1,2,3,4,5,6,7,8)
# tp2 = ("Tushar", "Rakshit", "Shivam", "Ankit")


# i = 0
# while i < len(tp2):
#     print(tp2[i])
#     i += 1

# tp = ()
# list1 = list(tp)
# for i in range(5):
#     name = eval(input("Enter the name:- "))
#     list1.append(name)
    
# tp = tuple(list1)
# print(tp)


# dict = {
#     1: "Tushar",
#     2: "Ankit",
#     3: "Rakshit",
#     4: "Shivam"
# }


# print(dict)
# print(type(dict))

# dict = {
#     "Name:- ": ["Tushar", "Kumar", "Lalit"],
#     "Adddress:- ": ("modinagar", "GZB", "Meerut"),
#     "Age" : 34,
#     "Mobile_Number": "8057184462",
#     5 : {"Cricket", "Badminton", "Hockey"},
#     "dict2": {1: "First", 2: "Second", 3: "Third"}
# }

# print(dict)


amount = 10000
code = int(input("Enter the code from 1 to 3"))

if(code == 1):
    if(amount <= 1000):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 10  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))  
elif(code == 2):
    if(amount <= 100):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 5  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))          
elif(code == 3):
    if(amount <= 500):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 10  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))