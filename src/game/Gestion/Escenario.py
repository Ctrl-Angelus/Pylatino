from src.game.Clases.Sprite import Sprite
from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO, CANTIDAD_DE_TILES


class Escenario:
    def __init__(self, contexto):
        self.contexto = contexto
        self.fondo = Sprite("src/recursos/fondo.png", None)

        self.fondo.cuerpo.x = -(self.fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
        self.fondo.cuerpo.y = -(self.fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

        self.fondo_estatico = Sprite("src/recursos/fondo-estatico.png", (CANTIDAD_DE_TILES, CANTIDAD_DE_TILES))

    def mostrar(self):
        self.contexto.escena.blit(self.fondo_estatico.imagen, self.fondo_estatico.cuerpo)
        self.contexto.escena.blit(self.fondo.imagen, self.fondo.cuerpo)