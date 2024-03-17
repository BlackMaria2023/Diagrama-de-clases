from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, encuesta, ayuda: str = None, requerida: bool = False, alternativas: list = None):
        self.enunciado = enunciado
        self.encuesta = encuesta
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = alternativas if alternativas else []

    @property
    def enunciado(self):
        return self.enunciado

    @property
    def encuesta(self):
        return self.encuesta

    @property
    def ayuda(self):
        return self.ayuda

    @property
    def requerida(self):
        return self.requerida

    @property
    def alternativas(self):
        return self.__alternativas