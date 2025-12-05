import pygame.time

from src.game.Clases.EntidadBase import EntidadBase
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Colisiones.Colisiones_entidades import colisiones
from src.game.Colisiones.Colisiones_tiles import colisiones_tiles


class Enemigo(EntidadBase):

    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego):
        super().__init__(posicion_inicial, velocidad, url, contexto)

        self.empuje = False
        self.empuje_x = 0
        self.empuje_y = 0
        self.empuje_duracion = 400 # milisegundos
        self.empuje_inicio = 0
        self.empuje_actual = 0

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
                    self.contexto.jugador.cuerpo.center,
                    DIMENSIONES_DEL_LIENZO[0] / 2
                )

                movimiento_x *= self.direccion
                movimiento_y *= self.direccion

            movimiento_x, movimiento_y = colisiones_tiles(self, movimiento_x, movimiento_y, self.contexto)
            colisiones(self, self.contexto, movimiento_x, movimiento_y)

            tile_actual = self.contexto.escenario.tile_map.obtener_tile_actual(self.cuerpo)

            if tile_actual is None:
                self.morir()

    def empujar(self):
        if self.empuje:
            self.empuje_actual = pygame.time.get_ticks()

            if self.empuje_actual - self.empuje_inicio >= self.empuje_duracion:
                self.empuje = False
                self.empuje_x = 0
                self.empuje_y = 0

    def iniciar_empuje(self, movimiento_x, movimiento_y):
        if not self.empuje:
            self.empuje = True
            self.empuje_inicio = pygame.time.get_ticks()
            self.empuje_x = movimiento_x
            self.empuje_y = movimiento_y

    def morir(self):
        self.contexto.entidades.remove(self)