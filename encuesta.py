class Encuesta:
    def __init__(self, nombre: str, preguntas=None):
        self.nombre = nombre
        self.__preguntas = preguntas if preguntas else []
        self.__listados_respuestas = []

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def preguntas(self):
        return self.__preguntas

    @property
    def listados_respuestas(self):
        return self.__listados_respuestas

    def mostrar_encuesta(self):
        print("Nombre de la encuesta:", self.nombre)
        print("Preguntas:")
        for pregunta in self.preguntas:
            print("- Enunciado:", pregunta.enunciado)
            if pregunta.ayuda:
                print("  Ayuda:", pregunta.ayuda)
            print("  Alternativas:")
            for alternativa in pregunta.alternativas:
                print("   - Contenido:", alternativa.contenido)
                if alternativa.ayuda:
                    print("     Ayuda:", alternativa.ayuda)

    def agregar_listado_respuestas(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int, preguntas=None):
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        return self.edad_minima

    @property
    def edad_maxima(self):
        return self.edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        usuario = listado_respuestas.usuario
        if self.edad_minima <= usuario.edad <= self.edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("El usuario no cumple con los requisitos de edad para responder esta encuesta.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: list, preguntas=None):
        super().__init__(nombre, preguntas)
        self.regiones = regiones

    @property
    def regiones(self):
        return self.__regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        usuario = listado_respuestas.usuario
        if usuario.region in self.regiones:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("El usuario no se encuentra en una región válida para responder esta encuesta.")