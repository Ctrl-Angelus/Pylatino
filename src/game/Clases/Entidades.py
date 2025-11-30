import pygame
from pygame import Rect, Surface
import random

from src.game.Parametros import MEDIDA_DE_TILE
from src.game.Movimiento.Movimiento import movimiento_relativo, mover_fondo
from src.game.Colisiones.Colisiones_borde import colision_borde_jugador
from src.game.Colisiones.Colisiones_borde import colision_borde_enemigos
from src.game.Colisiones.Colisiones_entidades import colisiones_con_entidades


class Entidad:
    def __init__(self, posicion_inicial: tuple, alto, ancho, velocidad: float, url: str):

        self.url: str = url
        self.imagen: Surface = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )

        self.cuerpo: Rect = self.sprite.get_rect()
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)

class Enemigo(Entidad):

    def __init__(self, posicion_inicial: tuple, alto, ancho, velocidad: float, url: str, objetivos: list[tuple]):
        super().__init__(posicion_inicial, alto, ancho, velocidad, url)

        self.objetivo: tuple = random.choice(objetivos)

    def mover(self, fondo: Rect, direccion: int, entidades: list):
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
            self.cuerpo.center,
            self.objetivo,
            MEDIDA_DE_TILE / 2
        )

        movimiento_x, movimiento_y = colision_borde_enemigos(self.cuerpo, desplazamiento, fondo, direccion)

        colisiones_con_entidades(self, movimiento_x, movimiento_y, entidades)

class Jugador(Entidad):
    controles = {
        "adelante": pygame.K_w,
        "atrás" : pygame.K_s,
        "click": pygame.MOUSEBUTTONDOWN
    }

    def mover(self, posicion_mouse: tuple, fondo: Rect, direccion: int, entidades: list[Enemigo]) -> None:
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
                self.cuerpo.center,
                posicion_mouse,
                10
            )

        movimiento_x, movimiento_y = colision_borde_jugador(self.cuerpo, desplazamiento, fondo, direccion)

        mover_fondo(fondo, entidades, movimiento_x, movimiento_y)


