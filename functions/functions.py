#External libraries
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from googletrans import Translator



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
    # store response from requests.get
    html = requests.get(url, timeout=3000)
    if html.status_code == 200:
        # create a BeatifulSoup object
        bs = BeautifulSoup(html.content, 'html.parser')
        for sibling in bs.find('table', {'class': 'bhZWny'}).tbody:
            lista = []
            for data in sibling.find_all('h4', {'class': 'caIgfs'}):
                lista.append(data.get_text())
            criptos.append(lista)
        return criptos
    return []


def get_about_cripto(name, cotations):
    cripto_name = cotations[name]['name']
    url = 'https://coinmarketcap.com/pt-br/currencies/{}/'.format(cripto_name)
    html = requests.get(url)
    infos = {}
    texts = []
    if html.status_code == 200:
        bs = BeautifulSoup(html.content, 'html.parser')
        data = bs.findAll('div', {'class': 'sc-1lt0cju-0 foqbLn'})
        for d in data:
            texts.append(d.get_text())
        infos['about'] = texts[-1]
        if name in cotations.keys():
            translator = Translator()
            about = infos['about']
            text = translator.translate(about, src='en', dest='pt')
            print("Sobre: {}".format(cripto_name))
            print(text.text)
        else:
            print("Criptomoeda desconhecida...")
    else:
        print(html.status_code)

def display(argument=None, cotations=None, total=None):
    date = datetime.now()
    if argument is not None:
        print("Data: {}".format(date.strftime("%d-%m-%Y - %H:%M:%S")))
        print("Sigla: {}".format(cotations[argument]['abbr']))
        print('POS: {}'.format(cotations[argument]['pos']))
        print("Cripto: {}".format(cotations[argument]['name']))
        print("Preço: {}".format(cotations[argument]['price']))
        print("Var %: {}".format(cotations[argument]['var']))
        print("MCap: {}".format(cotations[argument]['mcap']))
    elif total is not None and isinstance(total, int):
        for key, value in list(cotations.items())[:total]:
            print('{} - {}: {}'.format(value['pos'], value['abbr'], value['name']))

    else:
        print("Problema ao listar Criptomoedas!")



def write_csv(cotations, name=None):
    list_cotations = []
    filename = None
    if name is not None:
        if not name.endswith('.csv'):
            filename = '{}.csv'.format(name)
        else:
            filename = name
    else:
        filename = 'cotations.csv'
    for key, value in cotations.items():
        list_cotations.append(value)

    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['pos', 'abbr', 'name', 'price', 'var', 'mcap'])
            writer.writeheader()
            for cotation in list_cotations:
                writer.writerow(cotation)    
        print("Arquivo salvo com sucesso: {}".format(filename))
    except IOError:
        print("Error ao criar arquivo CSV!")


def convert_real(cripto, value, base, cotations):
    cripto_price = cotations[cripto]['price'].replace(',', '')
    cripto_price = float(cripto_price.replace('R$', ''))
    if base == 'f':
        print("Conversão de {} para Real".format(cotations[cripto]['name']))
        print("Preço: R$ {}".format(cripto_price))
        print("Valor: {} {}".format(cripto, value))
        converted = value * cripto_price
        print("Conversão: R$ {:.2f}".format(converted))
    else:
        print("Conversão de Real para {}".format(cotations[cripto]['name']))
        print("Preço: R$ {}".format(cripto_price))
        print("Valor: R$ {}".format(value))
        converted = value / cripto_price
        print("Conversão: {} {:.5f}".format(cripto, converted))


def menu():
    print("Opções:")
    print()
    print(
        "-a História da Critpomoeda. Ex: python cripto.py -a BTC\n"
        "-ct Para converter Real para Cripto. Ex: python cripto.py ct BTC 200\n"
        "-cf Para converter Cripto para Real. Ex: python cripto.py cf BTC 200\n"
        "-d Ver cotação da Criptomoeda. Ex: python cripto.py -d BTC\n"
        "-h Comando de ajuda. Ex: python cripto.py -h\n"
        "-l Lista de Criptomoedas disponiveis. Ex: python cripto.py -l\n"
        "-s Salvar arquivo CSV. Ex: python cripto.py -s cotations.csv\n"
    )