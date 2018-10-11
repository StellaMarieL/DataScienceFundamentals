import json
f = open("movies.json")
movies = json.load(f)

#ask for a year and print the movies corresponfing with the year
input_year = input("Please enter a year ")

for items in movies:
    if str(items["year"]) == input_year:
        print(f'{items["title"]} was made in {items["year"]}')

#give the user different filter posibilities
print("Choose a number based on which filter you would like to use:")
print("1: Filter year of release.")
print("2: Filter movies with durations longer than a certain amount of time.")
print("3: Filter based on directors who also acted in the film.")
print("4: Filter based on chosen genre.")
print("5: Cancel, and exit the program.")

choice_user = input("Which filter would you like to use?")

#ask for more concise data based on the users choice
if choice_user not in ["1", "2", "3", "4", "5"]:
	print("That choice is unavailable.")
	exit()

if choice_user == "1":
 user_year = input("Please enter a release year you would like to filter.")

if choice_user == "2":
	user_duration = input("Please enter a runtime in minutes.")

if choice_user == "4":
	user_genre = input("Please enter a genre.")

if choice_user == "5":
	print("Thank you for using the program. Goodbye.")
	exit()

#generate the results
for  movie in movies:
	year = movie["year"]
	title = movie["title"]
	director = movie["director"]
	actors = movie["actors"]
	duration = movie["duration"]
	genre = movie["genre"]

if choice_user == "1" and movie["year"] == user_year:
	print(f"{title} was released in {year}.")

if choice_user == "2" and movie["duration"] > user_duration:
	print(f"{title} is {duration} minutes long.")

if choice_user == "3" and movie["director"] == movie["actors"]:
	print(f"{title} is a movie wherein {director} is the director and also acts.")

if choice_user == "4" and movie["genre"] == user_genre:
	print(f"{title} has {genre} listed as its genre.")

