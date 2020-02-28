user = {"name": "Ed", "email": 'des@gmail.com',
        "age": 20, 'purchases': ['1', '2', '3', '4']}
#! this is a dictionary

user['name'] = 'Anna'

print(user)

for key in user:
    print(key)

for key in user.items():
    print(key)

# ? you get the idea
