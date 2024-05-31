class Bodega:
    def __init__(self, coordenadasUbicación, descripción, historia, nombre, periodoActualización, region    ):
        self.coordenadasUbicación = coordenadasUbicación
        self.descripción = descripción
        self.historia = historia
        self.nombre = nombre
        self.periodoActualización = periodoActualización
        self.region =   region

    def getNombre(self, ):
        return self.nombre

    def obtenerRegionYPais(self, ):
        region = self.region.getNombre()
        pais = self.region.obtenerPais()
        return region, pais

    def getCoordenadasUbicación(self, ):
        return self.coordenadasUbicación

    def setCoordenadasUbicación(self, value):
        return self.coordenadasUbicación

    def getDescripción(self, ):
        pass

    def setDescripción(self, value):
        pass

    def getHistoria(self, ):
        pass

    def setHistoria(self, value):
        pass

    def setNombre(self, value):
        pass

    def getPeriodoActualización(self, ):
        pass

    def setPeriodoActualización(self, value):
        pass
