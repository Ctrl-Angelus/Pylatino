import pygame
from pygame import Surface

from src.game.Gestion.Escenario import Escenario
from src.game.Gestion.Parametros import *


class ContextoDelJuego:
    def __init__(self):
        pygame.init()

        self.ejecutando = True
        self.menu_activo = True
        self.reiniciar = False
        self.offset = [0, 0]

        self.fuente = pygame.font.Font("src/recursos/fuente/Medodica.otf", int(DIMENSIONES_DEL_LIENZO[0] * 0.05))

        self.escena: Surface = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
        self.reloj = pygame.time.Clock()

        self.movimiento_enemigos_activo = True
        self.entidades = []
        self.proyectiles = []
        pygame.display.set_caption(TITULO)

        self.escenario = Escenario(self)
        self.administrador_de_entidades = None
        self.jugador = None

        self.puntos = 0

    def limpiar_entidades(self):
        self.entidades = []

    def terminar_game_loop(self):
        self.ejecutando = False

    def alternar_direccion_enemigos(self):
        for entidad in self.entidades:
            if entidad is self.jugador:
                continue
            entidad.modificar_direccion()

    def alternar_movimiento_enemigos(self):
        for entidad in self.entidades:
            if entidad is self.jugador:
                continue
            entidad.tiene_movimiento = not entidad.tiene_movimiento
