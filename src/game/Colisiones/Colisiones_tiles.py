from src.game.Gestion.Contexto import ContextoDelJuego


def colisiones_tiles(entidad, movimiento_x: float, movimiento_y: float, contexto: ContextoDelJuego) -> tuple:
    simulacion_x = entidad.cuerpo.move(movimiento_x, 0)

    correccion_x = 0

    tiles_cercanos = contexto.escenario.tile_map.obtener_tiles_cercanos(simulacion_x)
    for tile in tiles_cercanos:
        if tile is None:
            continue
        if tile.tiene_accion:
            if simulacion_x.colliderect(tile.cuerpo):
                tile.accion()
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
        if tile is None:
            continue
        if tile.tiene_accion:
            if simulacion_y.colliderect(tile.cuerpo):
                tile.accion()
        if not tile.colision:
            continue

        if simulacion_y.colliderect(tile.cuerpo):

            if movimiento_y > 0:
                correccion_y = min(correccion_y, tile.cuerpo.top - simulacion_y.bottom)

            elif movimiento_y < 0:
                correccion_y = max(correccion_y, tile.cuerpo.bottom - simulacion_y.top)

    return movimiento_x + correccion_x, movimiento_y + correccion_y