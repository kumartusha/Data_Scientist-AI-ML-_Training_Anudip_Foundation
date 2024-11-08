# Check the number is even or odd.
# list = [1,-2,7,-2,7,8,-7,-6,4]

# positive = []
# negative = []

# for i in list:
#     if(i < 0):
#         negative.append(i)
#     else:
#         positive.append(i)    
        
# print(negative)        
# print(positive)        



# Break Statement
# def myName(list, even, odd):
#     for i in list:
#         if(i % 2 == 0):
#             even.append(i)
#         else:
#             odd.append(i)    
    
    
# list = [1,2,3,4,5,6,7,8]
# even = []
# odd = []    
# myName(list, even, odd); 
# print(even)   
# print(odd)   


def myName2(list, positive, negative):
    for i in list:
        if(i < 0):
            negative.append(i)
        else:
            positive.append(i)       
    
    
list2 = [1,-2,3,-4,5,-6,7,-8]
positive = []
negative = []    
myName2(list2, positive, negative); 
print(positive)   
print(negative)   



# def printFun():
#     for i in range(5):
#         print("Hello Tushar")
        
# printFun()


# def anudipAddress():
#    print("Anudip Adress")
        
 
# for i in range(5):
#   a = input("Enter Your Name")
#   b = input("Enter Your Marks")
#   anudipAddress()


# def swaping(&a,&b):
#     temp = a
#     a = b
#     b = temp

# a = 4
# b = 8

# print(a,b)
# swaping(a,b)
# print(a,b)

# a = 7
# b = 9

# print(a,b)
# temp = a
# a = b
# b = temp
# print(a,b)


# Without Using the third Variable
# c = 8
# d = 7

# print(c, d)
# c, d = d, c
# print(c, d)


# Without Using the Third Variable
# a = 5
# b = 10

# print("Before Swapping:- ", a, b)

# a = a + b
# b = a - b
# a = a - b

# print("After Swapping:- ", a, b)


# a = input("Enter Character")
# print(a[0])


# result = eval(input("Enter the Expression"))
# print(result)


# for i in range(5):
#     bill = eval(input("Enter The Bill: "))  

#     if bill > 0 and bill < 100:
#         print("Total Amount:", bill * 5)
#     elif bill >= 100 and bill < 200:
#         print("Total Amount:", bill * 10)
#     elif bill >= 200 and bill < 300:
#        print("Total Amount:", bill * 20)
#     else:
#         print("Total Amount:", bill * 30)
    

          
    
    