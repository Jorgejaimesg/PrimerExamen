import os
import sys
import json
BASE='Segundo_Ejercicio/data/'
def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")  
        
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

def checkinput(type,msg):
    isrunning=True
    while isrunning:
        try:
            data=input(msg)
            if type=='str':
                pass
            if type=='int':
                data=int(data)
                if data <0:
                    raise ValueError
            if type=='float':
                data=float(data)
        except: 
            ValueError
            print('dato erroneo')
            pause_screen()
            clear_screen()
        else:
            isrunning=False
            return data