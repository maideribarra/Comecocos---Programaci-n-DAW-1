
import os
import random


    # ==============================
    # FUNCIONES
    # ==============================


def mover_fantasma(tablero, estado):
    """El fantasma se mueve aleatoriamente."""

    fantasma_fila = estado[2]
    fantasma_columna = estado[3]

    movimientos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    random.shuffle(movimientos)

    for movimiento in movimientos:

        nueva_fila = fantasma_fila + movimiento[0]
        nueva_columna = fantasma_columna + movimiento[1]

        if tablero[nueva_fila][nueva_columna] != "#":
            fantasma_fila = nueva_fila
            fantasma_columna = nueva_columna
            break

    nuevo_estado = [
        estado[0],
        estado[1],
        fantasma_fila,
        fantasma_columna,
        estado[4],
        estado[5]
    ]

    return nuevo_estado


def comprobar_colision(estado):
    """Comprueba si el jugador ha sido alcanzado por el fantasma."""

    jugador_fila = estado[0]
    jugador_columna = estado[1]
    fantasma_fila = estado[2]
    fantasma_columna = estado[3]
    vidas = estado[5]

    if jugador_fila == fantasma_fila and jugador_columna == fantasma_columna:

        vidas -= 1

        print("¡El fantasma te ha atrapado!")

        # Reiniciar posiciones
        nuevo_estado = [
            1, 1,
            9, 11,
            estado[4],
            vidas
        ]

    else:
        nuevo_estado = estado

    return nuevo_estado

def main():
    # ==============================
    # CONFIGURACIÓN DEL JUEGO
    # ==============================

    tablero = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", ".", ".", "#", ".", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]

    # Estado de la partida:
    # [jugador_fila, jugador_columna,
    #  fantasma_fila, fantasma_columna,
    #  puntos, vidas]

    estado = [1, 1, 9, 11, 0, 3]



    
    # ==============================
    # PROGRAMA PRINCIPAL
    # ==============================

    

main()