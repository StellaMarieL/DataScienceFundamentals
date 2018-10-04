#open the csv file with the footballers and their stats
csv = open("footballers.csv")

for line in csv:
	row = line.split(",")

	name = row[0]
	club = row[1]
	fee = row[2]

	print(name)
	print(club)
	print(fee)

#Write a sentence using the data in the file
	print(name + "is part of" + club + ", to which he was sold for" + fee + "million.")


#Advanced
newfile = open("footballers.txt", "w")

new_name = input("Enter the full name of a football player.")
new_club = input("Enter the name of his/her current team.")
new_fee = input("Enter the fee for which he/she was bought.")

new_player_row = "\n" + new_name + "," + new_club + "," + new_fee

csv.close()

footballers = open("footballers.csv", "a")

footballers.write(new_player_row)

newfile.close()
csv.close()
