import random

from pygame import Rect

from src.game.Clases.Enemigo import Enemigo
from src.game.Clases.Jugador import Jugador
from src.game.Colisiones.Colisiones_entidades import posibles_colisiones
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Parametros import VELOCIDAD, MEDIDA_DE_TILE_ESCALADO


class AdministradorDeEntidades:
    def __init__(self, contexto: ContextoDelJuego, jugador: Jugador):
        self.contexto = contexto
        self.jugador = jugador

    def generar_oleada(self, cantidad: int):
        for _ in range(cantidad):
            posicion_libre = False

            while not posicion_libre:

                x_aleatoria = self.generar_x_aleatoria()
                y_aleatoria = self.generar_y_aleatoria()

                posible_cuerpo = Rect(x_aleatoria, y_aleatoria, MEDIDA_DE_TILE_ESCALADO, MEDIDA_DE_TILE_ESCALADO)

                posicion_libre = posibles_colisiones(posible_cuerpo, self.contexto)

                posicion_libre = False if posible_cuerpo.colliderect(self.jugador.cuerpo) else posicion_libre

            posicion_inicial = (x_aleatoria, y_aleatoria)
            velocidad_enemigos = VELOCIDAD * 0.4

            self.contexto.entidades.append(
                Enemigo(
                    posicion_inicial,
                    velocidad_enemigos,
                    "src/recursos/enemigo.png",
                    self.contexto,
                    self.jugador
                )
            )
    def generar_x_aleatoria(self) -> int:
        return random.randint(
                self.contexto.escenario.tile_map.borde.left,
                int(self.contexto.escenario.tile_map.borde.right - MEDIDA_DE_TILE_ESCALADO)
            )

    def generar_y_aleatoria(self) -> int:
        return random.randint(
            self.contexto.escenario.tile_map.borde.top,
            int(self.contexto.escenario.tile_map.borde.bottom - MEDIDA_DE_TILE_ESCALADO)
        )