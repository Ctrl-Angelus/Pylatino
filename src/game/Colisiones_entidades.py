
def colisiones_con_entidades(entidad, movimiento_x: float, movimiento_y: float, entidades: list):
    entidad.cuerpo.move_ip(
        movimiento_x,
        0
    )

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide:
            if movimiento_x > 0:
                correccion = entidad_lista.cuerpo.left - entidad.cuerpo.right
                entidad.cuerpo.move_ip(correccion, 0)

            elif movimiento_x < 0:
                correccion = entidad_lista.cuerpo.right - entidad.cuerpo.left
                entidad.cuerpo.move_ip(correccion, 0)

    entidad.cuerpo.move_ip(
        0,
        movimiento_y
    )

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide:
            if movimiento_y > 0:
                correccion = entidad_lista.cuerpo.top - entidad.cuerpo.bottom
                entidad.cuerpo.move_ip(0, correccion)

            elif movimiento_y < 0:
                correccion = entidad_lista.cuerpo.bottom - entidad.cuerpo.top
                entidad.cuerpo.move_ip(0, correccion)