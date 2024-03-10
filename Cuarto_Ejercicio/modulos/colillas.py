import modulos.corefiles as cf
import modulos.reusable as r
from datetime import datetime
from tabulate import tabulate
def addcolillas(archivo:str,data):
    id=r.checkinput('str','Ingrese el id del empleado').upper()
    if id in data:
        fechapago=datetime.now()
        mes=fechapago.month
        if str(mes) not in data[id]['colillas']:

            diasTrabajados=r.checkinput('int','Ingrese los dias trabajados, recuerde que se le paga por dia completo: ')
            horasExtras=r.checkinput('float','ingrese las horas extra trabajadas: ')
            valorDia=data[id]['Salario']/diasTrabajados
            descuentoxCafeteria=r.checkinput('float','Ingrese el monto consumido en cafeteria: ')
            cuotaPrestamo=r.checkinput('float','Ingrese el valor de la cuota del prestamo que solicito: ')
            
            

            sueldobase=valorDia*diasTrabajados
            total_extra=5500*horasExtras
            totalpagar=sueldobase+total_extra-descuentoxCafeteria-cuotaPrestamo

            colillas={
                'mesPagado':str(mes),
                'fechaPago':str(fechapago),
                'sueldoBase':sueldobase,
                'valorTotalHrasExtras':total_extra,
                'cuotaPrestamo':cuotaPrestamo,
                'descuentoxCafeteria':descuentoxCafeteria,
                'totalAPagar':totalpagar
            }       
            data[id]['colillas'].update({mes:colillas})
            cf.addData('empresa.json',data)
        else:
            r.showError('Ya se registro la colilla para ese mes')
    else:
        r.showError('No se encuentra registrado ningun empleado con ese id')

def searchcolillas(data):

    valor = input("Ingrese el id de la persona a buscar -> ").upper()
    mes =input('ingrese el mes a buscar, recuerde que debe ingresar el numero del mes sin ceros')
    
    if valor in data:
        if mes in data[valor]['colillas']:
            if len(data):

                colilla=data[valor]['colillas'][mes]
                mes,fecha,sueldo_base,extras,prestamo,cafeteria,total=colilla.values()
                displayList = [['Id',valor],['Mes',mes],['Fecha',fecha],['Sueldo Base',sueldo_base],['Horas Extra',extras],['Cuota prestamo',prestamo],['Consummido en cafeteria',cafeteria],['Total a pagar',total]]
                print(tabulate(displayList,tablefmt="fancy_grid"))
                r.pause_screen()
                r.clear_screen()
            else:
                r.showError(f'No se genera pago aun para {valor}')
        else: 
            r.showError('El mes ingresado no corresponde a ninguna colilla')
    else: 
        r.showError(f'la persona con el id: {valor} no se encuentra registrada')
        r.clear_screen()

def total(data):
    total=0
    if len(data):
        for key,value in data.items():
                if 'colillas'in value:
                    for item,valor in value['colillas'].items():
                            total+=valor['totalAPagar']
    
        print(f'El valor total a pagar es de {total}')
    else:
        r.showError(f'No se genera pago')
