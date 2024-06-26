import string
import random
all_char = string.ascii_letters + string.digits + string.punctuation
len = int(input("Enter the length of the password: "))
pswd = ''.join(random.choices(all_char, k=len))
print("Your password is :", pswd)