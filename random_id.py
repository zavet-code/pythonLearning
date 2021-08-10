import random
import string
import requests

def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Alphanum Random string of length", length, "is:", '1' + rand_string)

i = 0 
while i < 10:
    generate_alphanum_random_string(32)
    i += 1

print(requests.get('https://drive.google.com/file/d/1vzirxUvgyHF8TNkqFEWBfnmmqlF77z4f/view?usp=sharing').text)
