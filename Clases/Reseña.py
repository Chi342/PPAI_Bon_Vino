import datetime


class Reseña:
    def __init__(self, comentario, esPremium, año, mes, dia, puntaje):
        self.comentario = comentario
        self.esPremium = esPremium
        self.fechaReseña = datetime.datetime(año, mes, dia)
        self.puntaje = puntaje

    def sosDePeriodo(self, fechaDesde, fechaHasta):
        if fechaDesde < self.fechaReseña < fechaHasta:
            return True
        return False

    def sosDeSommelier(self, ):
        return self.esPremium

    def getPuntaje(self, ):
        pass

    def getComentario(self, ):
        pass

    def setComentario(self, value):
        pass

    def getEsPremium(self, ):
        pass

    def setEsPremium(self, value):
        pass

    def getFechaReseña(self, ):
        pass

    def setFechaReseña(self, value):
        pass

    def getPuntaje(self, ):
        pass

    def setPuntaje(self, value):
        pass


fecha1 = datetime.datetime(2022, 5, 12)
fecha2 = datetime.datetime(2021, 5, 12)
print(fecha1 > fecha2)