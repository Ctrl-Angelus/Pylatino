
from src.game.Clases.EntidadBase import EntidadBase
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Movimiento.Movimiento import movimiento_relativo
from src.game.Colisiones.Colisiones_borde import colision_borde_enemigos
from src.game.Colisiones.Colisiones_entidades import colisiones_con_entidades


class Enemigo(EntidadBase):

    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, objetivo: tuple, contexto: ContextoDelJuego, jugador):
        super().__init__(posicion_inicial, velocidad, url, contexto)

        self.objetivo: tuple = objetivo
        self.jugador = jugador

    def mover(self):
        if self.contexto.movimiento_enemigos_activo:
            desplazamiento: tuple = movimiento_relativo(
                self.velocidad,
                self.cuerpo.center,
                self.objetivo
            )

            movimiento_x, movimiento_y = colision_borde_enemigos(
                self.cuerpo, desplazamiento,
                self.contexto.escenario.tile_map.borde,
                self.contexto.direccion_enemigos)

            colisiones_con_entidades(self, movimiento_x, movimiento_y, self.contexto.entidades, self.jugador)

    def modificar_objetivo(self, objetivo: tuple):
        self.objetivo = objetivo
