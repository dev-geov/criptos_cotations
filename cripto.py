#Internal modules
from functions.functions import *

#Core modules
import sys

def start():
    """
        Function to start displaying Cripto cotations
    """

    # Criptos names and criptos prices lists
    criptos = start_scrapping('http://coinbase.com/price')

    # initialize variable to store criptos cotations
    cotations = start_cotations(criptos)

    try:
        argument = str(sys.argv[1])
    except LookupError as e:
        print(e)
        print("Você deve fornecer um argumento válido.\nUse python cripto.py -h ...")
        return
    
    header = "=============| Cotação de Criptomoeda |===============".format(argument)
    if argument:
        print(header)
        if argument == '-h':
            menu()
        elif argument == '-l':
            total = 50
            if len(sys.argv) == 3:
                try:
                    total = int(sys.argv[2])
                except:
                    pass
            print("{} Criptos disponiveis:".format(total))
            argument = None
            display(argument, cotations, total)
        elif argument == '-c':
            if len(sys.argv) == 3:
                cripto = str(sys.argv[2]).upper()
            else:
                cripto = None
            if cripto is not None and cripto in cotations.keys():
                display(cripto, cotations)
            elif cripto is None:
                print("Digite uma cripto no formato similar 'XXX'")
            else:
                print("Criptomoeda fora de cotação...")
        elif argument == '-a':
            name = str(sys.argv[2]).upper()
            get_about_cripto(name, cotations)
        elif argument == '-s':
            write_csv(cotations)
        else:
            print("Opção inválida!")
        print("=" * len(header))

if __name__ == '__main__':
    start()

