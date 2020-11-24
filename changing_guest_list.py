guest_list = ['larry bird', 'steve jobs', 'dad']
print(f"The three people I would invite to a dinner party is {guest_list}.")
print(f"I would invite {guest_list[0].title()}, because he is my favorite basketball player.")
print(f"I would invite {guest_list[1].title()}, because I would really like to know how his brain works.")
print(f"I would invite {guest_list[2].title()}, because I miss him a lot and have a shit ton of questions I want to ask him.")
print(f"I just found out that {guest_list[0].title()} can't make it to dinner.")
del guest_list[0]
guest_list.insert(0,'steve wozniak')
print(f"I would invite {guest_list[0].title()}, because I think he is brilliant and would love to ask him a bunch of questions.")
print(f"I would invite {guest_list[1].title()}, because I would really like to know how his brain works.")
print(f"I would invite {guest_list[2].title()}, because I miss him a lot and have a shit ton of questions I want to ask him.")