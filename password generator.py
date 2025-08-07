import random
import string
def password_generator(length):
    if length < 4:
        return "Password should be atleast contain 4 characters"
    letters=string.ascii_letters
    digits=string.digits
    symbol=string.punctuation
    all_char=letters+digits+symbol
    password=''.join(random.choices(all_char,k=length))
    return password
try:
    user_input=int(input("Enter the length of the password:"))
    pwd=password_generator(user_input)
    print("Generated Password:",pwd)
except:
    print("Invalid Choice")
