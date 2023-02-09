# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["fdsaf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
