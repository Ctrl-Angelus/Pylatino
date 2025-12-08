import pygame
from pygame import Rect

from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO, MEDIDA_DE_TILE_ORIGINAL
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Sonidos import sonido_golpe, sonido_muerte
from src.game.Sprites.SpriteSheet import SpriteSheet


class EntidadBase:
    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego, filas, columnas):

        alto = MEDIDA_DE_TILE_ORIGINAL
        ancho = MEDIDA_DE_TILE_ORIGINAL

        self.url: str = url
        self.spritesheet = SpriteSheet(url)
        self.spritesheet.generar_frames(
            columnas,
            filas,
            (ancho, alto),
            (1, 1),
            1
        )
        self.spritesheet.iniciar_animacion()
        self.cuerpo: Rect = self.spritesheet.obtener_sprite_actual().imagen.get_rect().inflate(-10, -10)
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)
        self.contexto = contexto

        self.vida = 20
        self.vida_total = self.vida
        self.puntos_de_daño = 4

        self.duracion_inmunidad = 1000
        self.inmunidad = False
        self.inmunidad_inicio = 0
        self.inmunidad_actual = 0

        self.modificador_de_velocidad = 1
        self.direccion = 1
        self.tiene_colisiones = True
        self.entidad_viva = True
        self.tiene_movimiento = True
        self.invertido = False

        self.animaciones = {
            "original": 0,
            "daño": 1,
            "muerte": 2
        }

        self.animacion_actual = self.animaciones["original"]

    def modificar_velocidad(self, factor) -> None:
        self.modificador_de_velocidad = factor

    def modificar_direccion(self):
            self.direccion *= -1

    def alternar_colisiones(self) -> None:
        self.tiene_colisiones = not self.tiene_colisiones

    def obtener_posicion_visual(self) -> tuple:
        return self.cuerpo.x - self.contexto.offset[0], self.cuerpo.y - self.contexto.offset[1]

    def mover(self, movimiento_x, movimiento_y) -> None:
        self.cuerpo.move_ip(movimiento_x, movimiento_y)

    def es_visible(self) -> bool:
        offset_x_inicial = self.contexto.offset[0]
        offset_y_inicial = self.contexto.offset[1]

        offset_x_final = DIMENSIONES_DEL_LIENZO[0] + self.contexto.offset[0]
        offset_y_final = DIMENSIONES_DEL_LIENZO[1] + self.contexto.offset[1]

        visibilidad_x = self.cuerpo.right >= offset_x_inicial and self.cuerpo.left <= offset_x_final

        visibilidad_y = self.cuerpo.bottom >= offset_y_inicial and self.cuerpo.top <= offset_y_final

        return visibilidad_x and visibilidad_y

    def realizar_daño(self, puntos_de_daño: int):
        if not self.inmunidad:
            if self.entidad_viva:
                self.iniciar_inmunidad()
                muerte = self.daño(puntos_de_daño)
                if muerte:
                    sonido_muerte()
                    return

                sonido_golpe()

                self.animacion_actual = self.animaciones["daño"]

        else:
            self.inmunidad_actual = pygame.time.get_ticks()
            if self.inmunidad_actual - self.inmunidad_inicio >= self.duracion_inmunidad:
                if self.entidad_viva:
                    self.animacion_actual = self.animaciones["original"]
                self.inmunidad = False

    def daño(self, puntos_de_daño: int) -> bool:
        self.vida -= puntos_de_daño

        if self.vida <= 0:
            self.morir()
            return True
        return False

    def iniciar_inmunidad(self):
        self.inmunidad = True
        self.inmunidad_inicio = pygame.time.get_ticks()

    def actualizar(self):
        if self.inmunidad:
            ahora = pygame.time.get_ticks()
            if ahora - self.inmunidad_inicio >= self.duracion_inmunidad:
                self.inmunidad = False
                if self.entidad_viva:
                    self.animacion_actual = self.animaciones["original"]

    def morir(self):
        pass