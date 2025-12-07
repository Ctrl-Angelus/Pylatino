from typing import Optional

import pygame.time
from pygame import Surface

from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO
from src.game.Sonidos import sonido_cofre, sonido_salud
from src.game.Sprites.Sprite import Sprite


class Tile(Sprite):
    def __init__(self, ruta: Optional[str], tiles: Optional[tuple], imagen: Optional[Surface], x: int, y: int, contexto, id: str, colision: bool, tiene_accion: bool, tile_alterno):
        super().__init__(ruta, tiles, imagen)

        self.x = x
        self.y = y

        self.cuerpo.x = self.x
        self.cuerpo.y = self.y

        self.contexto = contexto

        self.id = id
        self.colision = colision
        self.tiene_accion = tiene_accion

        self.tile_alterno = tile_alterno


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

    def cambiar_tile(self):
        self.imagen = pygame.transform.scale(self.tile_alterno, (self.escalado[0], self.escalado[1]))

class TileConAccion(Tile):
    accionado = False
    duracion = 1000 # milisegundos
    inicio = 0
    ahora = 0

    def accionar(self):
        if self.tiene_accion:
            if not self.accionado:
                self.accionado = True
                self.inicio = pygame.time.get_ticks()
                self.accion()
            else:
                self.ahora = pygame.time.get_ticks()

                if self.ahora - self.inicio >= self.duracion:
                    self.accionado = False

    def accion(self):
        pass

class TileCuracion(TileConAccion):
    def accion(self):
        if self.contexto.jugador.vida == self.contexto.jugador.vida_total:
            return
        self.contexto.jugador.vida += 5

        if self.contexto.jugador.vida > self.contexto.jugador.vida_total:
            self.contexto.jugador.vida = self.contexto.jugador.vida_total

        self.tiene_accion = False
        self.cambiar_tile()
        sonido_salud()
        print("Curado")

class TileMunicion(TileConAccion):
    def accion(self):
        self.contexto.jugador.municion += 5
        self.tiene_accion = False
        self.colision = True
        self.cambiar_tile()
        sonido_cofre()
        print("Recarga")