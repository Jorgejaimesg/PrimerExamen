import os
import json
BASE='Cuarto_Ejercicio/data/'

        
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+archivo))):
        with open(BASE+archivo ,"w") as bw:
            json.dump(data,bw,indent=4)

def readDataFile(archivo):
    with open(BASE+archivo,"r+") as rf:
        return json.load(rf)

def addData(archivo,data):
    with open(BASE+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)

