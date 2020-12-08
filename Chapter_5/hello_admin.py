#users = ['admin', 'fred', 'lori', 'ryan', 'tyler']
users = []

for user in users:
    if user in 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    elif user in users:
        print(f"Hello {user.title()}, thank you for logging in again.")
if not users:
        print("We need to add some users")