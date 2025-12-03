import pygame
from pygame import Rect, Surface

from src.game.Gestion.Parametros import *
from typing import Optional

class Sprite:
    def __init__(self, ruta: Optional[str], tiles: Optional[tuple], imagen: Optional[Surface]):

        if ruta is None:
            self.imagen = imagen

        if imagen is None:
            self.imagen: Surface = pygame.image.load(ruta).convert_alpha()

        if tiles is None:
            self.tiles_x: int = self.imagen.get_width() // MEDIDA_DE_TILE_ORIGINAL
            self.tiles_y: int = self.imagen.get_height() // MEDIDA_DE_TILE_ORIGINAL

        else:
            self.tiles_x, self.tiles_y = tiles

        self.escalado = (
            MEDIDA_DE_TILE_ORIGINAL * (MEDIDA_DE_TILE_ESCALADO / MEDIDA_DE_TILE_ORIGINAL) * self.tiles_x,
            MEDIDA_DE_TILE_ORIGINAL * (MEDIDA_DE_TILE_ESCALADO / MEDIDA_DE_TILE_ORIGINAL) * self.tiles_y
        )

        self.imagen: Surface = pygame.transform.scale(imagen, (
            self.escalado[0],
            self.escalado[1]
        ))

        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.cuerpo: Rect = self.imagen.get_rect()