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


# k1 = k2 = 1
# list1 = []
# for i in range(6):
#     list1 = []
#     for j in range(6):
#         if(i >= j):
#             if(i % 2 == 1):
#                 list1.append(k1)
#             else:
#                 print(k1, end=' ')
#             k1 += 1
#         else:
#             # print(" ", end=' ')
#             pass
#     if(i % 2 == 1):
#         print()          
#         print(list1[::-1])  

# rows = 5  # Number of rows
# current_num = 1

# for i in range(1, rows + 1):  # Loop through rows
#     temp = []  # Temporary list to store numbers for the row
#     for j in range(i):  # Add numbers to the current row
#         temp.append(current_num)
#         current_num += 1
    
#     # Reverse the row numbers if the row index is odd
#     if i % 2 == 0:
#         temp.reverse()
    
#     # print(" ".join(map(str, temp)))  # Print the row as a space-separated string
#     print(" ".join(map(str, temp)))       # Returns Like this "1 2 3"


# row = 4
# col = 7

# for i in range(row):
#     for j in range(col):
#         if(j >= (row + 1) - i and j <= (col + 1 + i) - row + 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=' ')
#     print()            

# row = int(input("Enter the row"))
# col = int(input("Enter the col"))

# for i in range(1,row + 1):
#     for j in range(1,col + 1):
#         prin
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()        
            
# for i in range(1,row + 1):
#     for j in range(1,col + 1):
#         if (j > i and j < (col + 1) - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')    
#     print()
        
# def printPattern(n):
#     col = n * 2 - 1

#     for i in range(1,n + 1):
#         for j in range(1, col + 1):
#             if(j >= (n + 1) - i and j <= (n - 1) + i):
#                 print("*", end=' ')
#             else:
#                 # pass
#                 print(" ", end =' ')
#         print()   

# printPattern(11)     


#  Print the patterns By using the python language

# for i in range(1,row + 1):
#     for j in range(1, col + 1):
#         # if(j <= (row + 1) - i or j >= (row - 1) + i):
#         if(j >= i and j <= (row + 3) - i or j >= (row + 1) + i and j <= (col + 1) - i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()          

# row = 5
# col = 9
# k = 1
# l = 5

# for i in range(1,row + 1):
#     for j in range(1, col + 1):
#         if( j < i or j > (col + 1) - i):
#             print(k, end='  ')
#             k += 1
#         else:
#             print(" ", end=' ')     
#     print()      
# for i in range(1,row + 1):
#     for j in range(1, col + 1):
#         if(j <= (row + 1) - i or j >= (row - 1) + i):
#             print(l, end='  ')
#             l -= 1
#         else:
#             print(" ", end=' ')
#     print()      
    
# for i in range(1,10):
#     for j in range(1,10):
#         if(i == 1 or i == 9 or j == 1 or j == 9):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()      

# row = 5
# col = 5
# k = 1
# l = 2

# for i in range(1, row + 1):
#     # k += 2
#     for j in range(1, col + 1):
#         if( i >= j):
#             if(i % 2 == 0):
#                 print(l, end=' ')
#             else:
#                 print(k, end=' ')
#         else:
#             print(" ", end=' ')
#     print()            



#       1
#     2 2 2
#   3 3 3 3 3
# 4 4 4 4 4 4 4
#   5 5 5 5 5
#     6 6 6
#       7
# row = 4
# col = 7
# k = row  - 1
# l = -1

# for i in range(1, row + 1):
#     l += 1
#     for j in range(1, col + 1):
#         if(j > (row + 1) - i and j < (row - 1) + i):
#             print(l, end=' ')
#         else:
#             print(" ", end=' ')
#     print()            

# for i in range(1, row + 1):
#     k += 1
#     for j in range(1, col + 1):
#         if(j >= i and j <= (col + 1) - i):
#             print(k, end=' ')
#         else:
#             print(" ", end=' ')
#     print()         

# ch = 64

# for i in range(1,6):
#     ch += 1
#     for j in range(1,6):
#         if(i >= j):
#             print(chr(ch), end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# row = 5
# col = 5


# for i in range(1,row):
#     for j in range(1,col):
#         # if(i == 1 or i == 9):
#         if(j == 1 or i == row or i == 1):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()    

# for i in range(1,row):
#     for j in range(1,col):
#         # if(i == 1 or i == 9):
#         if(i == col or j == col):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# row = 6
# col = 6

# for i in range(1,row):
#     for j in range(1,col):
#         if(i == row // 2  or j == col // 2):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()            

# row = 6
# col = 6

# for i in range(1,row):
#     for j in range(1,col):
#         if(i == j  or i + j == row):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()            



# row = 6
# col = 6

# for i in range(1,row):
#     for j in range(1,col):
#         if(j == 1  or i == 5 or i == j):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# row = 6
# col = 6

# for i in range(1,row):
#     for j in range(1,col):
#         if(j == 1  or j == i or j == row - 1):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# ***************************************************************************************************************************************