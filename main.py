import re
# TODO: get password from user
sample_pass = 'we!fsWf3wef'
# check the password length
if len(sample_pass) < 8:
    print('The selected password\'s length must be at least 8')
# search for upper and lower case letters
elif re.search('[a-z]',sample_pass) == None:
    print('The password must contain lower case letters')
elif re.search('[A-Z]',sample_pass) == None:
    print('The password must contain Upper case letters')
# search for numbers in password
elif re.search('[0-9]',sample_pass) ==None:
    print('The password must contain at least one digit')
# search for special characters
elif re.search(r'[ !"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`\{|\}~]',sample_pass) == None:
    print('The password must contain at least one special character')
else:
    print('Your password strength has been verified!')