import pygame

from src.game.Clases.EntidadBase import EntidadBase
from src.game.Colisiones.Colisiones_entidades import colisiones_con_entidades
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, VELOCIDAD, DIMENSIONES_DEL_LIENZO
from src.game.Gestion.Contexto import ContextoDelJuego


class Jugador(EntidadBase):
    def __init__(self, contexto: ContextoDelJuego):

        posicion_inicial_x = contexto.escena.get_rect().center[0] - MEDIDA_DE_TILE_ESCALADO / 2
        posicion_inicial_y = contexto.escena.get_rect().center[1] - MEDIDA_DE_TILE_ESCALADO / 2
        velocidad = VELOCIDAD
        url = "src/recursos/jugador.png"

        super().__init__((posicion_inicial_x, posicion_inicial_y), velocidad, url, contexto)


        self.controles = {
            "adelante": pygame.K_w,
            "atrás" : pygame.K_s,
            "click": pygame.MOUSEBUTTONDOWN
        }

        self.direcciones = {
            "adelante": 1,
            "atras": -1
        }

        self.direccion = self.direcciones["adelante"]

        self.modificador_de_velocidad = 1
        self.dash_activo = False
        self.inicio_dash = 0
        self.duracion_dash = 500 # milisegundos

        self.colisiones = True

    def movimiento(self) -> None:

        if self.dash_activo:
            self.dash()

        movimiento_x, movimiento_y = movimiento_relativo(
            self.velocidad * self.modificador_de_velocidad,
                self.obtener_posicion(),
                pygame.mouse.get_pos()
            )

        movimiento_x *= self.direccion
        movimiento_y *= self.direccion

        if self.colisiones:
            colisiones_con_entidades(self, movimiento_x, movimiento_y, self.contexto.entidades)

        else:
            self.mover(movimiento_x, movimiento_y)

    def mover(self, movimiento_x, movimiento_y) -> None:
        self.cuerpo.move_ip(movimiento_x, movimiento_y)

        self.contexto.offset[0] = self.cuerpo.centerx - DIMENSIONES_DEL_LIENZO[0] // 2
        self.contexto.offset[1] = self.cuerpo.centery - DIMENSIONES_DEL_LIENZO[1] // 2

    def activar_dash(self) -> None:
        if not self.dash_activo:
            self.dash_activo = True
            self.inicio_dash = pygame.time.get_ticks()

    def dash(self) -> None:
        momento_actual = pygame.time.get_ticks()
        self.modificar_velocidad(3)

        if momento_actual - self.inicio_dash >= self.duracion_dash * 0.75:
            self.modificar_velocidad(1.75)

        if momento_actual - self.inicio_dash >= self.duracion_dash * 0.5:
            self.modificar_velocidad(1.5)

        if momento_actual - self.inicio_dash >= self.duracion_dash * 0.25:
            self.modificar_velocidad(1.25)

        if momento_actual - self.inicio_dash >= self.duracion_dash:
            self.dash_activo = False
            self.modificar_velocidad(1)

    def modificar_velocidad(self, factor) -> None:
        self.modificador_de_velocidad = factor

    def alternar_colisiones(self) -> None:
        self.colisiones = not self.colisiones

    def tiene_colisiones(self) -> bool:
        return self.colisiones

    def modificar_direccion(self, direccion: str):
        if direccion in self.direcciones:
            self.direccion = self.direcciones[direccion]