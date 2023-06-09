import os
from Registro import ManejadorRegistro

def menu_opciones():
    print("Menú de opciones:")
    print("1. Mostrar para cada variable el día y hora de menor y mayor valor")
    print("2. Indicar la temperatura promedio mensual por cada hora")
    print("3. Dado un número de día listar los valores de las tres variables para cada hora")
    print("4. Salir")

if __name__=='__main__':
    medicion=ManejadorRegistro()
    medicion.cargaarchivo()
    while True:
        os.system('cls')
        menu_opciones()
        menu={
              "1": "medicion.mayormenor()",
              "2": "medicion.temppromedio()",
              "3": "medicion.listarvalores()",
              "4": "print ('Gracias por usar nuestro sistema')"
        }
        opcion=input ("Ingrese la opción que desea: ")
        os.system('cls')
        if opcion in menu:
              if opcion=='4':
                   eval(menu[opcion])
                   break
              else:
                   eval(menu[opcion])
        else:
             print ("Ha ingresado una opción incorrecta, por favor, ingrese una opción nuevamente")