from src.game.Gestion.Contexto import ContextoDelJuego


def colisiones(entidad, movimiento_x: float, movimiento_y: float, entidades: list):

    entidad.mover(movimiento_x, 0)

    correccion_x = 0
    correccion_y = 0

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide_entidad = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_x > 0:
                correccion_x = entidad_lista.cuerpo.left - entidad.cuerpo.right

            elif movimiento_x < 0:
                correccion_x = entidad_lista.cuerpo.right - entidad.cuerpo.left

            entidad.mover(correccion_x, 0)

    entidad.mover(0, movimiento_y)

    for entidad_lista in entidades:
        if entidad_lista is entidad:
            continue

        collide_entidad = entidad.cuerpo.colliderect(entidad_lista.cuerpo)

        if collide_entidad:
            if movimiento_y > 0:
                correccion_y = entidad_lista.cuerpo.top - entidad.cuerpo.bottom

            elif movimiento_y < 0:
                correccion_y = entidad_lista.cuerpo.bottom - entidad.cuerpo.top

            entidad.mover(0, correccion_y)

def colision_tiles(entidad, movimiento_x: float, movimiento_y: float, contexto: ContextoDelJuego):
    simulacion_x = entidad.cuerpo.move(movimiento_x, 0)

    correccion_x = 0

    tiles_cercanos = contexto.escenario.tile_map.obtener_tiles_cercanos(simulacion_x)
    for tile in tiles_cercanos:
        if not tile.colision:
            continue

        if simulacion_x.colliderect(tile.cuerpo):

            if movimiento_x > 0:
                correccion_x = min(correccion_x, tile.cuerpo.left - simulacion_x.right)

            elif movimiento_x < 0:
                correccion_x = max(correccion_x, tile.cuerpo.right - simulacion_x.left)

    entidad.mover(movimiento_x + correccion_x, 0)


    simulacion_y = entidad.cuerpo.move(0, movimiento_y)

    correccion_y = 0

    tiles_cercanos = contexto.escenario.tile_map.obtener_tiles_cercanos(simulacion_y)
    for tile in tiles_cercanos:
        if not tile.colision:
            continue

        if simulacion_y.colliderect(tile.cuerpo):

            if movimiento_y > 0:
                correccion_y = min(correccion_y, tile.cuerpo.top - simulacion_y.bottom)

            elif movimiento_y < 0:
                correccion_y = max(correccion_y, tile.cuerpo.bottom - simulacion_y.top)

    entidad.mover(0, movimiento_y + correccion_y)