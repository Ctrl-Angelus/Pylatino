from typing import Optional

import pygame.time

from src.game.Clases.EntidadBase import EntidadBase
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Colisiones.Colisiones_entidades import colisiones, colision_tiles


class Enemigo(EntidadBase):

    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego, jugador):
        super().__init__(posicion_inicial, velocidad, url, contexto)

        self.jugador = jugador
        self.empuje = False
        self.empuje_x = 0
        self.empuje_y = 0
        self.empuje_duracion = 500 # milisegundos
        self.inicio = 0
        self.ahora = 0

    def movimiento(self) -> None:

        if self.contexto.movimiento_enemigos_activo:
            if self.empuje:
                self.empujar()
                movimiento_x = self.empuje_x
                movimiento_y = self.empuje_y

            else:
                movimiento_x, movimiento_y = movimiento_relativo(
                    self.velocidad * self.modificador_de_velocidad,
                    self.cuerpo.center,
                    self.jugador.cuerpo.center
                )

                movimiento_x *= self.direccion
                movimiento_y *= self.direccion

            movimiento_x, movimiento_y = colision_tiles(self, movimiento_x, movimiento_y, self.contexto)
            colisiones(self, movimiento_x, movimiento_y, self.contexto.entidades)

    def empujar(self):
        if self.empuje:
            self.ahora = pygame.time.get_ticks()

            if self.ahora - self.inicio >= self.empuje_duracion:
                self.empuje = False
                self.empuje_x = 0
                self.empuje_y = 0

    def iniciar_empuje(self, movimiento_x, movimiento_y):
        if not self.empuje:
            self.empuje = True
            self.inicio = pygame.time.get_ticks()
            self.empuje_x = movimiento_x
            self.empuje_y = movimiento_y