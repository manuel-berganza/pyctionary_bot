import requests
from bs4 import BeautifulSoup

testing_word = 'rojo'
r = requests.get(f'https://dle.rae.es/{testing_word}?m=form')
soup = BeautifulSoup(r.text, 'html.parser')
mark = soup.find_all('mark')

def get_words():
    list_of_words = []
    for i in mark:
        text = i.getText()
        list_of_words.append(text)
    return list_of_words

def get_uppercase(listed):
    upperlist = []
    for w in listed:
        if w[0].isupper():
            upperlist.append(w)
    return upperlist

def sentece_maker(param):
    separator = ' '
    print(separator.join(param), sep='\n' )

sentece_maker(get_words())
