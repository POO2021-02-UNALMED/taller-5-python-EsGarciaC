class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        from gestion.zona import Zona
        x = 0
        for zona in self._zonas:
            x += zona.cantidadAnimales()
        return x
         
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._nombre = ubicacion
    
    def getZona(self):
        return self._zonas
    
    def setZonas(self, zonas):
        self._nombre = zonas
    