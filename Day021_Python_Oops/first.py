# class LandRover:
#     def myFunc(self):
#         print("Hello")
    
# class Jaguar(LandRover):
#     def myFunc(self):
#         super().myFunc()
#         print("Tushar Kumar")


# c1 = Jaguar()
# c1.myFunc()


# class Car:
#     color = "Black"
    
#     @staticmethod
#     def start():
#         print("Car Started")
        
#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class Maruti(Car):
#     def __init__(self, name):
#       print("The Car name are:- ", name)
    
    
# m1 = Maruti("Toyota")
# m1.start()            
# m1.stop()


#   This is the Multilevel Inheritance....
# class Car:
#     def __init__(self):
#         print("This is the Car Constructor")
        
#     @staticmethod    
#     def start(): 
#         print("Car Started")
   
#     @staticmethod
#     def stop():
#         print("Car Stopped")
    

# class Maruti(Car):
#     @staticmethod
#     def run():
#         print("Car Running")
        
# class Swift(Maruti):
#     def __init__(self):
#         print("This is the Swift Class Constructor")
        
# s1 = Swift()
# s1.run();   


# This is the Example of the Multiple Inheritance

# class A:
#     def __init__(self):
#         print("This is the A class Constructor")
        
#     @staticmethod    
#     def run():
#         print("Car Running in A")
        
# class B:
#     def __init__(self):
#         print("This is the B Class Constructor")
     
#     @staticmethod    
#     def run():
#         print("Car Running in B")    
        

# class C(B,A):
#     def __init__(self):
#         print("THis is the C Class Constructor")
 
# c1 = C()
# c1.run()                                      
# c1.run()                                      
# c1.run() 

# Super Keyword in Pytgoon

# class Car:
#     def __init__(self, type):
#         print("I am the Car Sonstructor")
#         self.type = type
     
#     @staticmethod
#     def start():
#         print("Car is Started")
    
#     @staticmethod
#     def stop():
#         print("Car is Stopped")          
                                             
                                             
# class Maruti(Car):
#     def __init__(self,name, type):
#         self.name = name
#         print("I am Maruti Constructoe")
#         # super().__init__(type)
#         super().start()

      
# m1 = Maruti("Honda", "Diesel")
# m1.start()
# m1.stop()

# class Car:
#     name = "Tushar Kumar"
#     def __init__(self, name):
#         print("I'm in Car Constructor", name)
#         Car.name = name
#         self.__class__.name = name
#         print(self.__class__.name)
       
#     @classmethod    
#     def nameChange(self, name):
#         Car.name = name
#         # pass
        

# c1 = Car("Ankit")
# print(c1.name)
# print(Car.name)

# c1.nameChange("Rakshit")

# print(Car.name)
# print(c1.name)

# Polymorphism concept in Python

class Parent:
    def __init__(self, name, age):
        self.name = name            # Public attribute
        self._age = age             # Protected attribute
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

class Child(Parent):
    def show_age(self):
        print(f"Accessing protected _age from subclass: {self._age}")

# Creating instances
parent = Parent("Alice", 40)
child = Child("Bob", 20)

# Accessing protected attribute within the class
parent.show_info()  # Name: Alice, Age: 40

# Accessing protected attribute within subclass
child.show_age()    # Accessing protected _age from subclass: 20

# Accessing protected attribute from outside (not recommended)
print(parent._age)  # 40

        