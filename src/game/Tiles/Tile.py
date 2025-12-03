from typing import Optional

from pygame import Surface

from src.game.Sprites.Sprite import Sprite


class Tile(Sprite):
    def __init__(self, ruta: Optional[str], tiles: Optional[tuple], imagen: Optional[Surface], x: int, y: int):
        super().__init__(ruta, tiles, imagen)

        self.x = x
        self.y = y

        self.cuerpo.x = self.x
        self.cuerpo.y = self.y