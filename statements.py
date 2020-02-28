
# !  if else statements

age = 12

# ?the colon is needded to write if statments in py
if age == 18:
    print('hey, you are quite young')
elif age == 12:
    print('children\'s club is to the left')
else:
    print('you are old')
# ===============
#! not is !
age = 39
if age != 24:
    print('you are not 24')

age = 30
if age > 29 and age < 31:
    print('you are 30')

age = 29
if age > 28 or age > 31:
    print('you are 29')


is_logged = True

if is_logged:
    print('welcome')

#! Boolean values (falsy values)

# ? FALSY VALUES
#  ? 0
#  ? []
# ? ""

# ? Truthy Values
# ? 1
