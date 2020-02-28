language = 'python'

# ? len means length, counts each letter in above case
print(len(language))

# ? can acces any letter in a string
letter = language[5]
print(letter)
# ? can use : to use show multiple letters (in current example)
# ? 0 is not needed
letter = language[0:3]
print(letter)

#! String methods

captalization = language.upper()

print(captalization)
text = 'HEY, WHAT THE HELL?'
uncaptilaized = text.lower()
print(uncaptilaized)

place = text.find('HEY')
print(place)
place = text.replace('HEY', 'WAIT...')
print(place)

#!there are a lot
