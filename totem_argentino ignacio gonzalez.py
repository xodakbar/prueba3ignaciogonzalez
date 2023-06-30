dni = []
nombre = []
edad = []
p_nac = []
c_nac = []
e_conyugal = []
f_nac = []


while True:
    op = int(input("---------------------------------------------------------\n**bienvenido al sistema de autoservicio de RENAPER\n---------------------------------------------------------\n**para comenzar ingrese la opcion que desea hacer\n**1.grabar\n**2.buscar\n**3.imprimir\n**4.eliminar\n**5.salir\n---------------------------------------------------------\n-"))
    #este es el grabador 
    if op == 1:
        def calcular_cod_verificador(dni_g):
            dni = str(dni_g)
            multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2]
            suma = sum(int(dni[i]) * multiplicadores[i] for i in range(len(dni_g)))
            resto = suma % 11
            codigo_verificador = 11 - resto
            if codigo_verificador == 11:
                codigo_verificador = 0
            elif codigo_verificador == 10:
                codigo_verificador = 9
            return codigo_verificador
        dni_g = int(input("ingrese el DNI que desea grabar(sin el codigo verificador): "))
        codigo_verfificador = calcular_cod_verificador(dni)
        dni.append (dni_g)

        print (dni,codigo_verfificador)
        while True:
            
            
            grabar_nombre = str(input("ingrese el nombre que desea gabrar (minimo 8 caracteres):    "))
            if len (grabar_nombre)>=8:
                nombre.append(grabar_nombre)
                break
            else:
                print("deben ser minimo 8 caracteres")
                True
        while True:
            grabar_edad = int(input("ingrese la edad (la edad debe ser mayor o igual a cero):   "))
            if grabar_edad>=0:
                edad.append(grabar_edad)
                break
            else:
                print("la edad es invalida")
                True
                
        grabar_f_nac = input("ingrese su fecha de nacimiento:   ")
        f_nac.append (grabar_f_nac)
                
        grabar_e_conyugal = input("ingrese su estado conyugal:  ")
        e_conyugal.append (grabar_e_conyugal)
        
        grabar_p_nac = input("ingrese su pais de nacimiento:    ")
        p_nac.append(grabar_p_nac)
        
        grabar_c_nac = input("ingrese la ciudad de nacimiento:  ")
        c_nac.append(grabar_c_nac)
        
        print("los datos se han grabado los datos correctamente")
        
        #busqueda de los datos de una persona por su rut
    elif op == 2:
        while True:
            b_dni = int(input("ingrese el rut a buscar(sin digito verificador): "))
            if dni.index(b_dni)>=0:
                print (f"\nlos datos de la persona son:\n {nombre[dni.index(b_dni)]}\n edad:{edad[dni.index(b_dni)]}\n pais de nacimiento: {p_nac[dni.index(b_dni)]}\n ciudad de nacimiento: {c_nac[dni.index(b_dni)]}")
                if p_nac [dni.index(b_dni)] == 'argentina':
                    print(" nacionalidad argentina")
                    break
                else:
                    print("dni invalido")
                    True
        #impresion
    elif op == 3:
        while True:
            c_dni = int(input("ingrese dni para imprimir certificado:   "))
            
            if dni.index(c_dni)>=0:
                certificados = int(input('Seleccione una opcion segun el certificado que desea imprimir.\n1. Certificado de nacimiento.\n2. Certificado de estado conyugal.\n'))
                
                if certificados == 1:
                    print(f'------- Certificado de nacimiento -------\n\nRut: {c_dni}\nNombre: {nombre[dni.index(c_dni)]}\nEdad: {edad[dni.index(c_dni)]}\nPais de nacimiento: {p_nac[dni.index(c_dni)]}\nCiudad de nacimiento: {c_nac[dni.index(c_dni)]}\n fecha de nacimiento: {f_nac[dni.index(c_dni)]}')
                    break
                elif certificados == 2:
                   
                    print (f'------- Certificado de nacimiento -------\n\nRut: {c_dni}\nNombre: {nombre[dni.index(c_dni)]}\nEdad: {edad[dni.index(c_dni)]}nfecha de nacimiento: {f_nac[dni.index(c_dni)]}\n estado conyugal: {e_conyugal[dni.index(c_dni)]}')      
                    break
                    
    elif op ==4:

        
        eliminar_dni = (input('ingrese dni que desea eliminar(sin codigo verificador):  '))
        if dni.index(eliminar_dni)<=0:
                edad.pop(dni.index(eliminar_dni))
                p_nac.pop(dni.index(eliminar_dni))
                c_nac.pop(dni.index(eliminar_dni))
                dni.pop(dni.index(eliminar_dni))
                nombre.pop(dni.index(eliminar_dni))
    elif op == 5:
        exit()
            
            
