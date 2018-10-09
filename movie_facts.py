#simple version
movie = {
    "title" : "The Dark Knight",
    "year" : 2008,
    "duration" : 152,
    "director" : "Christopher Nolan"
    }

for key, value in movie.items():
    print(f{'key'} : {'value'})

#doing the same thing, but adding minutes to the duration
movie = {
    "title" : "The Dark Knight",
    "year" : 2008,
    "duration" : 152,
    "director" : "Christopher Nolan"
    }

for key, value in movie.items():
    if key == "duration":
        print(f{'key'} : {'value'} minutes)
    else:
        print(f{'key'} : {'value'})

#adding the actors
movie["actors"] = ["Heath Ledger", "Christian Bale", "Aaron Eckhart", "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman"]

for key, value in movie.items():
    if key == "duration":
        print(f{'key'} : {'value'} minutes)
    elif key == "actors"
        print(f{'key'} + ":" + ", ".join(value))
    else:
        print(f{'key'} : {'value'})
