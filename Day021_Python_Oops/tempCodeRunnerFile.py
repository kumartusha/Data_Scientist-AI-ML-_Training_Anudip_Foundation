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

class A:
    def __init__(self):
        print("This is the A class Constructor")
        
    @staticmethod    
    def run():
        print("Car Running in A")
        
class B:
    def __init__(self):
        print("This is the B Class Constructor")
     
    @staticmethod    
    def run():
        print("Car Running in B")    
        

class C(B,A):
    def __init__(self):
        print("THis is the C Class Constructor")
 
c1 = C()
c1.run()                                      
c1.run()                                      
c1.run()                                      