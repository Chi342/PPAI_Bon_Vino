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

