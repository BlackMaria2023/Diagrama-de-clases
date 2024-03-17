from listado_respuestas import ListadoRespuestas
from encuesta import Encuesta

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta: Encuesta, respuestas: list):
        listado_respuestas = ListadoRespuestas(usuario=self, respuestas=respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)