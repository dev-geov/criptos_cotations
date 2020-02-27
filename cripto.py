#Internal modules
from functions.functions import start_cotations, start_scrapping, display

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
        print("Você deve fornecer um argumento válido. Use --help")
        return
    
    header = "=============| Cotação de Criptomoeda |===============".format(argument)
    if argument:
        print(header)

        if argument == '-h':
            print(
                "\nOpções: \n-h 'Comando de ajuda'\n"
                "-l 'Ver Criptos disponiveis'\n"
                "-c 'XXX' 'Formato Criptomoeda'\n"
            )
        elif argument == '-l':
            print("Criptos disponiveis:")
            argument = None
            for key in cotations.keys():
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
        else:
            print("Opção inválida!")
        print("=" * len(header))

if __name__ == '__main__':
    start()

