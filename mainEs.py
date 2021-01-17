import requests
from bs4 import BeautifulSoup


def get_req(word):
    try:
        definition = " "

        r = requests.get(f'https://dle.rae.es/{word}?m=form')
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.find_all('p')

        contador = 0
        for d in p:
            definition += "\n" + d.getText()

            if contador > 3:
                definition += "\n\n" + "Fuente: " + "https://dle.rae.es/"
                break

            contador += 1


        return definition
    except:
        return "Error - Palabra No encontrada"


