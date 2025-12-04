from typing import Optional
from pygame import Surface

from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO
from src.game.Sprites.Sprite import Sprite


class Tile(Sprite):
    def __init__(self, ruta: Optional[str], tiles: Optional[tuple], imagen: Optional[Surface], x: int, y: int, contexto, id: str, colision: bool, tiene_accion: bool):
        super().__init__(ruta, tiles, imagen)

        self.x = x
        self.y = y

        self.cuerpo.x = self.x
        self.cuerpo.y = self.y

        self.contexto = contexto

        self.id = id
        self.colision = colision
        self.tiene_accion = tiene_accion

    def es_visible(self) -> bool:
        offset_x_inicial = self.contexto.offset[0]
        offset_y_inicial = self.contexto.offset[1]

        offset_x_final = DIMENSIONES_DEL_LIENZO[0] + self.contexto.offset[0]
        offset_y_final = DIMENSIONES_DEL_LIENZO[1] + self.contexto.offset[1]

        visibilidad_x = offset_x_inicial <= self.cuerpo.right and self.cuerpo.left <= offset_x_final

        visibilidad_y = offset_y_inicial <= self.cuerpo.bottom and self.cuerpo.top <= offset_y_final

        return visibilidad_x and visibilidad_y

    def obtener_posicion_visual(self) -> tuple:
        return self.cuerpo.x - self.contexto.offset[0], self.cuerpo.y - self.contexto.offset[1]

    def obtener_posicion(self) -> tuple:
        return self.cuerpo.centerx - self.contexto.offset[0], self.cuerpo.centery - self.contexto.offset[1]

class TileConAccion(Tile):
    def accion(self):
        print(f"accion realizada por: {self.id}")