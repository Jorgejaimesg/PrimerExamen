from tabulate import tabulate
import modulos.corefiles as cf
import sys
import modulos.reusable as r
import modulos.empleados as e
import modulos.colillas as c
data_inventario = {}
def main_menu():
    empleados = cf.readDataFile("empresa.json")
    global data_empleados
    data_empleados = empleados
    
    def wrapper(func,*params):
        r.clear_screen()
        func(*params)
        main_menu()
    
    r.clear_screen()
    title = """
            #########
            # PAGOS #
            #########
    """
    print(title)
    menu =[["1.", "Empleados"], ["2.", "Salarios"], ["3.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(empleados_menu)
    elif op == "2":
        wrapper(colillas_menu)
    elif op == "3":
        sys.exit(("\033[92m{}\033[00m" .format('Vuelva pronto!')))
    else:
        main_menu()

def empleados_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        empleados_menu()

    title = """
################
#  Empleados   #
################
    """
    print(title)
    menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(e.addpersonas,data_empleados)
    elif op == "2":
        cf.clear_screen()
        mod = input('Ingrese el id del empleado a modificar -> ').upper()
        wrapper(e.modify,data_empleados.get(mod,{}),data_empleados)
    elif op == "3":
        wrapper(e.delData,data_empleados)
    elif op == "4":
        wrapper(e.search,data_empleados)
    elif op == "5":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        empleados_menu()

def colillas_menu():
    def wrapper(func,*params):
        cf.clear_screen()
        func(*params)
        empleados_menu()

    title = """
################
#  COLILLAS   #
################
    """
    print(title)
    menu = [["1.", "Agregar colilla"],["2.", "Total a pagar"],["3.", "Buscar colilla"],["4.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))

    op = input("\n>> ")

    if op == "1":
        wrapper(c.addcolillas,data_empleados)
    elif op == "2":
        cf.clear_screen()
        wrapper(c.total,data_empleados)
    elif op == "3":
        wrapper(c.searchcolillas,data_empleados)
    elif op == "4":
        wrapper(main_menu)
    else:
        cf.clear_screen()
        empleados_menu()
