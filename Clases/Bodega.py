class Bodega:
    def __init__(self, coordenadasUbicación, descripción, historia, nombre, periodoActualización, region):
        """
        Constructor de la clase Bodega.

        Parámetros:
        - coordenadasUbicación: Las coordenadas de ubicación de la bodega.
        - descripción: La descripción de la bodega.
        - historia: La historia de la bodega.
        - nombre: El nombre de la bodega.
        - periodoActualización: El periodo de actualización de la bodega.
        - region: La región de la bodega.
        """
        self.coordenadasUbicación = coordenadasUbicación
        self.descripción = descripción
        self.historia = historia
        self.nombre = nombre
        self.periodoActualización = periodoActualización
        self.region = region

    def getNombre(self):
        """
        Obtiene el nombre de la bodega.

        Retorna:
        - El nombre de la bodega.
        """
        return self.nombre

    def obtenerRegionYPais(self):
        """
        Obtiene la región y el país de la bodega.

        Retorna:
        - La región de la bodega.
        - El país de la bodega.
        """
        region = self.region.getNombre()
        pais = self.region.obtenerPais()
        return region, pais
