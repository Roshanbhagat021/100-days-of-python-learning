import  random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1st way
# pick_random_person = random.randint(0,len(friends)-1)
# print(friends[pick_random_person])


# 2nd way

print(*random.choice(friends))

print(*random.choices(friends,k=2))



