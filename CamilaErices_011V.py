import os
clean="cls"
#Creamos una lista que contenga los cargos y otra los trabajadores
cargo_trabajadores=["ceo", "analista", "desarrollador"]
trabajadores=[["NOMBRE", "CARGO", "SUELDO BRUTO", "DESC. SALUD", "DESC. AFP", "SUELDO LIQUIDO"]]
#definimos una funcion para la opción 1
def registrar_trabajador(trabajadores):
    otro_trabajador="si"
    while otro_trabajador=="si":
        nombre=input("Ingresar nombre y apellido del trabajador: ")
        cargo_ok=False
        while cargo_ok==False:
            try:
                cargo=input("Ingrese cargo del trabajador CEO/DESARROLLADOR/ANALISTA: ").lower()
                if cargo in cargo_trabajadores:
                    cargo_ok=True
                else:
                    print("Cargo erroneo, ingrese otra vez")
                    cargo_ok=False
            except ValueError:
                print("Caego erroneo, intente otra vez")
                cargo_ok=False
        sueldobruto_ok=False
        while sueldobruto_ok==False:
            try:
                sueldo_bruto=int(input("ingrese sueldo bruto del trabajador: "))
                if sueldo_bruto >0:
                    print()
                    sueldobruto_ok=True
                else:
                    print("Sueldo bruto debe ser mayor a 0")
                    sueldobruto_ok=False
            except ValueError:
                print("Sueldo bruto debe ser mayor a 0")
                sueldobruto_ok=False
        #Realizamos los descuentos y calculo de sueldo liquido
        desc_salud=round(sueldo_bruto*0.07)
        desc_afp=round(sueldo_bruto*0.12)
        sueldo_liquido=(sueldo_bruto-desc_salud-desc_afp)
        nuevo_trabajador=[nombre, cargo, sueldo_bruto, desc_salud, desc_afp, sueldo_liquido]
        trabajadores.append(nuevo_trabajador)
        #consultamos si desea agregar otro trabajador
        otro_trabajador=input("Desea agregar otro trabajador? si/no: ").lower()
        os.system(clean)
        if otro_trabajador=="no":
            break
 

#definimos una funcion para listar a los trabajadores agregados
def listar_trabajadores (trabajadores):
    if len(trabajadores) <= 1:
        print("Aún no hay ningun trabajador agregado")
    else:
        for fila in trabajadores:
            print(f"{fila[0]:>15} {fila[1]:>15} {fila[2]:>15}{fila[3]:>15}{fila[4]:>15}{fila[5]:>15}")

#definimos una funcion para imprimir la plantilla
def imprimir_plantilla(trabajadores):
    cargoSeleccionado = input("Ingrese cargo para imprimir planilla o presione ENTER para seleccionar todos los trabajadores: ").lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores[1:] 
        nombreArchivo = 'planilla_todos.txt'
    elif cargoSeleccionado in cargo_trabajadores:
        trabajadores_a_imprimir = [trabajador for trabajador in trabajadores if trabajador[1] == cargoSeleccionado]
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print("Cargo no válido")
        return
    
    with open(nombreArchivo, 'w') as archivo:
        archivo.write(f"{'NOMBRE':>15} {'CARGO':>15} {'SUELDO BRUTO':>15} {'DESC. SALUD':>15} {'DESC. AFP':>15} {'SUELDO LIQUIDO':>15}\n")
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"{trabajador[0]:>15} {trabajador[1]:>15} {trabajador[2]:>15} {trabajador[3]:>15} {trabajador[4]:>15} {trabajador[5]:>15}\n")
#definimos una funcion para el menu 

#definimos una funcion para el menu principal()
def menu_principal():
    otra_accion="si"
    while otra_accion=="si":
        print("Bienvenido, seleccione la opcion: ")
        print("1.-Registre un trabajador ")
        print("2.- Listar trabajadores ingresados")
        print("3.- Imprimir planilla")
        print("4.- Salir")
        opcion=int(input("Opción: "))
        os.system(clean)
        if opcion==1:
            registrar_trabajador(trabajadores)
            
        elif opcion==2:
            listar_trabajadores(trabajadores)
        elif opcion==3:
            imprimir_plantilla(trabajadores)
        elif opcion==4:
            print("Has salido del programa")
            break
        else:
            print("Opcion invalida intente otra vez")
      

        print("Desea realizar otra accion? si/no: ")
        otra_accion=input("Opcion: ").lower()
        if otra_accion=="no":
            break
       
#llamamos al menu principal         
menu_principal()

    
