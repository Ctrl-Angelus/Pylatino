import pygame
from pygame import Rect, Surface
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, DIMENSIONES_DEL_LIENZO
from src.game.Gestion.Contexto import ContextoDelJuego


class EntidadBase:
    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego):

        alto = MEDIDA_DE_TILE_ESCALADO
        ancho = MEDIDA_DE_TILE_ESCALADO

        self.url: str = url
        self.imagen: Surface = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )
        self.cuerpo: Rect = self.sprite.get_rect().inflate(-10, -10)
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)
        self.contexto = contexto

        self.vida = 20
        self.vida_total = self.vida
        self.puntos_de_daño = 2

        self.duracion_inmunidad = 1000
        self.inmunidad = False
        self.inmunidad_inicio = 0
        self.inmunidad_actual = 0

        self.modificador_de_velocidad = 1
        self.direccion = 1
        self.colisiones = True

    def modificar_velocidad(self, factor) -> None:
        self.modificador_de_velocidad = factor

    def modificar_direccion(self):
            self.direccion *= -1

    def alternar_colisiones(self) -> None:
        self.colisiones = not self.colisiones

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
            self.iniciar_inmunidad()
            self.daño(puntos_de_daño)

        else:
            self.inmunidad_actual = pygame.time.get_ticks()
            if self.inmunidad_actual - self.inmunidad_inicio >= self.duracion_inmunidad:
                self.inmunidad = False

    def daño(self, puntos_de_daño: int):
        self.vida -= puntos_de_daño
        if self.vida <= 0:
            self.morir()

    def iniciar_inmunidad(self):
        self.inmunidad = True
        self.inmunidad_inicio = pygame.time.get_ticks()

    def morir(self):
        pass