import urllib.request
import os
from datetime import date

ACTUAL_PATH = os.path.dirname(__file__)
INPUT_PATH = ACTUAL_PATH+'/input'
today = date.today().strftime("%Y-%m-%d")

def download():
    url = 'https://gen2cluster.blob.core.windows.net/challenge/csv/nuevas_filas.csv?sp=r&st=2020-10-30T14:05:08Z&se=2020-11-30T22:05:08Z&spr=https&sv=2019-12-12&sr=b&sig=UCK4aQvPAIHz19h%2By2NNAYdzs2RF9myeVAFQkwP3Iuc%3D'
    urllib.request.urlretrieve(url, INPUT_PATH+'/doc.csv')


def prepare_csv():
    for inputFile in os.listdir(INPUT_PATH):
        with open(INPUT_PATH+'/'+inputFile, 'r') as infile, \
            open(INPUT_PATH+'/'+today+'_rdy_to_load.csv', 'w') as outfile:
            data = infile.read()
            data = data.replace('"', '')
            outfile.write(data)

download()
if(os.path.isfile(INPUT_PATH+'/doc.csv')):
    prepare_csv()
    os.remove(INPUT_PATH+'/doc.csv')

#Desarrollado por Emmanuel Pablo Belascuain
#email: epbelascuain@hotmail.com