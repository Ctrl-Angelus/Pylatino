
def colisiones(entidad, contexto, movimiento_x: float, movimiento_y: float):

    entidad.mover(movimiento_x, 0)

    correccion_x = 0
    correccion_y = 0

    for entidad_lista in contexto.entidades:
        if entidad_lista is entidad:
            continue

        if not entidad_lista.tiene_colisiones:
            continue

        collide_entidad = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_x > 0:
                correccion_x = entidad_lista.cuerpo.left - entidad.cuerpo.right

            elif movimiento_x < 0:
                correccion_x = entidad_lista.cuerpo.right - entidad.cuerpo.left

            entidad.mover(correccion_x, 0)

            if entidad_lista is contexto.jugador:
                contexto.jugador.realizar_daño(entidad.puntos_de_daño)

    entidad.mover(0, movimiento_y)

    for entidad_lista in contexto.entidades:
        if entidad_lista is entidad:
            continue

        if not entidad_lista.tiene_colisiones:
            continue

        collide_entidad = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_y > 0:
                correccion_y = entidad_lista.cuerpo.top - entidad.cuerpo.bottom

            elif movimiento_y < 0:
                correccion_y = entidad_lista.cuerpo.bottom - entidad.cuerpo.top

            entidad.mover(0, correccion_y)
            if entidad_lista is contexto.jugador:
                contexto.jugador.realizar_daño(entidad.puntos_de_daño)
