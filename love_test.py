#Get the users, and their lovers name.
name = input("What is your name? ")
loves_name = input("What is your lovers name? ")

#Clean the input by stripping extra spaces and capitalisation
name = name.lower().strip()
loves_name = loves_name.lower().strip()

#Checking the entered names are equal, greater than or lesser than from oneanother.
if name == lovers_name
    print("Either you love yourself or you and " + lovers_name + " are a perfect match!")

elif name < lovers_name
    print(lovers_name + " is the more dominant in the relationship!")
    
elif name > lovers_name
    print(lovers_name + " is the more submissive in the relationship!")

#Checking the name lengths
if len(name) == len(lovers_name)
    print("Both names are the same length, you have a very balanced relationship!")
    
elif len(name) < len(lovers_name)
    print(lovers_name + " has a longer name, which means that they are more dominant in the relationship!")
    
elif len(name) > len(lovers_name)
    print("You have a longer name, " + lovers_name + " is probably the more submissive in the relationship!")

#Calculating the match percentage of the names
difference = abs(len(name) - len(lovers_name))
if difference == 0:
    print("You and" + lovers_name + " are a 100% match!")

elif difference == 1:
    print("You and" + lovers_name + " are a 80% match! Pretty good!")
    
elif difference == 2:
    print("You and" + lovers_name + " are a 60% match! Seems okay, maybe you shouldn't marry them!")
    
elif difference == 3:
    print("You and" + lovers_name + " are a 40% match! Maybe not the greatest fit.")

elif difference == 4:
    print("You and" + lovers_name + " are a 20% match! Are you sure you two should be in a relationship?")
    
else: 
    print("You and " + lovers_name + " dont seem to match at all! Try finding someone that fits better to you!")
