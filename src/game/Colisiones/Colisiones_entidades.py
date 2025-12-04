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

def colision_tiles(entidad, movimiento_x: float, movimiento_y: float, contexto: ContextoDelJuego) -> tuple:
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

    simulacion_y = entidad.cuerpo.move(movimiento_x + correccion_x, movimiento_y)

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

    return movimiento_x + correccion_x, movimiento_y + correccion_y


def posibles_colisiones(rect, contexto: ContextoDelJuego):
    tiles = contexto.escenario.tile_map.obtener_tiles_cercanos(rect)
    tiles_seguros = 0
    entidades_seguras = 0
    for tile in tiles:
        if not tile.colision or not tile.cuerpo.colliderect(rect):
            tiles_seguros += 1

    for entidad_lista in contexto.entidades:
        if not entidad_lista.cuerpo.colliderect(rect):
            entidades_seguras += 1

    return tiles_seguros == len(tiles) and entidades_seguras == len(contexto.entidades)

def posibles_colisiones_jugador(jugador, contexto: ContextoDelJuego):
    tile_actual = contexto.escenario.tile_map.obtener_tile_actual(jugador.cuerpo)
    if tile_actual is None:
        return False

    tiles = contexto.escenario.tile_map.obtener_tiles_cercanos(jugador.cuerpo)
    tiles_seguros = 0
    entidades_seguras = 0

    for tile in tiles:
        if not tile.colision or not tile.cuerpo.colliderect(jugador.cuerpo):
            tiles_seguros += 1

    for entidad_lista in contexto.entidades:
        if not entidad_lista.cuerpo.colliderect(jugador.cuerpo) or jugador is entidad_lista:
            entidades_seguras += 1

    return tiles_seguros == len(tiles) and entidades_seguras == len(contexto.entidades)