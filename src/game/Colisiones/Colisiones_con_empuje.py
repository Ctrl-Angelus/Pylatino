
def colisiones_con_empuje(jugador, movimiento_x: float, movimiento_y: float, entidades: list):
    jugador.mover(movimiento_x, 0)

    correccion_x = 0
    correccion_y = 0

    for entidad_lista in entidades:
        if entidad_lista is jugador:
            continue

        collide_entidad = jugador.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_x > 0:
                correccion_x = entidad_lista.cuerpo.left - jugador.cuerpo.right

            elif movimiento_x < 0:
                correccion_x = entidad_lista.cuerpo.right - jugador.cuerpo.left

            jugador.mover(correccion_x, 0)
            entidad_lista.iniciar_empuje(movimiento_x / 2, 0)
            entidad_lista.realizar_daño(jugador.puntos_de_daño)

    jugador.mover(0, movimiento_y)

    for entidad_lista in entidades:
        if entidad_lista is jugador:
            continue

        collide_entidad = jugador.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_y > 0:
                correccion_y = entidad_lista.cuerpo.top - jugador.cuerpo.bottom

            elif movimiento_y < 0:
                correccion_y = entidad_lista.cuerpo.bottom - jugador.cuerpo.top

            jugador.mover(0, correccion_y)

            entidad_lista.iniciar_empuje(0, movimiento_y / 2)
            entidad_lista.realizar_daño(jugador.puntos_de_daño)