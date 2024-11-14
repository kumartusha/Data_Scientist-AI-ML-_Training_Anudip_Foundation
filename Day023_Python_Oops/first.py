class Parent:
    def __init__(self):
        print("I am Constructor")
    
    def myName(self):
        print("Tushar Kumar")
    
    def branch(self):
        print("Computer Science and Engineering")
            
        
class Child(Parent):
     def myName(self):
         print("I am Child")


c1 = Child()
c1.myName()            