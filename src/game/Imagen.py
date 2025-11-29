import pygame
from pygame import Rect, Surface
from Parametros import DIMENSIONES_DEL_LIENZO


class Imagen:
    def __init__(self, ruta: str, escalado_tiles: int):
        self.ruta: str = ruta

        imagen: Surface = pygame.image.load(self.ruta).convert()


        self.factor_escalado = (
                DIMENSIONES_DEL_LIENZO[0] / (imagen.width / escalado_tiles),
                DIMENSIONES_DEL_LIENZO[1] / (imagen.height / escalado_tiles)
        )

        self.imagen: Surface = pygame.transform.scale(imagen, (
            imagen.width * self.factor_escalado[0],
            imagen.height * self.factor_escalado[1]
        ))

        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.rect: Rect = self.imagen.get_rect()