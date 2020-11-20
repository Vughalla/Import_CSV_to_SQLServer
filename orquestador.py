import schedule
import time
import subprocess
import os
import sys
from datetime import date, datetime

ACTUAL_PATH = os.path.dirname(__file__)
INPUT_PATH = ACTUAL_PATH+'/input'
OUTPUT_PATH = ACTUAL_PATH+'/output'
SQL_PATH = ACTUAL_PATH+'/sql'
LOG_PATH = ACTUAL_PATH+'/log'
today = date.today().strftime("%Y-%m-%d")
logFile = LOG_PATH+"/"+today+"_logAll.log"
SERVER = 'PUT_SERVER_NAME_HERE'

def logger(mensaje):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d_%H:%M:%S")
    print(dt_string + " " + mensaje)

def logSQL():
    with open(LOG_PATH+"/sql_temp.log") as log_temp:
        lines = log_temp.readlines()
        lines = [l for l in lines]
        line = str(lines).split(",")[1]
        line = line.split("\\")[0]
        line = line.split("'")[1]
        logger(line)
    os.remove(LOG_PATH+"/sql_temp.log")

def contar():
    csv = open(INPUT_PATH+'/'+today+'_rdy_to_load.csv') 
    numline = len(csv.readlines()) 
    logger("Se insertaran " +str(numline-1)+ " registros del documento descargado.") 

def ejecutarSQL():
    for csvFile in os.listdir(INPUT_PATH):
        logger(str(csvFile))
        for sqlFile in os.listdir(SQL_PATH):
            logger("Inicia la ejecucion del SQL "+sqlFile)
            FNULL = open(os.devnull, 'w') 
            subprocess.call([ACTUAL_PATH+'/load.bat', SERVER, INPUT_PATH, csvFile, SQL_PATH, sqlFile, LOG_PATH], stdout=FNULL, stderr=subprocess.STDOUT)
            logSQL()
            FNULL.close()
            logger("Ejecucion del archivo "+sqlFile+ " finalizada.")

def mover():
    for inputFile in os.listdir(INPUT_PATH):
        if(os.path.isfile(OUTPUT_PATH+'/'+inputFile)):
            os.remove(OUTPUT_PATH+'/'+inputFile)
            os.rename(INPUT_PATH+'/'+inputFile, OUTPUT_PATH+'/'+inputFile)
        else:
            os.rename(INPUT_PATH+'/'+inputFile, OUTPUT_PATH+'/'+inputFile)

def job():
    sys.stdout = open(logFile, "w")
    logger("Inicia el proceso Orquestador.")
    logger("Inicia el proceso de descarga del documento CSV.")
    os.system(ACTUAL_PATH+"/csv_downloader.py")
    logger("Descarga finalizada.")
    contar()
    logger("Inicia el proceso de carga a la BD.")
    ejecutarSQL()
    logger("Finaliza el proceso de carga a la BD.")
    mover()
    logger("Los documentos input se moveran a la ruta /OUTPUT.")
    logger("Finaliza el proceso Orquestador.")
    sys.stdout.close()
    
schedule.every().monday.at("05:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


#Desarrollado por Emmanuel Pablo Belascuain
#email: epbelascuain@hotmail.com