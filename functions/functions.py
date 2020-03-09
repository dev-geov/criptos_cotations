#External libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from threading import Thread
import time


def start_cotations(criptos=None):
    cotations = {}
    if criptos is not None:
        for cripto in criptos:
            cotations[cripto[2]] = {
                'pos': cripto[0],
                'abbr': cripto[2],
                'name': cripto[1],
                'price': cripto[3],
                'var': cripto[4],
                'mcap': cripto[6] 
            }
        return cotations
    return None



def start_scrapping(url):
    criptos = []
    #store response from requests.get 
    html = requests.get(url)
    if html.status_code == 200:
        #create a BeatifulSoup object
        bs = BeautifulSoup(html.content, 'html.parser')
        for sibling in bs.find('table', {'class': 'bhZWny'}).tbody:
            lista = []
            for data in sibling.find_all('h4', {'class': 'caIgfs'}):
                lista.append(data.get_text())
            criptos.append(lista)
        return criptos
    return criptos

def get_about_cripto(name):
    url = 'https://coinmarketcap.com/pt-br/currencies/{}/'.format(name)
    html = requests.get(url)
    infos = {}
    texts = []
    if html.status_code == 200:
        bs = BeautifulSoup(html.content, 'html.parser')
        data = bs.findAll('div', {'class': 'sc-1lt0cju-0 foqbLn'})
        for d in data:
            texts.append(d.get_text())
        infos['about'] = texts[-1]
        return infos['about']
    return None

def display(argument=None, cotations=None):
    date = datetime.now()
    if argument is not None:
        print("Data: {}".format(date.strftime("%d-%m-%Y - %H:%M:%S")))
        print("Sigla: {}".format(cotations[argument]['abbr']))
        print('POS: {}'.format(cotations[argument]['pos']))
        print("Cripto: {}".format(cotations[argument]['name']))
        print("Preço: {}".format(cotations[argument]['price']))
        print("Var %: {}".format(cotations[argument]['var']))
        print("MCap: {}".format(cotations[argument]['mcap']))
    else:
        for key, value in cotations.items():
            print()
            print('POS: {}'.format(value['pos']))
            print('Sigla: {}'.format(value['abbr']))
