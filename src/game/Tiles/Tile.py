from typing import Optional
from pygame import Surface

from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO
from src.game.Sprites.Sprite import Sprite


class Tile(Sprite):
    def __init__(self, ruta: Optional[str], tiles: Optional[tuple], imagen: Optional[Surface], x: int, y: int, contexto):
        super().__init__(ruta, tiles, imagen)

        self.x = x
        self.y = y

        self.cuerpo.x = self.x
        self.cuerpo.y = self.y

        self.contexto = contexto

    def es_visible(self) -> bool:
        visibilidad_x = self.contexto.offset[0] <= self.cuerpo.right and self.cuerpo.left <= DIMENSIONES_DEL_LIENZO[0] + self.contexto.offset[0]

        visibilidad_y = self.contexto.offset[1] <= self.cuerpo.bottom and self.cuerpo.top <= DIMENSIONES_DEL_LIENZO[1] + self.contexto.offset[1]
        return visibilidad_x and visibilidad_y

    def obtener_posicion(self) -> tuple:
        return self.cuerpo.centerx - self.contexto.offset[0], self.cuerpo.centery - self.contexto.offset[1]