import conversiones as c
import os
def main():
    title="""
    ##############################
    ## CONVERSION DE DIVISAS 🪙 #
    ##############################
    """
    isrunning=True
    while isrunning:
        print(title)
        list=['1. Dolar','2. Pesos', '3. Euros', '4. Yenes']
        print('Ingrese la divisa que desea convertir')
        for item in list:
            print (item)
        op1=input('->')
        try:
            cantidad=float(input('Ingrese la cantidad a convertir: '))
        except:
            ValueError
            print('Dato incorrecto')
        else:

            os.system('cls')

            print('Ingrese la divisa que desea convertir')
            for item in list:
                print (item)
            op2=input('->')
            os.system('cls')

            c.conversion1(op1,op2,cantidad)
        
        
        salir=input('Desea salir S(si) N(no)')
        if salir == 's' or salir=='S':
            isrunning=False
        elif salir =='N' or salir =='n':
            main()
        else:
            print('Dato erroneo')
if __name__=='__main__':
    main()
    

