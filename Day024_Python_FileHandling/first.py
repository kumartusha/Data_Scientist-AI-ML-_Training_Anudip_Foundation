

# f = open("first.txt", "r")



# line1 = f.readline()
# print(line1)

# Create and write to a file
# file = open("example.txt", "w")  # Open in write mode
# file.write("This is a newly created file.")  # Write content to the file
# file.close()  # Close the file


# f = open("example.txt", "r")

# line1 = f.readline()
# print(line1)


# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()


with open("C:/Users/USER/OneDrive/Desktop/demo/demo.txt", "w") as f:
    f.write("Hello My Name is Tushar Kumar")
    f.write("Hello My Name is Rakshit Panwar")
    f.write("Hello My Name is Shivam Chaudhary")
    
  
with open("C:/Users/USER/OneDrive/Desktop/McKinleyRIceResume.pdf", "r") as f:
     list1 = f.readline()
     print(list1)