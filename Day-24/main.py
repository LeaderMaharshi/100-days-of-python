with open("my_file.txt", mode="a") as file:
    file.write("\n second time Hello world!")
    
with open("new_file.txt", mode="w") as file:
    file.write("second time Hello world!")