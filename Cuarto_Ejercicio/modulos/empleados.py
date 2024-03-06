import reusable as r
import corefiles as cf
from tabulate import tabulate
def modify(data, srcData):
    if len(data) <= 0:
        r.showError('No se encontro informacion sobre ese activo')
        r.clear_screen()
    else:
        for key in data.keys():
            if(key != 'id'):
                if key != 'colilla':
                        if bool(r.yesORnot(f'Desea modificar el {key}')):
                            r.clear_screen()
                            data[key] = input(f'Ingrese el nuevo valor para {key}: ')
            srcData.update(data)
        r.UpdateFile('empresa.json', srcData)
        r.showSuccess('Informacion modificada correctamente')
        r.clear_screen()

def addpersonas(archivo:str,data):
    
    id=r.checkinput('str','Ingrese el id: ').upper()
    nombre=r.checkinput('str','Ingrese el nombre: ')
    r.clear_screen()
    opc=['1','2','3','4','5']
    isocupation=True
    while isocupation:
        listop=['1. Almacenista', '2. Jefe IT', '3. Administrador', '4. Mensajero', '5. Genrente']
        for item in listop:
            print(item)
        op=input('->')
        if op=='1':
            cargo='Almacenista'
            isocupation=False
        elif op=='2':
            carg='jefe IT'
            isocupation=False
        elif op=='3':
            cargo='Administrador'
            isocupation=False
        elif op=='4':
            cargo='Mensajero'
            isocupation=False
        elif op=='5':
            cargo='Gerente'
            isocupation=False
    
    persona={
        'id':id,
        'nombre':nombre,
        'cargo':cargo,
        'colillas':{}       
    }
        
    data.update({id:persona})
    cf.addData('empresa.json',data)
    

def delData(data):
    if len(data):
        iddel = input(f"Ingrese el id del empleado que desea borrar -> ").upper()
        if iddel in data:
            data.pop(iddel)
            cf.addData('empresa.json',data)
            r.showSuccess('Se ha eliminado correctamente')
            r.clear_screen()
        else:
            r.showError('Ese codigo no se encuentra en la base de datos')
    else:
        r.showError('No hay informacion registrada')
    r.clear_screen()
        
def search(data):
    if len(data):
        valor = input("Ingrese el id de la persona a buscar -> ").upper()
        if valor in data:
            result= data.get(valor)
            id,nombre,cargo,colilla = result.values()
            displayList = [['Id',id],['Nombre',nombre],['cargo',cargo]]
            print(tabulate(displayList,tablefmt="fancy_grid"))
            cf.pause_screen()
            cf.clear_screen()
        else:
            r.showError(f'No hay activos registrados con el codigo {valor}')
    else: 
        r.showError('No hay personal registrado')
        cf.clear_screen()
        
        



