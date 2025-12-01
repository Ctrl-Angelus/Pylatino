import pygame
from pygame import Surface

from src.game.Gestion.Escenario import Escenario
from src.game.Gestion.Parametros import *


class ContextoDelJuego:
    def __init__(self):
        pygame.init()

        self.ejecutando = True

        self.display = pygame.display
        self.tiempo = pygame.time
        self.mouse = pygame.mouse
        self.teclas = pygame.key
        self.escena: Surface = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
        self.reloj = self.tiempo.Clock()
        self.get_ticks = pygame.time.get_ticks

        self.direccion_enemigos = 1
        self.movimiento_enemigos_activo = True
        self.entidades = []
        self.display.set_caption(TITULO)

        self.escenario = Escenario(self)

    def limpiar_entidades(self):
        self.entidades = []

    def terminar_game_loop(self):
        self.ejecutando = False

    def alternar_direccion_enemigos(self):
        self.direccion_enemigos *= -1

    def alternar_movimiento_enemigos(self):
        self.movimiento_enemigos_activo = not self.movimiento_enemigos_activo

    def obtener_ticks(self) -> int:
        return self.tiempo.get_ticks()

    def obtener_posicion_mouse(self) -> tuple:
        return self.mouse.get_pos()

    def obtener_teclas_presionadas(self):
        return self.teclas.get_pressed()