import csv
import numpy as np
class alumno:
    __dni=''
    __apellido=''
    __nombre=''
    __carrera=''
    __anioCursa=0
    def __init__(self,dni,apellido,nombre,carrera,anioCursa):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__anioCursa=anioCursa
    def __str__(self):
        return('DNI {} Apellido y nombre {} {} Carrera {} año que cursa {}'.format(self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__anioCursa))
    def __lt__(self,otro):
        return (self.__anioCursa, (self.__apellido + self.__nombre)) < (otro.getanio(), (otro.get_nomap()))
    def getdni(self):
        return self.__dni
    def getnom(self):
        return self.__nombre
    def getape(self):
        return self.__apellido
    def getanio(self):
        return self.__anioCursa
    def getnomap(self):
        return self.__apellido+" "+self.__nombre
class MateriasAprobadas:
    __Dni=''
    __NomMateria=''
    __fecha=''
    __nota=0.0
    __aprobacion=''
    def __init__(self,DNI,nomMat,fecha,nota,aprobacion):
        self.__Dni=DNI
        self.__NomMateria=nomMat
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
    def getDni(self):
        return self.__Dni
    def getNota(self):
        return float(self.__nota)
    def getNombre(self):
        return self.__NomMateria
    def getFecha(self):
        return self.__fecha
    def getAprov(self):
        return self.__aprobacion
    

class ArregloNumpy:
    __cantidad=0
    __dimension=0
    __incremento=8
    def __init__(self,dim,incremento=8):
        self.__Alumnos = np.empty(dim,dtype=alumno)
        self.__cantidad=0
        self.__dimension=dim
        self.__incremento=incremento

    def agregarAlumno(self,unAlumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__Alumnos.resize(self.__dimension)
        self.__Alumnos[self.__cantidad]=unAlumno
        self.__cantidad += 1

    def testArregloAlumnos(self):
        i=0
        archivo=open('C:\\Users\\ville\\OneDrive\\Escritorio\\Python\\Ejercicio integrador\\alumnos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if i!=0:
                Alum=alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarAlumno(Alum)
            else:
                i+=1
        archivo.close()
    
    def mostrarArreglo(self):
        for i in range(self.__cantidad):
            print(self.__Alumnos[i])
            
    def buscarAlum2(self,dni):
        i=0
        while i<self.__cantidad and dni!=self.__lista[i].getDni():
            i+=1
        if i!=self.__cantidad:
            print ("{}       {}".format(self.__lista[i].get_dni(),self.__lista[i].get_nomap().ljust(17)),end="           ")
        return self.__listaalum[i].getanio()
    
    def Mostar_Listado_Ordenado(self,listado_ordenado):
        for alumno in listado_ordenado:
            alumno.Muestra_Listado()
    
    def ordenaAlumnos(self):
        listado_ordenado = sorted(self.__Alumnos)
        self.Mostrar_Listado_Ordenado(listado_ordenado)

    

class manejadorMaterias:
    def __init__(self):
        self.__lista=[]

    def agregarMateias(self,MateriaAprobada):
        self.__lista.append(MateriaAprobada)

    def testMaterias(self):
        archivo2=open('C:\\Users\\ville\\OneDrive\\Escritorio\\Python\\Ejercicio integrador\\materiasAprobadas.csv')
        reader=csv.reader(archivo2,delimiter=';')
        i=0
        for fila in reader:
            if i!=0:
                Ma=MateriasAprobadas(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarMateias(Ma)
            else:
                i+=1
        archivo2.close()



    
    def generaPromedio(self):
        dni=input('ingrese DNI del alumno: ')
        lista_indices=[]
        i=0
        for fila in self.__lista:
            if fila.getDni()==dni:
                lista_indices.append(i)
            i+=1 
        if len(lista_indices)==0:
            print ("No se encontró el Alumno buscado")
        else:
            prom=[0,0]
            for cant in range (len(lista_indices)):
                prom[0]+=self.__lista[lista_indices[cant]].getNota()                
                if self.__lista[lista_indices[cant]].getAprov()=='E':
                    if self.__lista[lista_indices[cant]].getNota()>=4:
                        prom[1]+=self.__lista[lista_indices[cant]].getNota()
                if self.__lista[lista_indices[cant]].getAprov()=='P':
                    if self.__lista[lista_indices[cant]].getNota()>=7:
                        prom[1]+=self.__lista[lista_indices[cant]].getNota()
                if self.__lista[lista_indices[cant]].getAprov()=='X':
                    if self.__lista[lista_indices[cant]].getNota()>=6:
                        prom[1]+=self.__lista[lista_indices[cant]].getNota()
            print ("El promedio del alumno con aplazos es "+str(prom[0]/len(lista_indices)))
            print ("El promedio del alumno sin aplazos es "+str(prom[1]/len(lista_indices)))
    
    def buscarMateria(self,materia):
        i=0
        p=False
        while i<len(self.__lista):
            if i<len(self.__lista):
                if materia==self.__lista[i].getNombre:
                    p=True
                    return p
                else:
                    p=False
            else:
                print('Usted escribió un nombre incorrecto de materia')
        return p
    
    

    
    def informaMateria(self):
        materia=input('Ingrese el nombre de la materia: ')
        print ("DNI\tApellido y Nombre\tFecha\tNota\tAño que cursa\n")
        for fila in self.__lista:
            if materia.upper()==fila.getNombre():
                if fila.getAprov=='P':
                    if fila.getNota>=7:
                        pos=self.buscarAlum2(fila.getDni)
                    
                else:
                    print('No hay alumnos promocionales de la materia {}'.format(materia))
        return    


if __name__=='__main__':
    A=alumno(44634956,'Villegas','Juan','LCC',2)
    print(A)
    arregloAlumnos=ArregloNumpy(3,8)
    arregloAlumnos.testArregloAlumnos()
    arregloAlumnos.mostrarArreglo()
    mM=manejadorMaterias()
    mM.testMaterias()
    opc=input('\tMenú\na)-informar promedio con y sin aplazos\nb)-informar estudiantes que aprobaron una materia\nc)-obtener listado de alumnos ordenado\nOpción: ')
    while opc=='a' or opc=='b' or opc=='c':
        if opc=='a':
            mM.generaPromedio()
        elif(opc=='b'):
            mM.informaMateria()
        elif(opc=='c'):
            arregloAlumnos.ordenaAlumnos()

