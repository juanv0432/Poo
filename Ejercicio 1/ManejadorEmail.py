import csv
from Email import Email
class manejadorEmail:
    def __init__(self):
        self.__lista=[]

    def agregarMail(self,mail):
        self.__lista.append(mail)

    def testMail(self):
        archivo= open('C:\\Users\\ville\\OneDrive\\Escritorio\\Python\\Ejercicio 1\\DatosE1.csv') #archivo = open('DatoeE1.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            mail=Email(fila[0],fila[1],fila[2],fila[3])
            mail.retornaEmail()
            self.agregarMail(mail)
        archivo.close()
        return
    
    def comparaDominio(self):
        for i in range (len(self.__lista)):
            if (self.__lista[i].retornaDom()!='yahoo'or'gmail'or'hotmail'):
                print('error: dominio mal escrito')
        return
    
    def contador(self):
        dominioAux=input('ingrese un dominio: ')
        for i in (len(self.__lista)):
            if self.__lista[i].retornadDom==dominioAux:
                cont=cont+1
        return cont      