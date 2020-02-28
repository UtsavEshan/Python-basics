#  A module is basically a file containing a set of functions to include in your application.
#  There are core python modules, modules you can install using pip package manager
#  (including Django) as well as custom modules

import validator
from validator import validate_email
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello world'))

email - 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('email is not valid')
