class ListadoRespuestas:
    def __init__(self, usuario, encuesta):
        self.__usuario = usuario
        self.__encuesta = encuesta
        self.__respuestas = []

    @property
    def usuario(self):
        return self.__usuario

    @property
    def encuesta(self):
        return self.__encuesta

    @property
    def respuestas(self):
        return self.__respuestas

    def agregar_respuesta(self, respuesta):
        self.__respuestas.append(respuesta)