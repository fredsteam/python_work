#age = 12
#age = 3
#age = 19
age = 65
if age < 4:
#    print("Your admission cost is $0.")
    price = 0   
elif age < 18:
#    print("Your admission cost is $25.")
    price = 25
elif age < 65:
    price = 40
#instead of an else statement. You could use a final elif statement
#elif age >= 65:
else:
#    print("Your admission ost is $40.")
    price = 20
print(f"Your admission cost is ${price}.")