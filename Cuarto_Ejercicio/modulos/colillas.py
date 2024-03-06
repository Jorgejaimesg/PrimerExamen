import corefiles as cf
import reusable as r
from datetime import datetime
from tabulate import tabulate
def addcolillas(archivo:str,data):
    id=r.checkinput('str','Ingrese el id del empleado').upper()
    nro=len(data[id]['colilla'])+1

    diasTrabajados=r.checkinput('int','Ingrese los dias trabajados, recuerde que se le paga por dia completo').upper()
    horasExtras=r.checkinput('float','ingrese las horas extra trabajadas').upper()
    valorDia=r.checkinput('float','Ingrese el valor de un dia de trabajo').upper()
    descuentoxCafeteria=r.checkinput('float','Ingrese el monto consumido en cafeteria').upper()
    cuotaPrestamo=r.checkinput('float','Ingrese el valor de la cuota del prestamo que solicito').upper()
    mes=r.checkinput('str','ingrese el mes del pago')
    dia=r.checkinput('int','ingrese el dia del pago')
    fechapago=(f'{dia}/{mes}/2024')

    sueldobase=valorDia*diasTrabajados
    total_extra=5500*horasExtras
    totalpagar=sueldobase+total_extra-descuentoxCafeteria-cuotaPrestamo

    colillas={
        'mesPagado':mes,
        'fechaPago':fechapago,
        'sueldoBase':sueldobase,
        'valorTotalHrasExtras':total_extra,
        'cuotaPrestamo':cuotaPrestamo,
        'descuentoxCafeteria':descuentoxCafeteria,
        'totalAPagar':totalpagar
    }       
        
    data[id]['colillas'].update({nro:colillas})
    cf.addData('empresa.json',data)

def searchcolillas(data):

    valor = input("Ingrese el id de la persona a buscar -> ").upper()
    if valor in data:
        if len(data):

            result= data.get(valor)
            id,nombre,cargo,colilla = result.values()
            mes,fecha,sueldo_base,extras,prestamo,cafeteria,total=colilla.values()
            displayList = [['Id',id],['Mes',mes],['Fecha',fecha],['Sueldo Base',sueldo_base],['Horas Extra',extras],['Cuota prestamo',prestamo],['Consummido en cafeteria',cafeteria],['Total a pagar',total]]
            print(tabulate(displayList,tablefmt="fancy_grid"))
            cf.pause_screen()
            cf.clear_screen()
        else:
            r.showError(f'No se genera pago aun para {valor}')
    else: 
        r.showError(f'la persona con el id: {valor} no se encuentra registrada')
        cf.clear_screen()

def total(data):
    valor = input("Ingrese el id de la persona a buscar -> ").upper()
    if valor in data:
        if len(data):

            result= data.get(valor)
            id,nombre,cargo,colilla = result.values()
            mes,fecha,sueldo_base,extras,prestamo,cafeteria,total=colilla.values()
            displayList = [['Id',id],['Total a pagar',total]]
            print(tabulate(displayList,tablefmt="fancy_grid"))
            cf.pause_screen()
            cf.clear_screen()
        else:
            r.showError(f'No se genera pago aun para {valor}')
    else: 
        r.showError(f'la persona con el id: {valor} no se encuentra registrada')
        cf.clear_screen()
