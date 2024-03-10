import modulos.coreFiles1 as cf
def menu():
    estudiantes={}
    cf.checkFile('estudiantes.json',estudiantes)
    global data_estudiantes
    data_estudiantes=cf.readDataFile('estudiantes.json')

    title="""
    #############################
    ####### ESTUDIANTES #########
    #############################
    """

    isRunning=True
    while isRunning:
        print (title)

        print('1. Agregar \n2. Buscar\n3. Salir')
        op=input('->')
        if op=='1':
            id=cf.checkinput('str','Ingrese el id del estudiante: ').upper()
            nombre=cf.checkinput('str','Ingrese el nombre: ').upper()
            apellido=cf.checkinput('str','Ingrese el o los apellidos: ')
            dirección=cf.checkinput('str','Ingrese la direccion: ')
            ciudad=cf.checkinput('str','Ingrese la ciudad: ')
            longitud=cf.checkinput('float','Ingrese la longitud: ')
            latitud=cf.checkinput('float','Ingrese la latitud: ')
            email=cf.checkinput('str','Ingrese el email: ')
            edad=cf.checkinput('int','Ingrese la edad: ')
            ocupación= cf.checkinput('str','Ingrese la ocupacion: ')

            estudiante={
                'id':id,
                'nombre':nombre,
                'apellido':apellido,
                'dirección':dirección,
                'ubicacion':{
                    'ciudad':ciudad,
                    'longitud':longitud,
                    'latitud':latitud},
                'email':email,
                'edad':edad,
                'ocupación':ocupación
            }
            data_estudiantes.update({id:estudiante})
            cf.addData('estudiantes.json',data_estudiantes)
        elif op=='2':
            buscar=input('ingrese el nombre del estudiante').upper()
            if buscar in data_estudiantes:
                print(data_estudiantes[nombre])
            else:
                print('El estudiante no existe')
                
        elif op=='3':
            isRunning=False
        else:
            menu()
