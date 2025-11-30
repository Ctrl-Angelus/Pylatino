import pygame
from pygame import Rect, Surface

from src.game.Parametros import *


class Sprite:
    def __init__(self, ruta: str, tiles):
        self.ruta: str = ruta

        imagen: Surface = pygame.image.load(self.ruta).convert()

        if tiles is None:
            self.tiles_x = imagen.get_width() // TAMAÑO_TILE_ORIGINAL
            self.tiles_y = imagen.get_height() // TAMAÑO_TILE_ORIGINAL

        else:
            self.tiles_x, self.tiles_y = tiles

        self.escalado = (
                TAMAÑO_TILE_ORIGINAL * (MEDIDA_DE_TILE / TAMAÑO_TILE_ORIGINAL) * self.tiles_x,
                TAMAÑO_TILE_ORIGINAL * (MEDIDA_DE_TILE / TAMAÑO_TILE_ORIGINAL) * self.tiles_y
        )

        self.imagen: Surface = pygame.transform.scale(imagen, (
            self.escalado[0],
            self.escalado[1]
        ))

        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.cuerpo: Rect = self.imagen.get_rect()