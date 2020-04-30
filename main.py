import re
# TODO: get password from user
user_password = input('Please insert your password: ')
is_password_strong = False

while is_password_strong == False:
    # check the password length
    if len(user_password) < 8:
        user_password= input('The selected password\'s length must be at least 8 :')
    # search for upper and lower case letters
    elif re.search('[a-z]', user_password) == None:
        user_password= input('The password must contain lower case letters :')
    elif re.search('[A-Z]', user_password) == None:
        user_password= input('The password must contain Upper case letters :')
    # search for numbers in password
    elif re.search('[0-9]', user_password) ==None:
        user_password= input('The password must contain at least one digit :')
    # search for special characters
    elif re.search(r'[ !"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`\{|\}~]', user_password) == None:
        user_password= input('The password must contain at least one special character :')
    else:
        is_password_strong =True

print('Your password strength has been verified!')
print(f'Your Verified Password: {user_password}')