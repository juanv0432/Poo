class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def __str__(self):
        return "%s %s %s %s %s" %(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def retornaMillas(self):
        return(self.__millas_acum)
    
    def retornaNom(self):
        return(self.__nombre)
    
    def retornaApe(self):
        return(self.__apellido)
    
    def retornaDni(self):
        return(str(self.__dni))
    
    def retornaNum(self):
        return(int(self.__num_viajero))
    
    def acumulaMillas(self):
        millas1=int(input('ingrese cantidad nueva de millas: '))
        self.__millas_acum+=millas1
        return
    
    def canjearMillas(self):
        millasCanje=int(input('ingrese las millas a canjear: '))
        if millasCanje<=self.__millas_acum:
            self.__millas_acum-=millasCanje
            print('Usted ha canjeado sus puntos')
            print('Sus puntos actuales: ',self.__millas_acum)
        else:
            print('Error, supera las millas que posee')
        return