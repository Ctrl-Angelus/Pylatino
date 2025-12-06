import pygame.image
from pygame import Surface

from src.game.Sprites.Sprite import Sprite

class SpriteSheet:
    def __init__(self, url: str):
        self.imagen = pygame.image.load(url).convert_alpha()
        self.matriz_de_sprites: list[list[Sprite]] = []

        self.coordenada_sprite_actual: list[int] = [0, 0]
        self.duracion_animacion = 500  # milisegundos
        self.inicio_animacion = 0
        self.momento_actual_animacion = 0
        self.animacion_activa = False

    def generar_frames(self, cantidad_de_columnas: int, cantidad_de_filas: int, dimensiones_del_sprite: tuple, tiles: tuple, espaciado):
        self.matriz_de_sprites = []

        coordenada_y = 0

        for _ in range(cantidad_de_filas):
            fila = []
            coordenada_x = 0
            for _ in range(cantidad_de_columnas):
                sprite = obtener_sprite(
                    self.imagen,
                    coordenada_x,
                    coordenada_y,
                    dimensiones_del_sprite[0],
                    dimensiones_del_sprite[1],
                    tiles
                )
                fila.append(sprite)
                coordenada_x += dimensiones_del_sprite[0] + espaciado

            self.matriz_de_sprites.append(fila)
            coordenada_y += dimensiones_del_sprite[1] + espaciado

    def obtener_sprite_actual(self) -> Sprite:
        fila = self.coordenada_sprite_actual[0]
        columna = self.coordenada_sprite_actual[1]
        return self.matriz_de_sprites[fila][columna]

    def iniciar_animacion(self):
        self.animacion_activa = True
        self.inicio_animacion = pygame.time.get_ticks()
        self.coordenada_sprite_actual[1] = 0

    def finalizar_animacion(self):
        self.animacion_activa = False

    def animacion(self, fila):
        self.coordenada_sprite_actual[0] = fila
        if self.animacion_activa:
            self.momento_actual_animacion = pygame.time.get_ticks()

            if self.momento_actual_animacion - self.inicio_animacion >= self.duracion_animacion:
                if self.coordenada_sprite_actual[1] < len(self.matriz_de_sprites[fila]) - 1:
                    self.coordenada_sprite_actual[1] += 1
                else:
                    self.coordenada_sprite_actual[1] = 0

                self.inicio_animacion = pygame.time.get_ticks()

def obtener_sprite(spritesheet: Surface, x, y, ancho, alto, tiles: tuple) -> Sprite:
    rect = pygame.Rect(x, y, ancho, alto)
    superficie = spritesheet.subsurface(rect).copy()
    return Sprite(None, (tiles[0], tiles[1]), superficie)