#External libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime


def start_cotations(criptos=None):
    cotations = {}
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



def start_scrapping(url):
    #store response from requests.get 
    html = requests.get(url)
    #create a BeatifulSoup object
    bs = BeautifulSoup(html.content, 'html.parser')
    #filter all H4 tags and store its contents
    #criptos = bs.findAll('h4', {'class': 'caIgfs'})
    criptos = []
    for sibling in bs.find('table', {'class': 'bhZWny'}).tbody:
        lista = []
        for data in sibling.find_all('h4', {'class': 'caIgfs'}):
            lista.append(data.get_text())
        criptos.append(lista)
    return criptos

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
