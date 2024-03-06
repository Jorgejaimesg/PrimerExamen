
def conversion1(op1,op2,cantidad):

    if op1 == '1':
        if op2=='1':
            print(f'Es el mismo valor, por lo que la divisa es le misma= {cantidad} Dolares')
            return
        elif op2=='2':
            result=cantidad*3944
            print(f'El total es de {result} Pesos')
            return
        elif op2=='3':
            result=(cantidad*3944)/4279
            print(f'El total es de {result} Euros')
            return
        elif op2=='4':
            result=(cantidad*3944)/26.30
            print(f'El total es de {result} Yenes')
            return
        
    elif op1 == '2':
        if op2=='1':
            result=(cantidad/3944)
            return result
        elif op2=='2':
            print(f'Es el mismo valor, por lo que la divisa es le misma= {cantidad} Pesos')
            return
        elif op2=='3':
            result=cantidad/4279
            print(f'El total es de {result} Euros')
            return
        elif op2=='4':
            result=cantidad/26.30
            print(f'El total es de {result} Yenes')
            return
            
    
    elif op1 == '3':
        if op2=='1':
            result=(cantidad*4279)/3944
            return result
        elif op2=='2':
            result=cantidad*4279
            print(f'El total es de {result} Pesos')
            return
        elif op2=='3':
            print(f'Es el mismo valor, por lo que la divisa es le misma= {cantidad} Euros')
            return
        elif op2=='4':
            result=(cantidad*4279)/26.30
            print(f'El total es de {result} Yenes')
            return
        
    elif op1 == '4':
        if op2=='1':
            result=(cantidad*26.30)/3944
            return result
        elif op2=='2':
            result=cantidad*3944
            print(f'El total es de {result} Pesos')
            return
        elif op2=='3':
            result=(cantidad*26.30)/4279
            print(f'El total es de {result} Euros')
            return
        elif op2=='4':
            print(f'Es el mismo valor, por lo que la divisa es le misma= {cantidad} Yenes')
            return
  



    
