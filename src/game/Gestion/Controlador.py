import pygame
from pygame import Event

from src.game.Clases import Jugador
from src.game.Colisiones.Posibles_colisiones import posibles_colisiones_jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Movimiento.Angulo import calcular_angulo


class Controlador:
    def __init__(self, contexto: ContextoDelJuego, jugador: Jugador):
        self.contexto = contexto
        self.jugador = jugador

    def verificar_eventos(self, evento: Event):
        if evento.type == pygame.QUIT:
            self.contexto.terminar_game_loop()

        if evento.type == pygame.MOUSEMOTION:
            mouse_x_mundo = pygame.mouse.get_pos()[0] + self.contexto.offset[0]
            mouse_y_mundo = pygame.mouse.get_pos()[1] + self.contexto.offset[1]

            angulo = calcular_angulo(self.jugador.cuerpo.center, (mouse_x_mundo, mouse_y_mundo))

            self.jugador.invertido = angulo > 90 or angulo < -90

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:
                self.jugador.disparar()

            # Habilidades del jugador para usar en un futuro
            """ 
            if evento.button == 2:
                self.contexto.alternar_direccion_enemigos()
            if evento.button == 3:
                if self.jugador.es_intangible():

                    posicion_libre = posibles_colisiones_jugador(self.jugador, self.contexto)

                    if posicion_libre:
                        self.jugador_intangible()
                    else:
                        print("Esta área tiene tiene_colisiones o está fuera del mapa")

                else:
                    self.jugador_intangible()

            """

    def verificar_controles(self):
        teclas_presionadas = pygame.key.get_pressed()
        dash = self.jugador.dash_activo
        adelante = teclas_presionadas[self.jugador.controles["adelante"]]
        atras = teclas_presionadas[self.jugador.controles["atrás"]]

        if teclas_presionadas[pygame.K_ESCAPE]:
            self.contexto.reiniciar = True
            self.contexto.regresar_al_menu = False

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