#One portion of chips contains 30 gram of chips
#The nutritional value of one protion of chips
calories = 162
fat = 9.9
carbs = 16
sugar = 0.9

#calculating the amount of chips and nutrition consumed
amount = input("How many grams of chips did you eat?")
total_calories = float(amount) * calories
total_fat = float(amount) * fat
total_carbs = float(amount) * carbs
total_sugar = float(amount) * sugar

#print a statement with the results
print("You have consumed " + str(amount) + " grams of chips. These contained " + str(total_calories) + " calories, " + str(total_fat) + " grams of fat, " + str(total_carbs) + " grams of carbs and " + str(total_sugar) + " grams of sugar.")
