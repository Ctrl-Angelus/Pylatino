import pygame
from pygame import Surface


class TileSet:
    def __init__(self, contexto, url: str, ancho: int, alto: int, espaciado: int):
        self.contexto = contexto
        self.archivo = pygame.image.load(url)
        self.tiles: dict[str, Surface] = {}

        ancho_total = self.archivo.width

        x = 0
        for i in range((ancho_total // ancho + espaciado) - espaciado):
            tile = obtener_tile(self.archivo, x, 0, ancho, alto)
            self.tiles[f"{i + 1}"] = tile
            x += ancho + espaciado



def obtener_tile(tiles: Surface, x, y, ancho, alto) -> Surface:
    rect = pygame.Rect(x, y, ancho, alto)
    superficie = tiles.subsurface(rect).copy()
    return superficie