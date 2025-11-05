import pygame as pg

pg.init()
x = 800
y = 600

ALTO_VENTANA = y
ANCHO_VENTANA = x

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
"""
imagen_vertical = pg.Surface((x, y))
imagen_vertical.fill((255,0,0))
rectangulo = imagen_vertical.get_rect()

rectangulo.x = (ANCHO_VENTANA - rectangulo.width) // 2
rectangulo.y = (ALTO_VENTANA - rectangulo.height) // 2
"""


#fondo = pg.image.load("D:/UTN/Programacion_I_312/Pygame/img/bill.png")
#fondo = pg.transform.scale(fondo, (ANCHO_VENTANA - 300, ALTO_VENTANA - 100))

# Blitear el fondo

"""
imagen = pg.image.load("ss.png")
imagen2 = imagen.get_rect()

imagen2.x = 30
imagen2.y = 30

escenario = pg.image.load("tablerosudoku.png")
escenario1 = pg.transform.scale(escenario, (ANCHO_VENTANA,ALTO_VENTANA))
escenario2 = escenario1.get_rect()

escenario2.x = 0
escenario2.y = 0
"""
#megaman = imagen.get_rect()


#screen.fill("grey")
"""
cuadrado = pg.Surface((50, 50))
cuadrado.fill("red")
figura = cuadrado.get_rect()
figura.x = 50

figura.y = 0
"""



simbolo_x = pg.image.load("D:/UTN/Programacion_I_312/Pygame/img/icono.png")
sinbolo_x = pg.transform.scale(simbolo_x, (10, 10))


def dibujar_imagen(imagen,posicion):
    screen.blit(imagen,posicion)

#screen.blit(fondo, (0, 100))

while True:

    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = evento.pos 
            coordenada = evento.pos
            #screen.blit(simbolo_x, evento.pos)
            print(evento.pos)
            screen.blit(simbolo_x, (11, 111))
            #if mouseX >=  and x
            
    
    pg.display.update()
    pg.display.flip()
    


    """
    #CORREGIR ESCALA
    correccion_tamaño = pg.transform.scale(imagen_cargada, (numero,numero))
    
    """