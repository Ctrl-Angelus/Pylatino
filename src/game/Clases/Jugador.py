import pygame

from src.game.Clases.EntidadBase import EntidadBase
from src.game.Clases.Proyectil import Proyectil
from src.game.Colisiones.Colisiones_entidades import colisiones
from src.game.Colisiones.Colisiones_tiles import colisiones_tiles
from src.game.Colisiones.Colisiones_con_empuje import colisiones_con_empuje
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, VELOCIDAD, DIMENSIONES_DEL_LIENZO
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Sonidos import sonido_dash, sonido_proyectil


class Jugador(EntidadBase):
    def __init__(self, contexto: ContextoDelJuego):

        posicion_inicial_x = contexto.escena.get_rect().center[0] - MEDIDA_DE_TILE_ESCALADO / 2
        posicion_inicial_y = contexto.escena.get_rect().center[1] - MEDIDA_DE_TILE_ESCALADO / 2
        velocidad = VELOCIDAD
        url = "src/recursos/jugador-spritesheet.png"

        super().__init__((posicion_inicial_x, posicion_inicial_y), velocidad, url, contexto, 4, 4)


        self.controles = {
            "adelante": pygame.K_w,
            "atrás" : pygame.K_s,
            "click": pygame.MOUSEBUTTONDOWN
        }

        self.animaciones = {
            "original": 0,
            "dash": 1,
            "daño": 2,
            "muerte": 3
        }

        self.dash_activo = False
        self.inicio_dash = 0
        self.duracion_dash = 500 # milisegundos
        self.duracion_disparo = 1000
        self.inicio_disparo = 0
        self.disparo_actual = 0
        self.disparo = False

        self.intangible = False
        self.puntos_de_daño = 5
        self.municion = 20

        self.muerte_duracion = 2000
        self.muerte_inicio = 0
        self.muerte_actual = 0

    def movimiento(self) -> None:
        if not self.tiene_movimiento:
            return

        if self.dash_activo:
            self.dash()

        mouse_x_mundo = pygame.mouse.get_pos()[0] + self.contexto.offset[0]
        mouse_y_mundo = pygame.mouse.get_pos()[1] + self.contexto.offset[1]

        movimiento_x, movimiento_y = movimiento_relativo(
            self.velocidad * self.modificador_de_velocidad,
                self.cuerpo.center,
                (mouse_x_mundo, mouse_y_mundo),
                None
            )

        movimiento_x *= self.direccion
        movimiento_y *= self.direccion

        if self.tiene_colisiones:
            movimiento_x, movimiento_y = colisiones_tiles(self, movimiento_x, movimiento_y, self.contexto)

            if self.dash_activo:
                colisiones_con_empuje(self, movimiento_x, movimiento_y, self.contexto.entidades)
            else:
                colisiones(self, self.contexto, movimiento_x, movimiento_y)


            tile_actual = self.contexto.escenario.tile_map.obtener_tile_actual(self.cuerpo)

            if tile_actual is None:
                self.morir()

            elif tile_actual.tiene_accion:
                tile_actual.accionar()
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
            self.iniciar_inmunidad()
            self.animacion_actual = self.animaciones["dash"]
            self.modificar_velocidad(3)
            sonido_dash()

    def dash(self) -> None:
        momento_actual = pygame.time.get_ticks()

        if momento_actual - self.inicio_dash >= self.duracion_dash:
            self.dash_activo = False
            self.modificar_velocidad(1)
            self.animacion_actual = self.animaciones["original"]
        elif momento_actual - self.inicio_dash >= self.duracion_dash * 0.25:
            self.modificar_velocidad(1.25)
        elif momento_actual - self.inicio_dash >= self.duracion_dash * 0.5:
            self.modificar_velocidad(1.5)
        elif momento_actual - self.inicio_dash >= self.duracion_dash * 0.75:
            self.modificar_velocidad(1.75)

    def es_intangible(self) -> bool:
        return self.intangible

    def morir(self):
        self.tiene_movimiento = False
        self.contexto.alternar_movimiento_enemigos()
        self.entidad_viva = False
        self.spritesheet.iniciar_animacion()
        self.animacion_actual = self.animaciones["muerte"]
        self.muerte_inicio = pygame.time.get_ticks()

    def mostrar(self):
        if self.invertido:
            self.contexto.escena.blit(
                pygame.transform.flip(self.spritesheet.obtener_sprite_actual().imagen, True, False),
                self.obtener_posicion_visual())
            self.spritesheet.animacion(self.animacion_actual)
        else:
            self.contexto.escena.blit(self.spritesheet.obtener_sprite_actual().imagen, self.obtener_posicion_visual())
            self.spritesheet.animacion(self.animacion_actual)

    def actualizar_muerte(self):
        if not self.entidad_viva:
            self.muerte_actual = pygame.time.get_ticks()
            if self.muerte_actual - self.muerte_inicio >= self.muerte_duracion:
                self.contexto.reiniciar = True

    def disparar(self):
        if self.municion <= 0:
            return

        if not self.disparo:
            self.inicio_disparo = pygame.time.get_ticks()
            self.disparo = True
            self.generar_proyectil()

        else:
            self.disparo_actual = pygame.time.get_ticks()

            if self.disparo_actual - self.inicio_disparo >= self.duracion_disparo:
                self.disparo = False

    def actualizar_disparo(self):
        if self.disparo:

            self.disparo_actual = pygame.time.get_ticks()

            if self.disparo_actual - self.inicio_disparo >= self.duracion_disparo:
                self.disparo = False

    def generar_proyectil(self):
        mouse_x_mundo = pygame.mouse.get_pos()[0] + self.contexto.offset[0]
        mouse_y_mundo = pygame.mouse.get_pos()[1] + self.contexto.offset[1]
        movimiento = movimiento_relativo(
            self.velocidad * 2,
            self.cuerpo.center,
            (mouse_x_mundo, mouse_y_mundo),
            None
        )
        self.contexto.proyectiles.append(
            Proyectil(
                self.contexto,
                "src/recursos/proyectil.png",
                MEDIDA_DE_TILE_ESCALADO / 2,
                MEDIDA_DE_TILE_ESCALADO / 2,
                movimiento,
                (
                    self.cuerpo.x,
                    self.cuerpo.y
                )
            )
        )
        sonido_proyectil()
        self.municion -= 1
