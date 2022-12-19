import os
from time import sleep
from urllib.request import urlretrieve

try:
    os.system('cls')
    pagLink = input(" Informe o LINK da pagina: ")
    pagForm = input(" Informe o formato da página(PHP ou html): ")

    def download():
        urlretrieve(pagLink, pagForm)

    download()
    os.system('cls')
    print('\n Clonando... ')
    sleep(1.5)
    print('\n Pagina clonada com sucesso!'.format(pagForm))
    exit()

except Exception as y:
    os.system('cls')
    print('\n Clonando... ')
    sleep(1)
    print('\n Ocorreu o seguinte erro: '.format(y))
    exit()
