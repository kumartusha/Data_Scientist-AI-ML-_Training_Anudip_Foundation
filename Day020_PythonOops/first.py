# class Student:
#     # marks = []
#     # name = []
#     def __init__(self, name, list1):
#         self.marks = list1
#         self.name = name        
         
#     def average(self):
#        length = len(list1)
#        totalSum = 0
       
#        for i in list1:
#            totalSum += i
#        print("The Average are:- ", round(totalSum / length, 2))      
           
    
# name = "Tushar"
# list1 = [89,78,65, 89, 78, 67 ,98, 78]
# s1 = Student(name, list1)
# s1.average()
   
   
# class Student:
#     # marks = []
#     # name = []
#     def __init__(self, name, list1):
#         self.marks = list1
#         self.name = name 
        
#     @staticmethod
#     def print():
#         print("Hello")          
         
    # def average(self):
    #    length = len(list1)
    #    totalSum = 0
       
    #    for i in list1:
    #        totalSum += i
    #    print("The Average are:- ", round(totalSum / length, 2))      
           
    
# name = "Tushar"
# list1 = [89,78,65, 89, 78, 67 ,98, 78]
# s1 = Student(name, list1)
# s1.average()
# s1 = Student()
# s1.print()

# Student.print()
   
   
# class Bank:
#     def __init__(self, pss = ""):
#         self.__pss = pss
        
#     def getter(self):
#         return self.__pss

#     def setter(self, passw):
#         self.__pss = passw   


# b1 = Bank()
# b1.setter("12345678")
# print(b1.getter())
         
         
# class Geek: 
#     __age = 0
#     # def __init__(self, age = 0):
#     #      self._age = age 
      
#     # getter method 
#     def get_age(self): 
#         return self._age 
      
#     # setter method 
#     def set_age(self, x): 
#         self._age = x 
  
# raj = Geek() 
  
# # setting the age using setter 
# raj.set_age(21) 
  
# # retrieving age using getter 
# print(raj.get_age()) 
  
# print(raj._age) 



#  Example of the Abstraction..

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
        
#     def start(self):
#         self.acc = True            
#         self.brake = True            
#         self.clutch = True
#         print("Car Started...")
        
# c1 = Car()
# c1.start()                    

# class BankAccount:
#     def __init__(self, account, total_amount):
#         self.account = account
#         self.total_amount = total_amount
        
#     def addBalance(self, amount):
#         self.total_amount = self.total_amount + amount
#         print("The amount to be added:- ", amount)
#         print("The total Balance are:- ", self.total_amount)    
        
#     def withdraw(self, amount):
#         print("The withdraw Anount are:- ", amount)
#         self.total_amount = self.total_amount - amount
#         print("The remaining bbalance are:- ", self.total_amount)
        
#     def balance(self):
#         print("The Total amount are:- ", self.total_amount)        

# b1 = BankAccount("1234556", 30000)
# b1.addBalance(10000)
# b1.withdraw(5000)
# b1.balance()

        
        
