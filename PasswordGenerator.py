import string
import random
a2b = string.ascii_lowercase
A2B = string.ascii_uppercase
nums = string.digits
syms = string.punctuation
length = int(input("Password Length(Recommended >8) : "))
characters = list(a2b) + list(A2B) + list(nums) + list(syms)
random.shuffle(characters)
print("Password : ")
print("".join(random.sample(characters, length)))
