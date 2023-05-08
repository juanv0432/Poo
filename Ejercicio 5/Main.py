from ManejadorPlan import manejadorPlan
if __name__ =='__main__':
    mP=manejadorPlan()
    mP.testPlan()
    opc=None
    while opc!='e':
        opc=input('\tMenú \n\n a)- Actualizar el valor del vehículo\n b)- mostrar código del plan, modelo y versión del vehículo según un valor\n c)- Mostrar el monto que se debe haber pagado para licitar el vehículo\n d)- Modificar la cantidad cuotas que debe tener pagas para licitar\n e)- Salir del Menú\n\nIngrese opción: ')
        if opc=='a':
            mP.actualizarValor()
        elif opc =='b':
            importe=float(input('ingrese un importe: '))
            mP.mostrarPlanes(importe)
        elif opc == 'c':
            mP.mostrarInfo()
        elif opc == 'd':
            mP.modificaCuotasLic()