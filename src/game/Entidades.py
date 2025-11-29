
import pygame
from pygame import Rect
from Movimiento import movimiento_relativo
from Colisiones_borde import desplazamiento_y_colision
from Parametros import MEDIDA_DE_TILE
from Colisiones_borde import desplazamiento_y_colision_enemigos
from Colisiones_entidades import colisiones_con_entidades


class Entidad:
    def __init__(self, posicion_inicial_x: float, posicion_inicial_y: float, alto, ancho, velocidad: float, url: str):

        self.imagen = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )

        self.cuerpo: Rect = self.sprite.get_rect()
        self.velocidad: float = velocidad

        self.cuerpo.x = posicion_inicial_x
        self.cuerpo.y = posicion_inicial_y

    def mover(self, objetivo: tuple, fondo: Rect, direccion: int, entidades: list):
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
            self.cuerpo.center,
            objetivo,
            MEDIDA_DE_TILE / 2,
            None
        )

        movimiento_x, movimiento_y = desplazamiento_y_colision_enemigos(self.cuerpo, desplazamiento, fondo, direccion)

        colisiones_con_entidades(self, movimiento_x, movimiento_y, entidades)


class Jugador(Entidad):
    controles = {
        "adelante": pygame.K_w,
        "atrás" : pygame.K_s,
        "click": pygame.MOUSEBUTTONDOWN
    }

    def mover(self, posicion_mouse: tuple, fondo: Rect, direccion: int, entidades: list[Entidad]) -> None:
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
                self.cuerpo.center,
                posicion_mouse,
                10,
            None
            )

        movimiento_x, movimiento_y = desplazamiento_y_colision(self.cuerpo, desplazamiento, fondo, direccion)

        for entidad in entidades:
            entidad.cuerpo.move_ip(
                movimiento_x, movimiento_y
            )

        fondo.move_ip(
            movimiento_x,
            movimiento_y
        )
