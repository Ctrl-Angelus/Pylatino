import pygame
from pygame import Surface

from src.game.Gestion.Escenario import Escenario
from src.game.Gestion.Parametros import *


class ContextoDelJuego:
    def __init__(self):
        pygame.init()

        self.ejecutando = True
        self.offset = [0, 0]

        self.fuente = pygame.font.Font("src/recursos/fuente/Medodica.otf", 60)

        self.escena: Surface = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
        self.reloj = pygame.time.Clock()

        self.movimiento_enemigos_activo = True
        self.entidades = []
        pygame.display.set_caption(TITULO)

        self.escenario = Escenario(self)
        self.administrador_de_entidades = None
        self.jugador = None

    def limpiar_entidades(self):
        self.entidades = []

    def terminar_game_loop(self):
        self.ejecutando = False

    def alternar_direccion_enemigos(self):
        for entidad in self.entidades:
            entidad.modificar_direccion()
        self.entidades[-1].modificar_direccion()

    def alternar_movimiento_enemigos(self):
        self.movimiento_enemigos_activo = not self.movimiento_enemigos_activo
