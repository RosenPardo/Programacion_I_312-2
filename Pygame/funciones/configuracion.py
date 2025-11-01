import pygame as pg


def iniciar_juego():
    pg.init()
    tamaño_pantalla = (750, 750)
    pantalla = pg.display.set_mode(tamaño_pantalla)

    pg.display.set_caption("SUDOKU UTN FRA")

    icono = pg.image.load("D:/UTN/Programacion_I_312/Pygame/img/icono.png")
    pg.display.set_icon(icono)

    return pantalla