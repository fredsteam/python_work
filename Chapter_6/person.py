person_0 = { 'first_name': 'tyler', 'last_name': 'russell', 'age': '18', 'city': 'virginia beach'}
print(person_0['first_name'].title())
print(person_0['last_name'].title())
print(person_0['age'].title())
print(person_0['city'].title())
print("\n")
print("The output from the 4 lines above was created by a print call for each variable.")
print("\n")
first = person_0['first_name'].title()
last = person_0['last_name'].title()
age_years = person_0['age'].title()
city_live = person_0['city'].title()
print(f"{first} {last} is {age_years} years old and lives in {city_live}")
print("\n")
print("This was a really bad way to do the second line. This is the first time I've picked up this book in a few months.")