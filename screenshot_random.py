import random
import string
import requests


def generate_random_lightshot_url(length):
    letters = string.ascii_lowercase
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(random.choice([letters_and_digits,letters]), length))
    return "http://prnt.sc/" + rand_string



def check_for_avai_img():
    page_url = generate_random_lightshot_url(6)
    html_text_url = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}).text
    if '//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png' in html_text_url:
        return print('The screenshot was removed')
    else:
        return print(page_url)

i = 0
while i < 30:
    check_for_avai_img()
    i += 1
