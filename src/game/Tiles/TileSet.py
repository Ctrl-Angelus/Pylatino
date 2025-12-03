import pygame
from pygame import Surface


class TileSet:
    def __init__(self, url: str, ancho: int, alto: int, espaciado: int):
        self.archivo = pygame.image.load(url).convert_alpha()
        self.tiles: list[list[Surface]] = []

        ancho_total = self.archivo.get_width()
        alto_total = self.archivo.get_height()

        for y in range(0, alto_total, alto + espaciado):
            fila = []
            for x in range(0, ancho_total, ancho + espaciado):
                rect = pygame.Rect(x, y, ancho, alto)
                tile = self.archivo.subsurface(rect)
                fila.append(tile)
            self.tiles.append(fila)
