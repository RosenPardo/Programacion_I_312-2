from funciones.configuracion import *


iniciar_juego()

color_blanco = (255, 255, 255)

while True:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.flip()
    

