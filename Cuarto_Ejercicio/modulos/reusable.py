import os
import sys
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
                if data <0:
                    raise ValueError
        except: 
            ValueError
            print('dato erroneo')
            pause_screen()
            clear_screen()
        else:
            isrunning=False
            return data

def showSuccess(message):
    os.system("cls")
    print("\033[92m{}\033[00m" .format(message))
    os.system("pause")
def showError(message):
    os.system("cls")
    print("\033[91m{}\033[00m" .format(message))
    os.system("pause")


def yesORnot(message):
    os.system("cls")
    while(True):
        continuar = checkinput("str", f"{message} Si(s) o No(n)").upper()
        if continuar == "s":
            return True
        elif continuar == "n":
            return False
        else:
            showError("Error Opcion no Reconocida Ingresa s para (Si) o n Para (No)")
