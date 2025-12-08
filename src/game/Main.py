import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS, DIMENSIONES_DEL_LIENZO



def main():
    enemigos_iniciales = 20
    cantidad_de_enemigos = enemigos_iniciales
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)
    contexto.jugador = jugador

    administrador_de_entidades = AdministradorDeEntidades(contexto)
    contexto.administrador_de_entidades = administrador_de_entidades
    contexto.administrador_de_entidades.generar_oleada(cantidad_de_enemigos)
    contexto.entidades.append(jugador)

    controlador = Controlador(contexto, jugador)

    pygame.mixer.music.load("src/recursos/audio/musica-fondo.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0.0)

    menu_original = pygame.image.load("src/recursos/interfaz/menu.png")

    menu = pygame.transform.scale(
        menu_original,
        (
            menu_original.get_width() * DIMENSIONES_DEL_LIENZO[0] / menu_original.get_width(),
            menu_original.get_height() * DIMENSIONES_DEL_LIENZO[1] / menu_original.get_height()
        )
    )

    instrucciones_originales = pygame.image.load("src/recursos/interfaz/instrucciones.png")

    instrucciones = pygame.transform.scale(
        instrucciones_originales,
        (
            instrucciones_originales.get_width() * DIMENSIONES_DEL_LIENZO[0] / instrucciones_originales.get_width(),
            instrucciones_originales.get_height() * DIMENSIONES_DEL_LIENZO[1] / instrucciones_originales.get_height()
        )
    )

    pantalla_muerte = pygame.image.load("src/recursos/interfaz/pantalla-muerte.png")

    muerte = pygame.transform.scale(
        pantalla_muerte,
        (
            pantalla_muerte.get_width() * DIMENSIONES_DEL_LIENZO[0] / pantalla_muerte.get_width(),
            pantalla_muerte.get_height() * DIMENSIONES_DEL_LIENZO[1] / pantalla_muerte.get_height()
        )
    )

    finalizado = pygame.image.load("src/recursos/interfaz/ronda-completada.png")

    ronda_finalizada = pygame.transform.scale(
        finalizado,
        (
            finalizado.get_width() * DIMENSIONES_DEL_LIENZO[0] / finalizado.get_width(),
            finalizado.get_height() * DIMENSIONES_DEL_LIENZO[1] / finalizado.get_height()
        )
    )

    aumento_oleada = False

    while contexto.ejecutando:

        if contexto.reiniciar:
            contexto = ContextoDelJuego()

            jugador = Jugador(contexto)
            contexto.jugador = jugador
            if cantidad_de_enemigos <= 45 and aumento_oleada:
                cantidad_de_enemigos += 5

            administrador_de_entidades = AdministradorDeEntidades(contexto)
            contexto.administrador_de_entidades = administrador_de_entidades
            contexto.administrador_de_entidades.generar_oleada(cantidad_de_enemigos)
            contexto.entidades.append(jugador)

            controlador = Controlador(contexto, jugador)
            contexto.reiniciar = False
            contexto.menu_activo = contexto.regresar_al_menu
            aumento_oleada = False


        if contexto.menu_activo:
            contexto.escena.blit(menu, (0, 0))
            creditos = contexto.fuente.render("Creado por Miguel Ortiz", True, (209, 194, 241))
            texto = contexto.fuente.render("Presione ENTER para Jugar", True, (255, 255, 255))
            contexto.escena.blit(texto, (
                DIMENSIONES_DEL_LIENZO[0] / 2 - texto.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.8
            ))
            contexto.escena.blit(
                creditos,
                (
                DIMENSIONES_DEL_LIENZO[0] / 2 - creditos.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.6
            ))
            pygame.display.flip()
            contexto.reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    contexto.terminar_game_loop()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        contexto.menu_activo = False
                        contexto.instrucciones_activas = True


            continue

        elif contexto.instrucciones_activas:
            contexto.escena.blit(instrucciones, (0, 0))
            texto = contexto.fuente.render("Presione ENTER para continuar", True, (255, 255, 255))
            contexto.escena.blit(texto, (
                DIMENSIONES_DEL_LIENZO[0] / 2 - texto.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.9
            ))
            pygame.display.flip()
            contexto.reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    contexto.terminar_game_loop()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        contexto.instrucciones_activas = False


            continue

        elif contexto.pantalla_final:
            contexto.escena.blit(ronda_finalizada, (0, 0))
            texto = contexto.fuente.render("Presione ENTER para ir al Menú", True, (255, 255, 255))
            contexto.escena.blit(texto, (
                DIMENSIONES_DEL_LIENZO[0] / 2 - texto.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.9
            ))
            pygame.display.flip()
            contexto.reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    contexto.terminar_game_loop()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        contexto.pantalla_final = False
                        contexto.reiniciar = True
                        contexto.regresar_al_menu = True
                        aumento_oleada = True


            continue

        elif contexto.pantalla_muerte:
            contexto.escena.blit(muerte, (0, 0))
            texto = contexto.fuente.render("Presione ENTER para reiniciar", True, (255, 255, 255))
            contexto.escena.blit(texto, (
                DIMENSIONES_DEL_LIENZO[0] / 2 - texto.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.9
            ))
            pygame.display.flip()
            contexto.reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    contexto.terminar_game_loop()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        contexto.pantalla_muerte = False
                        contexto.reiniciar = True
                        aumento_oleada = False
                        contexto.regresar_al_menu = False


            continue

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


        jugador.actualizar_muerte()
        jugador.mostrar()
        jugador.actualizar()
        jugador.actualizar_disparo()

        for proyectil in contexto.proyectiles:
            proyectil.mover()
            proyectil.mostrar()

        tamaño = contexto.fuente.get_height()
        imagen_1 = pygame.image.load("src/recursos/interfaz/barra-vida-2.png")

        barra_vida = pygame.transform.scale(
            imagen_1,
            (
                imagen_1.get_width() * tamaño / imagen_1.get_height(),
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )
        imagen_2 = pygame.image.load("src/recursos/interfaz/barra-vida-1.png")
        total = imagen_2.get_width() * tamaño / imagen_2.get_height()
        porcentaje = jugador.vida / jugador.vida_total
        barra_vida_contenido_original = pygame.transform.scale(
            imagen_2,
            (
                total,
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )

        barra_vida_contenido = pygame.transform.scale(
            imagen_2,
            (
                int(total * porcentaje),
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )

        contexto.escena.blit(barra_vida_contenido, (barra_vida.get_width() - barra_vida_contenido_original.get_width(), 10))
        contexto.escena.blit(barra_vida, (10, 10))

        enemigos_icono = pygame.image.load("src/recursos/interfaz/enemigo-icono.png")

        icono_enemigos = pygame.transform.scale(
            enemigos_icono,
            (
                enemigos_icono.get_width() * contexto.fuente.get_height() / enemigos_icono.get_width(),
                enemigos_icono.get_height() * contexto.fuente.get_height() / enemigos_icono.get_height(),
            )
        )

        enemigos_cantidad = contexto.fuente.render(f"{len(contexto.entidades) - 1}", True, (255, 255, 255))

        posicion_texto_enemigos = (DIMENSIONES_DEL_LIENZO[0] - enemigos_cantidad.get_width() - 10, 10)
        contexto.escena.blit(
            enemigos_cantidad,
            posicion_texto_enemigos
        )
        contexto.escena.blit(
            icono_enemigos,
            (
                posicion_texto_enemigos[0] - icono_enemigos.get_width() - 10,
                posicion_texto_enemigos[1]
            )
        )

        proyectiles = pygame.image.load("src/recursos/proyectil.png")
        icono_proyectiles = pygame.transform.scale(
            proyectiles,
            (
                proyectiles.get_width() * contexto.fuente.get_height() / proyectiles.get_width(),
                proyectiles.get_height() * contexto.fuente.get_height() / proyectiles.get_height()
            )
        )

        proyectiles_cantidad = contexto.fuente.render(f"{jugador.municion}", True, (255, 255, 255))

        posicion_texto_proyectiles = (
            DIMENSIONES_DEL_LIENZO[0] - proyectiles_cantidad.get_width() - 10,
            DIMENSIONES_DEL_LIENZO[1] - proyectiles_cantidad.get_height() - 10
        )
        contexto.escena.blit(
            proyectiles_cantidad,
            posicion_texto_proyectiles
        )
        contexto.escena.blit(
            icono_proyectiles,
            (
                posicion_texto_proyectiles[0] - icono_proyectiles.get_width() - 10,
                posicion_texto_proyectiles[1]
            )
        )

        if len(contexto.entidades) - 1 == 0:
            contexto.pantalla_final = True

        pygame.display.flip()
        contexto.reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
