class Vino:
    def __init__(self, anada, fechaActualizacion, imagenEtiqueta, nombre, notaCataBodega, precioARS):
        self.anada = anada
        self.fechaActualizacion = fechaActualizacion
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaCataBodega = notaCataBodega
        self.precioARS = precioARS
        self.resena = []

    def mostrar_datos(self):
        print(self.anada)
        print(self.fechaActualizacion)
        print(self.imagenEtiqueta)
        print(self.nombre)
        print(self.notaCataBodega)
        print(self.precioARS)
        for i in range(len(self.resena)):
            self.resena[i].mostrar_datos()

    def agregar_resena(self, nueva_resena):
        self.resena.append(nueva_resena)


class Resena:
    def __init__(self, comentario, espremium, fecharesena, puntaje):
        self.comentario = comentario
        self.espremium = espremium
        self.fecharesena = fecharesena
        self.puntaje = puntaje

    def mostrar_datos(self):
        print(self.comentario)
        print(self.espremium)
        print(self.fecharesena)
        print(self.puntaje)


resena1 = Resena("Muy bueno", True, "22/05/2024", 10)
resena2 = Resena("Muy malo", False, "21/05/2024", 1)
Vino1 = Vino(1993, "14/05/2024", "imagen", "Balbo", 10, 1500)
Vino1.agregar_resena(resena1)
Vino1.agregar_resena(resena2)
Vino1.mostrar_datos()
