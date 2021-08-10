import random
import string
import requests
import re


def generate_random_lightshot_url(length):
    letters = string.ascii_lowercase
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(random.choice([letters_and_digits,letters]), length))
    return "http://prnt.sc/" + rand_string


def check_for_avai_img():
    page_url = generate_random_lightshot_url(6)
    html_text_url = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}).text
    if '//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png' in html_text_url:
        return 'The screenshot was removed'
    else:
        return page_url

def check_for_url_of_img(page_url):
        if 'The screenshot was removed' in page_url:
            return 'The screenshot was removed'
        html_text_url = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}).text
        if 'https://image.prntscr.com/image/' in html_text_url:
            match = re.search('https://image.prntscr.com/image/.{22,32}.png', html_text_url)
            return (match[0] if match else 'Not found')
        else:
            match = re.search('https://i.imgur.com/.{7}.png', html_text_url)
            return (match[0] if match else 'Not found')


def download_img_from_url(url):
    if 'Not found' in url:
        print('Not found')
    elif 'The screenshot' in url:
        print('The screenshot was removed')
    else:
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

i = 0
while i < 100:
    url = check_for_avai_img()
    download_img_from_url(check_for_url_of_img(url))
    i += 1
