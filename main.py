# Proyecto: Cuatro en línea.

import pygame
import time
import re


def crear_tablero(filas, columnas):
    tablero = []
    i = 0
    while i < filas:
        fila = []
        j = 0
        while j < columnas:
            fila = fila + ["."]
            j += 1
        tablero = tablero + [fila]
        i += 1
    return tablero


def mostrar_tablero(tablero):
    j = 0
    encabezado = ""
    while j < len(tablero[0]):
        encabezado = encabezado + str(j) + " "
        j += 1
    print(encabezado)

    i = 0
    while i < len(tablero):
        j = 0
        fila = ""
        while j < len(tablero[i]):
            fila = fila + tablero[i][j] + " "
            j += 1
        print(fila)
        i += 1


def introducir_ficha(tablero, columna, color):
    if color == "Amarilla":
        for fila in reversed(tablero):
            if fila[columna] == '.':
                fila[columna] = 'X'
                return tablero
    elif color == "Roja":
        for fila in reversed(tablero):
            if fila[columna] == '.':
                fila[columna] = 'O'
                return tablero
    else:
        print("Solo hay fichas rojas y amarillas.")
        print("Escriba 'Amarilla' o 'Roja'.")

    print("Columna llena.")
    return tablero


def revisar_filas(tablero, color):
    for fila in tablero:
        contador = 0
        for celda in fila:
            if celda == color:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0
    return False


def revisar_columnas(tablero, color):
    columnas = len(tablero[0])
    filas = len(tablero)
    for col in range(columnas):
        contador = 0
        for fila in range(filas):
            if tablero[fila][col] == color:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0
    return False


def revisar_diagonal_derecha(tablero, color):
    fil = 0
    while fil <= len(tablero) - 4:
        col = 0
        while col <= len(tablero[0]) - 4:
            if tablero[fil][col] == color:
                if tablero[fil + 1][col + 1] == color:
                    if tablero[fil + 2][col + 2] == color:
                        if tablero[fil + 3][col + 3] == color:
                            return True
            col += 1
        fil += 1
    return False


def revisar_diagonal_izquierda(tablero, color):
    fil = 0
    while fil <= len(tablero) - 4:
        col = len(tablero[0]) - 1
        while col >= len(tablero) - 4:
            if tablero[fil][col] == color:
                if tablero[fil + 1][col - 1] == color:
                    if tablero[fil + 2][col - 2] == color:
                        if tablero[fil + 3][col - 3] == color:
                            return True
            col -= 1
        fil += 1
    return False


def comprobar_ganador(tablero, color):
    cuatro_fila = revisar_filas(tablero, color)
    cuatro_columna = revisar_columnas(tablero, color)
    cuatro_diag_der = revisar_diagonal_derecha(tablero, color)
    cuatro_diag_izq = revisar_diagonal_izquierda(tablero, color)
    if cuatro_fila | cuatro_columna | cuatro_diag_der | cuatro_diag_izq:
        return True
    return False


def columna_llena(tablero, columna):
    return tablero[0][columna] != '.'


def tablero_lleno(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == '.':
                return False
    return True


print("--- Bienvenido a Cuatro en Línea REBORN ---")
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
print("Jugador 1: Fichas Amarillas (X).")
print("Jugador 2: Fichas Rojas (O).")

print("\n")
tab = crear_tablero(6, 7)
mostrar_tablero(tab)
print("\n")

jugador = 1
turno = 1

# X = Amarilla, O = Roja

while True:
    print(f"Turno {turno}")
    col = input(f"Jugador {jugador}, elige tu columna: ")

    if not re.fullmatch(r'\d+', col):
        print("Sólo puedes ingresar números.")
        continue

    col = int(col)

    if col < 0 or col >= len(tab[0]):
        print("Columna inválida. Intenta de nuevo.")
        continue

    if columna_llena(tab, col):
        print("La columna está llena. Intenta con otra.")
        continue

    if jugador == 1:
        introducir_ficha(tab, col, "Amarilla")
        mostrar_tablero(tab)
        jugador = 2
    elif jugador == 2:
        introducir_ficha(tab, col, "Roja")
        mostrar_tablero(tab)
        jugador = 1
    if turno >= 7:
        if comprobar_ganador(tab, "X"):
            print("¡Gana Jugador 1!")
            break
        elif comprobar_ganador(tab, "O"):
            print("¡Gana Jugador 2!")
            break
    turno += 1
    if tablero_lleno(tab):
        print("¡Empate!")
        break

pygame.mixer.music.stop()
pygame.mixer.music.load("victory.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
time.sleep(5)
