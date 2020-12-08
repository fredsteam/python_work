car = ['subaru', 'bmw', 'audi', 'honda', 'Toyota']
print("Is a'subaru' in the list? I predict True.")
print('subaru' in car)

print("\nIs a 'audi'in the list? I predict True.")
print('audi' in car)

print("\nIs a 'toyota' in the list? I predict False.")
print('toyota' in car)
print("toyota is false because it is capitalized in the list.")
#print("I will use the .lower with car to have it evaluate all items lowercase.")
#car.lower() == 'toyota'
#print("\nIs a 'toyota' in the list? I predict True.")
#This gave an error because you can't do it this way with a list. You can do it for a
#single item but not a list. I will probably learn how this can be done later in the book.

car = 'Toyota'
car.lower() == 'toyota'
print(f"\nIs toyota in this list? I predict yes")
print('toyota' in car.lower())
print(car)
#I'm not sure what I really did here. The value of the variable hasn't changed.
#So that part is good, but I'm not sure I need to define the car.lower() on #18

#age = 19
#age = 17
age = 53
if age >= 18:
    print("\nYou are old enough to enter the club.")
if age < 18:
    print("\nSorry your aren't old enough to enter the club.")
if age >= 50:
    print("\nHowever, you are old and may die in this club.")
    
#guess = 18
guess = 53
#if guess != 18:
#    print("\nWrong answer, guess again.")
if guess == 53:
    print("\nThat is the correct number!")

age_0 = 21
age_1 = 20
if age_0 and age_1 >= 21:
    print("\nEveryone is old enough to enter the club.")
else:
    print("\nSorry, everyone isn't old enough to enter the club.")
if age_0 or age1 < 21:
    print("\nIf you want to hangout together, we have an underage club too.")
    
cool_people = ['fred', 'lori', 'sean', 'ryan', 'tyler']
person = 'trace'
#person = 'fred'
if person in cool_people:
    print(f"\n{person.title()}, is cool!!")
if person not in cool_people:
    print(f"\n{person.title()}, isn't cool!")