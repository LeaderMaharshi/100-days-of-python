programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}


#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["conditions"] = "Something will execute when conditions are true."

#creating an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}

#edit an item in a dictionary
programming_dictionary["Bug"] = "edited note."
# print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
