import modulos.corefiles as cf
from tabulate import tabulate
def menu():
    tienda={}
    cf.checkFile('tienda.json',tienda)
    global data_tienda
    data_tienda=cf.readDataFile('tienda.json')

    title="""
    ###############################
    ####### Tienda Viveres 🌱 ####
    ###############################
    """

    isRunning=True
    while isRunning:
        print (title)

        print('1. Agregar \n2. Buscar\n3. Salir')
        op=input('->')
        if op=='1':
            id=cf.checkinput('str','Ingrese el id: ')
            nombre=cf.checkinput('str','Ingrese el nombre: ')
            valorUnitario=cf.checkinput('float','Ingrese el valor unitario: ')
            stockmin=cf.checkinput('int','Ingrese el stock minimo: ')
            stockmax=cf.checkinput('int','Ingrese el stock maximo: ')
    

            Producto={
            'id':id,
            'nombre':nombre,
            'valorUnitario':valorUnitario,
            'stockmin':stockmin,
            'stockmax':stockmax
            }
            data_tienda.update({id:Producto})
            cf.addData('tienda.json',data_tienda)
        elif op=='2':
            buscar=input('ingrese el id del estudiante')
            if buscar in data_tienda:
                print(data_tienda[buscar])
                cf.pause_screen()
            else:
                print('El estudiante no existe')
                cf.pause_screen()
                
            pass
        elif op=='3':
            isRunning=False
        else:
            menu()
