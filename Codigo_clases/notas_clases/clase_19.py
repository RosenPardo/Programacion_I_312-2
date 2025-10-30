import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

while True:
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill((24, 55, 72))

    pygame.display.update()


#GDB de Manu: https://onlinegdb.com/w410xODAi
