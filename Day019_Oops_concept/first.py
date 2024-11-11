# classes and Objects in Python...

#  Creating the Objects..
# class Student:
#     name = "Tushar Kumar"


# # Creating the Objects..
# s1 = Student()
# print(s1.name)

# class Student:
#     def __init__(self):
#         print("Hello")
#         pass
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass
 
# # s1 = Student()   

# s2 = Student("Tushar", 19)
# print(s2.age)
# print(s2.name)
    
# s2 = Student("Tushar", 19)
# print(s2.age)
# print(s2.name)
    
    
#  Class Attribute and the Object Attribute 
# class Student:
#     student_name = "Rakshit Panwar"
#     name = "Tushar Kumar"
    
#     def __init__(self):
#         pass
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# s1 = Student("Shivam", 19)
# print(s1.age)                            #  Using the Object Attribute Refernce
# print(s1.name)                           #  Using the Object Attribute Refernce
# print(Student.name)                      #  Using the Class Attribute Refernce
# print(Student.student_name)              #  Using the Class Attribute Refernce


class Student:
    name = "Tushar Kumar"
    age = 20
    # def __init__(self) -> None:
    #   pass
    
    def greeting(self):
        print("Hello")
    
    def identity(self, name, age):
        self.age = age
        self.name = name
            
        
s1 = Student()
s1.greeting();  
s1.identity("Tushar", 19);  

