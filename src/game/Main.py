import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS, DIMENSIONES_DEL_LIENZO


def main():
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)
    contexto.jugador = jugador

    administrador_de_entidades = AdministradorDeEntidades(contexto)
    contexto.administrador_de_entidades = administrador_de_entidades
    contexto.administrador_de_entidades.generar_oleada(10)
    contexto.entidades.append(jugador)

    controlador = Controlador(contexto, jugador)

    while contexto.ejecutando:

        for evento in pygame.event.get():
            controlador.verificar_eventos(evento)

        controlador.verificar_controles()

        contexto.escenario.mostrar()

        for entidad in contexto.entidades:
            if entidad is jugador:
                continue
            entidad.actualizar_muerte()
            entidad.movimiento()
            entidad.actualizar()

            if entidad.es_visible():
                entidad.mostrar()

        jugador.mostrar()
        jugador.actualizar()

        contexto.escena.blit(
            contexto.fuente.render(f"Vida: {jugador.vida} / {jugador.vida_total}", True, (255, 255, 255)),
            (10, 10)
        )
        contexto.escena.blit(
            contexto.fuente.render(f"Enemigos: {len(contexto.entidades) - 1}", True, (255, 255, 255)),
            (10, DIMENSIONES_DEL_LIENZO[1] - contexto.fuente.get_height() - 10)
        )
        if len(contexto.entidades) == 1:
            print("Ganaste la ronda")
            contexto.administrador_de_entidades.generar_oleada(10)

        pygame.display.flip()
        contexto.reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
