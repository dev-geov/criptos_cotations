# Cotação de Criptos no terminal linux
## A base de dados é o site do Coinbase

**ferramentas:**
- Python 3
- requests
- BeautifulSoup4

**Como funciona:**
* clone o projeto em um diretório da sua máquina.
* rode o comando *python cripto.py -opção*

**Resultado**
- $ python cripto.py -h *Lista de ajuda* Exibe os comandos e como usar
- $ python cripto.py -l *Lista de criptomoedas* Lista todas as criptomoedas disponiveis para consulta
- $ python cripto.py -c BTC *onde BTC é a sigla da criptomoeda* Exibe dados da respectiva criptomoeda e sua cotação
- $ python cripto.py -a BTC *Resumo da criptomoeda* Exibe um breve resumo da criptomoeda
- $ python cripto -s nome_arquivo.csv *Salva arquivo nome_aqui.csv* Salva uma lista com as 50 principais moedas em um arquivo CSV, onde o .csv é opcional.