import requests
from bs4 import BeautifulSoup

def get_req(word):
    try:
        req = requests.get(f'https://www.dictionary.com/browse/{word}')
        soup = BeautifulSoup(req.text, 'html.parser')
        definition = soup.select('.e1q3nk1v4')

        return definition[0].get_text()

    except:
        return "Error - word not found"






#All data is given by www.dictionary.com
