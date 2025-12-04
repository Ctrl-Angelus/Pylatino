
from src.game.Clases.EntidadBase import EntidadBase
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Colisiones.Colisiones_entidades import colisiones, colision_tiles


class Enemigo(EntidadBase):

    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego, jugador):
        super().__init__(posicion_inicial, velocidad, url, contexto)

        self.jugador = jugador

    def movimiento(self) -> None:
        if self.contexto.movimiento_enemigos_activo:
            movimiento_x, movimiento_y = movimiento_relativo(
                self.velocidad * self.modificador_de_velocidad,
                self.cuerpo.center,
                self.jugador.cuerpo.center
            )

            movimiento_x *= self.direccion
            movimiento_y *= self.direccion

            movimiento_x, movimiento_y = colision_tiles(self, movimiento_x, movimiento_y, self.contexto)
            colisiones(self, movimiento_x, movimiento_y, self.contexto.entidades)