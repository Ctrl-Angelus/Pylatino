import math

import pygame
from pygame import Rect
from Parametros import TAMAÑO

class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo: Rect = cuerpo
        self.velocidad: float = velocidad

        self.controles = {
            pygame.K_w: (0, -self.velocidad),
            pygame.K_a: (-self.velocidad, 0),
            pygame.K_s: (0, self.velocidad),
            pygame.K_d: (self.velocidad, 0)
        }

    def colision_limite(self, limites: list, movimiento: tuple) -> bool:
        posicion_inicial_x = self.cuerpo.x
        posicion_inicial_y = self.cuerpo.y

        posicion_final_x = posicion_inicial_x + movimiento[0]
        posicion_final_y = posicion_inicial_y + movimiento[1]

        limite_x = limites[0] - TAMAÑO
        limite_y = limites[1] - TAMAÑO

        colision_inicial_x = posicion_final_x < 0
        colision_final_x = posicion_final_x > limite_x

        colision_inicial_y = posicion_final_y < 0
        colision_final_y = posicion_final_y > limite_y

        colision_x = colision_inicial_x or colision_final_x
        colision_y = colision_inicial_y or colision_final_y

        if colision_inicial_x:
            self.cuerpo.move_ip(0 - posicion_inicial_x, 0)
        elif colision_final_x:
            self.cuerpo.move_ip(limite_x - posicion_inicial_x, 0)

        if colision_inicial_y:
            self.cuerpo.move_ip(0, 0 - posicion_inicial_y)
        elif colision_final_y:
            self.cuerpo.move_ip(0, limite_y - posicion_inicial_y)

        return colision_x or colision_y

    def mover(self, teclas, limites: list) -> None:

        teclas_presionadas = 0
        for clave, valor in self.controles.items():
            if teclas[clave]:
                teclas_presionadas += 1

        if teclas_presionadas == 2:
            factor = math.sin(math.radians(45))
        else:
            factor = 1

        for clave, movimiento in self.controles.items():
            if teclas[clave]:
                if self.colision_limite(limites, movimiento):
                    continue
                else:
                    self.cuerpo.move_ip(
                        movimiento[0] * factor,
                        movimiento[1] * factor
                    )