import datetime

class Vino:
    def __init__(self, añada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS):
        self._añada = añada
        self._fechaActualizacion = datetime.datetime.now().strftime('%d/%m/%Y')
        self._imagenEtiqueta = imagenEtiqueta
        self._nombre = nombre
        self._notaDeCataBodega = notaDeCataBodega
        self._precioARS = precioARS

    @property
    def añada(self):
        return self._añada
    
    @añada.setter
    def nombre(self, añada):
        self._añada = añada

    @property
    def fechaActualizacion(self):
        return self._fechaActualizacion
    
    @fechaActualizacion.setter
    def fechaActualizacion(self, fecha_Actualizacion):
        self._fechaActualizacion = fecha_Actualizacion

    @property
    def imagenEtiqueta(self):
        return self._imagenEtiqueta
    
    @imagenEtiqueta.setter
    def imagenEtiqueta(self, imagenEtiqueta):
        self._imagenEtiqueta = imagenEtiqueta
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def notaDeCataBodega(self):
        return self._notaDeCataBodega
    
    @notaDeCataBodega.setter
    def notaDeCataBodega(self, notaDeCataBodega):
        self._notaDeCataBodega = notaDeCataBodega

    @property
    def precioARS(self):
        return self._precioARS
    
    @añada.setter
    def precioARS(self, precioARS):
        self._precioARS = precioARS
    
    def calcularRanking():
        pass

    def compararEtiqueta():
        pass

    def esDeBodega():
        pass

    def esDeRegionVitivinicola():
        pass