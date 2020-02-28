users = ['Ed', 'Homeboi', 'Ana', 'John', 'Snow', 'Betrayed']

name = list('utsav')
print(name)

#! for loops
for user in users:
    message = f'welcome {user}'
    print(message)

for i in range(0, 20):
    print('I am Batman')


my_list = list(range(0, 100, 5))
print(my_list)


#! while loop
age = 0

while age <= 20:
    print(f'I am {age} years old')
    age = age + 1
    if age == 14:
        print('I can do math')
        continue
