
import random
class Email:
    def __init__(self, id, dom, tipo, contraseña):
        self.__idCuenta= id
        self.__dominio= dom
        self.__tipoDom= tipo
        self.__contraseña = contraseña
    def retornaEmail(self):
        mail=(self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDom)
        return(mail)
    def retornaDom(self):
        return(self.__dominio)
    def __str__ (self):
        return +self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDom

    def crearCuenta(self):
        a=str(random.randint(1,9))
        b=str(random.randint(1,9))
        c=str(random.randint(1,9))
        d=str(random.randint(1,9))
        f=str(random.randint(1,9))
        cuenta=(self.__idCuenta+'#'+a +b +c +d +f)
        return cuenta
    
    def modificaContraseña(self):
        contra=input('ingrese contraseña actual: ')
        while(contra!=self.__contraseña):
            print('Ingresó una contraseña incorrecta')
            contra=input('ingrese contraseña actual: ')
        self.__contraseña=input('ingrese nueva contraseña: ')
        return()
    def separar(self,correoaux):
        x=(str(correoaux).split('@'))
        y=(x[1].split('.'))
        ids=str(x[0])
        dom=str(y[0])
        tipod=str(y[1])
        contra=input('ingrese contraseña: ')
        mail2=Email(ids, dom, tipod, contra)
        mail2.retornaEmail()
        return mail2
