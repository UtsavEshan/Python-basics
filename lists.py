# ! this is called a list basically an array
users = ['Ed', 'Homeboi', 'Ana', 'John', 'Snow', 'Betrayed']
print(users[2])
print(users[4:])

alot_zeros = [0]*20
print(alot_zeros)
#! Addings users
users.append('New Items')

print(users)
# ? adding to a certain place
users.insert(0, 'begin')
print(users)


#! remove usesr
users.pop(0)
# ? removes last item, If nothing is entered it will delete the last item
print(users)

#! UNPACKING
items = ['Laptops', 'Phone', 'Joystick']

laptop = items[0]
print(laptop)


# =======================================================================
#! Tupple
letters = ('a', 'b', 'c', 'd')

#! Sets
numbers = {'1', '2', '3'}
