import pygame

from src.game.Clases.EntidadBase import EntidadBase
from src.game.Movimiento.Movimiento import movimiento_relativo, mover_fondo
from src.game.Colisiones.Colisiones_borde import colision_borde_jugador
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, VELOCIDAD
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
            "adelante": -1,
            "atras": 1
        }

        self.direccion = self.direcciones["adelante"]

        self.modificador_de_velocidad = 1
        self.dash_activo = False
        self.inicio_dash = 0
        self.duracion_dash = 500 # milisegundos

        self.colisiones = True

    def mover(self) -> None:

        if self.dash_activo:
            self.dash()

        desplazamiento: tuple = movimiento_relativo(
            self.velocidad * self.modificador_de_velocidad,
                self.cuerpo.center,
                pygame.mouse.get_pos()
            )

        movimiento_x, movimiento_y = colision_borde_jugador(self.cuerpo, desplazamiento, self.contexto.escenario.tile_map.borde, self.direccion)

        if self.colisiones:

            correccion_x = 0
            correccion_y = 0

            mover_fondo(self.contexto, movimiento_x, 0)

            for entidad in self.contexto.entidades:
                colision = self.cuerpo.colliderect(entidad.cuerpo)

                if colision:
                    if movimiento_x > 0:
                        correccion_x = self.cuerpo.left - entidad.cuerpo.right

                    elif movimiento_x < 0:
                        correccion_x = self.cuerpo.right - entidad.cuerpo.left

                    mover_fondo(self.contexto, correccion_x, 0)

            mover_fondo(self.contexto,0, movimiento_y)

            for entidad in self.contexto.entidades:
                colision = self.cuerpo.colliderect(entidad.cuerpo)

                if colision:
                    if movimiento_y > 0:
                        correccion_y = self.cuerpo.top - entidad.cuerpo.bottom

                    elif movimiento_y < 0:
                        correccion_y = self.cuerpo.bottom - entidad.cuerpo.top

                    mover_fondo(self.contexto, 0, correccion_y)

        else:
            mover_fondo(self.contexto, movimiento_x, movimiento_y)


    def activar_dash(self):
        if not self.dash_activo:
            self.dash_activo = True
            self.inicio_dash = pygame.time.get_ticks()

    def dash(self):
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