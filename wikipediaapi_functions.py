import requests
#Create a function
def lookup(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)
    data = req.json()
    user_input = data[f"{value}"]
    return user_input

#Ask the user for a wikipedia article and if they want a description or extract
title = input("What would you like to look for on wikipedia?")
title.strip().replace(" ", "_")

value = input("Would you like to view a 'description' or a 'extract'? Please choose one of the two: ")
value.lower().strip()

data = lookup(title, value)
print(data)
