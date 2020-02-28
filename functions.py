
#! what do you do if you have to run it multiple times
# ? define a function


def greeting():
    print('hello, there my friend')
    print('what is your name')
    name = input()
    print(f'nice to meet you {name}')


def multiply_by_10(number):
    return 10 * number


newnum = multiply_by_10(20)

print(newnum)


def add(number, by=1):
    return number + by


added_number = add(10, 5)

print(added_number)
