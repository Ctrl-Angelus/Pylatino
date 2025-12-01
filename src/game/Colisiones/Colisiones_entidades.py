
def colisiones_con_entidades(entidad, movimiento_x: float, movimiento_y: float, entidades: list, jugador):

    entidad.cuerpo.move_ip(movimiento_x, 0)

    correccion_x = 0
    correccion_y = 0

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide:
            if movimiento_x > 0:
                correccion_x = entidad_lista.cuerpo.left - entidad.cuerpo.right

            elif movimiento_x < 0:
                correccion_x = entidad_lista.cuerpo.right - entidad.cuerpo.left

            entidad.cuerpo.move_ip(correccion_x, 0)

    if jugador.tiene_colisiones():
        collide_x_jugador = entidad.cuerpo.colliderect(jugador.cuerpo)

        if collide_x_jugador:
            if movimiento_x > 0:
                correccion_x = jugador.cuerpo.left - entidad.cuerpo.right

            elif movimiento_x < 0:
                correccion_x = jugador.cuerpo.right - entidad.cuerpo.left

            entidad.cuerpo.move_ip(correccion_x, 0)

    entidad.cuerpo.move_ip(0, movimiento_y)

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide:
            if movimiento_y > 0:
                correccion_y = entidad_lista.cuerpo.top - entidad.cuerpo.bottom

            elif movimiento_y < 0:
                correccion_y = entidad_lista.cuerpo.bottom - entidad.cuerpo.top

            entidad.cuerpo.move_ip(0, correccion_y)

    if jugador.tiene_colisiones():
        collide_y_jugador = entidad.cuerpo.colliderect(jugador.cuerpo)

        if collide_y_jugador:
            if movimiento_y > 0:
                correccion_y = jugador.cuerpo.top - entidad.cuerpo.bottom

            elif movimiento_y < 0:
                correccion_y = jugador.cuerpo.bottom - entidad.cuerpo.top

            entidad.cuerpo.move_ip(0, correccion_y)