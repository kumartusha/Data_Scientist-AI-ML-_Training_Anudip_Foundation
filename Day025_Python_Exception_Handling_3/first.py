import os
# Try Except wit the Exception to check the finally Should orking fine..
# try:
#     num1 = 10
#     num2 = 0
    
#     print(num1 / num2)
#     print("Hello I'm in the try Class")
# except:
#     print("Exception Can Be Handled")
    
# else:
#     print("I'm running when no exception")

# finally:
#     print("The Process Completed")            
    

# Try Except without the Exception to check the finally Should orking fine..
# try:
#     num1 = 20
#     num2 = 10
    
#     print(num1 / num2)
#     print("Hello I'm in the try Class")
# except:
#     print("Exception Can Be Handled")
    
# else:
#     print("I'm running when no exception")

# finally:
#     print("The Process Completed")                
    

#  Can we Explaicity Handle to stop the Finally Block.
# There are so many methods to do the same thing..

# 1. Os.exit(0), Using the infinity Loop, hen the system Crash, 

# try:
#     num1 = 10
#     num2 = 0
    
#     print(num1 / num2)
#     print("Hello I'm in the try Class")
# except:
#     #  Here we use the Os.Exit to stop the Execution of the Program
#     os._exit(0)
#     print("Exception Can Be Handled")
    
# else:
#     print("I'm running when no exception")

# finally:
#     print("The Process Completed")            
    
    
# 2...  Using the While Loop..

try: 
   num1 = 10
   num2 = 0
    
   print(num1 / num2)
   print("Hello I'm in the try Class")
except:
    #  Here we use the Os.Exit to stop the Execution of the Program
    # os._exit(0)
    while True:
        pass
    print("Exception Can Be Handled")
    
else:
    print("I'm running when no exception")

finally:
    print("The Process Completed")            
        