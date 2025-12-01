import pygame
from pygame import Event

from src.game.Clases import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego


class Controlador:
    def __init__(self, contexto: ContextoDelJuego, jugador: Jugador):
        self.contexto = contexto
        self.jugador = jugador

    def verificar_eventos(self, evento: Event):
        if evento.type == pygame.QUIT:
            self.contexto.terminar_game_loop()

        if evento.type == self.jugador.controles["click"]:
            if evento.button == 1:
                self.contexto.alternar_direccion_enemigos()

            if evento.button == 2:
                self.realizar_dash()

            if evento.button == 3:
                self.jugador_intangible()

    def verificar_controles(self):
        teclas_presionadas = self.contexto.obtener_teclas_presionadas()

        if self.jugador.dash_activo:
            self.jugador.mover()

        elif teclas_presionadas[self.jugador.controles["adelante"]]:
            self.jugador.mover()

        elif teclas_presionadas[self.jugador.controles["atrás"]]:
            self.jugador.modificar_direccion("atras")
            self.jugador.modificar_velocidad(0.75)
            self.jugador.mover()
            self.jugador.modificar_velocidad(1)
            self.jugador.modificar_direccion("adelante")

    def realizar_dash(self):
        self.jugador.activar_dash()

    def jugador_intangible(self):
        self.contexto.alternar_movimiento_enemigos()
        self.jugador.alternar_colisiones()