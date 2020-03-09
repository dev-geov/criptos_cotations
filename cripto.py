#Internal modules
from functions.functions import start_cotations, start_scrapping, display, get_about_cripto

#Core modules
import sys

def start():
    """
        Function to start displaying Cripto cotations
    """

    #Criptos names and criptos prices lists
    criptos = start_scrapping('http://coinbase.com/price')

    #initialize variable to store criptos cotations
    cotations = start_cotations(criptos)

    try:
        argument = str(sys.argv[1])
    except:
        print("Você deve fornecer um argumento válido.\nUse python cripto.py -h ...")
        return
    
    header = "=============| Cotação de Criptomoeda |===============".format(argument)
    if argument:
        print(header)

        if argument == '-h':
            print("Opções:")
            print()
            print(
                "-a 'XXX' História da Critpomoeda\n"
                "-h 'Comando de ajuda'\n"
                "-l 'Ver Criptomoedas disponiveis'\n"
                "-c 'XXX' Ver infos da Criptomoeda\n"
            )
        elif argument == '-l':
            print("Criptos disponiveis:")
            argument = None
            display(argument, cotations)
        elif argument == '-c':
            cripto = None
            try:
                cripto = str(sys.argv[2]).upper()
            except:
                pass
            if cripto is not None and cripto in cotations.keys():
                display(cripto, cotations)
            elif cripto is None:
                print("Digite uma cripto no formato similar 'XXX'")
            else:
                print("Criptomoeda fora de cotação...")
        elif argument == '-a':
            name = str(sys.argv[2]).upper()
            if name in cotations.keys():
                name = cotations[name]['name']
                about = get_about_cripto(name)
                print("About: {}".format(name))
                print(about)
            else:
                print("Criptomoeda desconhecida...")
        else:
            print("Opção inválida!")
        print("=" * len(header))

if __name__ == '__main__':
    start()

