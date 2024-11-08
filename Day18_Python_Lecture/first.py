# Dictionary in Python..

dict = {
    
    1: 10,
    2: 20, 
    3: 30,
    
}


# def is_present(x):
#     if x in dict:
#         print("Present")
#     else:
#         print("Not Present")    
        
# is_present(5)        

# setData = {1,2,3,4,5,6}
# print(setData)

# st = {5,2,3,4,"Bhai"}
# print(st)
# print(type(st))

# dict = {
#     1:1,
# }
# print(dict)

# st = {}

# st = {1,2,3,4,5}

# for i in st:
#     print(i)

# st = {1,2,3,4,5,6,7,8}
# st2 = {5,56,6,8}

# st.add(90)
# st.update(st2)
# st.union(st2)
# st.intersection(st2)

# lst = [1,6,8,8,9,7,2,2,3,4,5,5,6,6,7]
# st = set(lst)

# list1 = list(st)
# print(list1)

# for i in lst:
#     st.add(i)

# Questions on set ********************

# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=' ')
#     print()   


# for i in range(1,5):
#     for j in range(1,5):
#         if(i >= j):
#             print("*", end=' ')       
#     print() 

# for i in range(1,5):
#     for j in range(1,5):
#         if(i <= j):
#             print("*", end=' ')   
#     print() 


# for i in range(1,5):
#     for j in range(1,5):
#         if(j >= 5-i):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()            


for i in range(1,5):
    for j in range(1,5):
        if(j <= i):
            print("*", end=' ')   
    print()

