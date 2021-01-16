import requests
from bs4 import BeautifulSoup

test = 'soup'
req = requests.get(f'https://www.dictionary.com/browse/{test}')
soup = BeautifulSoup(req.text, 'html.parser')

definition = soup.select('.e1q3nk1v4')

def getting_text():
    print (definition[0].get_text())
getting_text()

#All data is given by www.dictionary.com
