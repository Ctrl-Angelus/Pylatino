import pygame
from pygame import Rect
from Movimiento import movimiento_respecto_al_mouse
from Colisiones import colision_con_el_limite

class Jugador:
    def __init__(self, posicion_inicial_x: float, posicion_inicial_y: float, alto, ancho, velocidad: float):
        sprite_original = pygame.image.load("src/recursos/jugador.png").convert_alpha()

        self.sprite = pygame.transform.scale(
            sprite_original,
            (
                sprite_original.get_width() * (alto / sprite_original.get_width()),
                sprite_original.get_height() * (ancho / sprite_original.get_height()),
            )
        )

        self.cuerpo: Rect = self.sprite.get_rect()
        self.velocidad: float = velocidad

        self.cuerpo.x = posicion_inicial_x
        self.cuerpo.y = posicion_inicial_y

        self.controles = {
            "adelante" : pygame.K_w
        }

    def mover(self, posicion_mouse: tuple, fondo: Rect) -> None:
        desplazamiento: tuple = movimiento_respecto_al_mouse(
            self.velocidad,
                self.cuerpo.center,
                posicion_mouse
            )

        fondo_con_desplazamiento: Rect = fondo.move(
            -desplazamiento[0],
            -desplazamiento[1]
        )

        # El movimiento por defecto lo da el desplazamiento original, se modifica en caso de ser necesario
        movimiento_x: float = -desplazamiento[0]
        movimiento_y: float = -desplazamiento[1]

        colisiones: dict = colision_con_el_limite(self.cuerpo, fondo_con_desplazamiento)

        # En caso de haber colisiones, se modifica el movimiento lo justo para que el personaje alcance el borde sin pasarlo
        if colisiones.get("izquierda"):
            movimiento_x = self.cuerpo.left - fondo.left

        elif colisiones.get("derecha"):
            movimiento_x = self.cuerpo.right - fondo.right

        if colisiones.get("arriba"):
            movimiento_y = self.cuerpo.top - fondo.top

        elif colisiones.get("abajo"):
            movimiento_y = self.cuerpo.bottom - fondo.bottom

        fondo.move_ip(
            movimiento_x,
            movimiento_y
        )
