banned_users = ['andrew', 'carolina', 'david']
user = 'david'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
if user in banned_users:
    print(f"{user.title()}, this account has been banned and you aren't able to post.")
    
