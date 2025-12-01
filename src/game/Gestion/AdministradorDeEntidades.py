import random

from src.game.Clases.Enemigo import Enemigo
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Parametros import VELOCIDAD, MEDIDA_DE_TILE_ESCALADO


class AdministradorDeEntidades:
    def __init__(self, contexto: ContextoDelJuego, jugador: Jugador):
        self.contexto = contexto
        self.jugador = jugador

    def generar_oleada(self, cantidad: int):
        for _ in range(20):
            x_aleatoria = random.randint(
                self.contexto.escenario.fondo.cuerpo.left,
                int(self.contexto.escenario.fondo.cuerpo.right - MEDIDA_DE_TILE_ESCALADO)
            )

            y_aleatoria = random.randint(
                self.contexto.escenario.fondo.cuerpo.top,
                int(self.contexto.escenario.fondo.cuerpo.bottom - MEDIDA_DE_TILE_ESCALADO)
            )

            posicion_inicial = (x_aleatoria, y_aleatoria)
            velocidad_enemigos = VELOCIDAD * 0.4

            self.contexto.entidades.append(
                Enemigo(
                    posicion_inicial,
                    velocidad_enemigos,
                    "src/recursos/enemigo.png",
                    self.jugador.cuerpo.center,
                    self.contexto,
                    self.jugador
                )
            )