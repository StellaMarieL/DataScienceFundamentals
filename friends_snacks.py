#Create a list with three friends
friends = ["Kim", "Ellie", "Alex"]

#Loop list and print names with the number of their characters
for friend in friends:
	name = friend[0]
	name_length = len(name)
	print(name + " has" + str(name_length) + " characters in their name.")
	snack = input(name + ", what is your favorite snack?")
	friend.append(snack)

for friend in friends:
	name = friend[0]
	print(name + "s favorite snack is" + friend[1])
