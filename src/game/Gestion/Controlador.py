import pygame
from pygame import Event

from src.game.Clases import Jugador
from src.game.Colisiones.Colisiones_entidades import posibles_colisiones_jugador
from src.game.Gestion.Contexto import ContextoDelJuego


class Controlador:
    def __init__(self, contexto: ContextoDelJuego, jugador: Jugador):
        self.contexto = contexto
        self.jugador = jugador

    def verificar_eventos(self, evento: Event):
        if evento.type == pygame.QUIT:
            self.contexto.terminar_game_loop()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:
                self.contexto.alternar_direccion_enemigos()

            if evento.button == 3:
                if self.jugador.es_intangible():

                    posicion_libre = posibles_colisiones_jugador(self.jugador, self.contexto)

                    if posicion_libre:
                        self.jugador_intangible()
                    else:
                        print("Esta área tiene colisiones o está fuera del mapa")

                else:
                    self.jugador_intangible()

            if evento.button == 6:
                self.contexto.limpiar_entidades()

    def verificar_controles(self):
        teclas_presionadas = pygame.key.get_pressed()
        dash = self.jugador.dash_activo
        adelante = teclas_presionadas[self.jugador.controles["adelante"]]
        atras = teclas_presionadas[self.jugador.controles["atrás"]]

        if teclas_presionadas[pygame.K_SPACE]:
            self.realizar_dash()

        if dash:
            self.jugador.movimiento()

        elif adelante:
            self.jugador.movimiento()

        elif atras:
            self.jugador.modificar_direccion()
            self.jugador.modificar_velocidad(0.75)
            self.jugador.movimiento()
            self.jugador.modificar_velocidad(1)
            self.jugador.modificar_direccion()

    def realizar_dash(self):
        self.jugador.activar_dash()

    def jugador_intangible(self):
        self.contexto.alternar_movimiento_enemigos()
        self.jugador.alternar_colisiones()
        self.jugador.intangible = not self.jugador.intangible