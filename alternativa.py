class Alternativa:
    def __init__(self, contenido: str, pregunta, ayuda: str = None):
        self.contenido = contenido
        self.ayuda = ayuda
        self.pregunta = pregunta

    @property
    def contenido(self):
        return self.contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    @property
    def ayuda(self):
        return self.ayuda

    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda

    @property
    def pregunta(self):
        return self.pregunta