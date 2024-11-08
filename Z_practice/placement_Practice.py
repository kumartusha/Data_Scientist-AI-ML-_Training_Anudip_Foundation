#  Here we write the code for the python to print the pattern program and all program.

#  We need to play with the for loop and the while loop.

# 1.       
# * 
# * *
# * * *
# * *
# *
# number = int(input("Enter the number that you want:- "))   

# for i in range(number):
#     for j in range(number):
#         if(j <= i):
#             print("*", end =' ')
#     print()  
# for i in range(number):
#     for j in range(number):
#         if(j > i):
#             print("*", end =' ')
#     print()                       

# 2. 
#       *
#     * *
#   * * *
# * * * *    

# for i in range(1,5):
#     for j in range(1,5):
#         if(j >= 5 - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()        
# for i in range(1,5):
#     for j in range(1,5):
#         if(j <= 5 - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()   

# for i in range(1,5):
#     for j in range(1,5):
#         if(j <= 5 - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()            

# for i in range(1,5):
#     for j in range(1,5):
#         if(j >= i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()     

# for i in range(1,5):
#     for j in range(1,8):
#         if(j >= 5 -i and j <= (8 + i) - 5):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()                   

# for i in range(1,5):
#     for j in range(1,8):
#         if(j >= 5 -i and j >= (8 + i) - 5):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()                   

# for i in range(1,5):
#     for j in range(1,8):
#         if(j >= i and j <= 8 - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')   
#     print()      

# print("Print the Value",end=" ", sep='-')
# print("Hello")   

# print("Hello ","Tushar"," How are You",end=' ', sep='-')


# for i in range(1,5):
#     for j in range(1,8):
#         if(j <= 5 - i or j >= 3 + i):
#             print("*", end=' ')
#         else:
#             print(" ",end=' ')    
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         if(j <= i):
#             print(j, end=' ')
#         else:
#             print(" ", end=' ')
#     print()     

# for i in range(5,0,-1):
#     for j in range(1,5):
#         if(j > 5 - i):
#             print(j, end=' ')
#         else:
#             print(" ", end=' ')
#     print()       

# for i in range(1,5):
#     print(i)

# for i in range(1,10):
#     k = 10 - i
#     for j in range(1,10):
#         if( j <= 10 - i):
#             print(k, end=' ')
#             k -= 1
#         else:
#             print(" ", end=' ')
#     print()

# for i in range(1,5):
#     #  Here are the starting point for the next row
    
#     for j in range(1,5):
#         if(j <= i):
#             print(1, end=' ')
#         else:
#             print(" ",end=' ')    
#     print()

# def print_pattern(n):
#     if n % 2 == 0:
#         print("Please enter an odd number.")
#         return

#     mid = n // 2  # Calculate the middle row index

#     for i in range(n):
#         # Calculate the number of @ symbols based on row position
#         at_signs = "@" * (min(i, n - i - 1) + 1)
        
#         if i == mid:
#             # Print middle row with both @ and * repeated n times
#             print(at_signs +  "*" * n )
#         else:
#             # Print other rows with @ symbols and a single *
#             print(at_signs + " " * (n - len(at_signs)) + "*")

# # Example usage:
# # print_pattern(3)
# print()
# print_pattern(5)

# def print_pattern(n):
#     if n % 2 == 0:
#         print("Please enter an odd number.")
#         return

#     mid = n // 2  # Calculate the middle row index

#     for i in range(n):
#         # Calculate the number of @ symbols based on row position
#         at_signs = "#" * (min(i, n - i - 1) + 1)
        
#         if i == mid:
#             # Print middle row with both @ and * repeated n times
#             print(at_signs + "*" * n)
#         else:
#             # Print other rows with @ symbols and a single *
#             print(at_signs + " " * (n - len(at_signs) + mid) + "*")

# # Example usage:
# print_pattern(3)

# # for i in range(3):
# #     print(i)

# # print("*" * 3)


         
# print("Tushar" + " " * (3) + "*")


# def print_pattern(n):
#     if(n % 2 == 0):
#         print("The Even Numbers are not allowed")
     
#     mid = n // 2
    
#     for i in range(n):
        
#         at_signs = "@" * (min(i, n - i - 1) + 1)
            
#         if(i == mid):
#             print(at_signs + "*" * n)
#         else:
#             print(at_signs + " " * (n - len(at_signs) + mid) + "*")       
# print_pattern(3)    