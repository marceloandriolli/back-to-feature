import string
from random import choice


CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

def genetaror(chars=string.ascii_lowercase, len=50):
    return ''.join(choice(chars) for i in range(len))


print(genetaror(chars=CHARS))