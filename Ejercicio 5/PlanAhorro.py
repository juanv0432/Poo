class planAhorro:
    __codigoPlan=-1
    __modelo=''
    __versionVehiculo=''
    __valorVehiculo=-2
    __cantCuotasPlan=60
    __cantCuotasPagasNecesarias=10
    def __init__(self, cod, mod, ver, valor):
        self.__codigoPlan=cod
        self.__modelo=mod
        self.__versionVehiculo=ver
        self.__valorVehiculo=valor

    def __str__(self):
        return "%s %s %s" %(self.__codigoPlan, self.__modelo, self.__versionVehiculo)
    
    def getCod(self):
        return self.__codigoPlan
    
    def getMod(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__versionVehiculo
    
    def getValorVehiculo(self):
        return self.__valorVehiculo
    
    @classmethod
    def getCantCoutasPlan(cls):
        return (cls.__cantCuotasPlan)
    
    @classmethod
    def getCantCuotasPagasNecesarias(cls):
        return (cls.__cantCuotasPagasNecesarias)
