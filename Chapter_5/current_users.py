current_users = ['fred', 'lori', 'sean', 'Ryan', 'tyler']
new_users = ['chuck', 'nancy', 'LORI', 'don', 'ryan']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user.title()}, that username isn't available, please choose a different username.")
    else:
        print(f"Congratulations {new_user.title()}, this username is available.")
                