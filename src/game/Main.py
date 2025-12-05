import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS


def main():
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)

    administrador_de_entidades = AdministradorDeEntidades(contexto, jugador)
    administrador_de_entidades.generar_oleada(10)
    contexto.entidades.append(jugador)

    controlador = Controlador(contexto, jugador)

    while contexto.ejecutando:

        for evento in pygame.event.get():
            controlador.verificar_eventos(evento)

        controlador.verificar_controles()

        contexto.escenario.mostrar()

        for entidad in contexto.entidades:
            if entidad is not jugador:
                entidad.movimiento()

            if entidad.es_visible():
                contexto.escena.blit(entidad.sprite, entidad.obtener_posicion_visual())

        if jugador.vida > 0:
            contexto.escena.blit(jugador.sprite, jugador.obtener_posicion_visual())

        contexto.escena.blit(
            contexto.fuente.render(f"Vida: {jugador.vida}", True, (255, 255, 255)),
            (10, 10)
        )

        pygame.display.flip()
        contexto.reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
