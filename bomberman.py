import pygame
import pygame.locals
import os

NEGRO = (0, 0 ,0)
BLANCO = (121, 121, 121)
hecho = False

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# pygame.mouse.set_visible(0) #Oculta el MOuse
 
dimensiones = [798,798]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Bomberman")

reloj = pygame.time.Clock()  # Se usa para establecer cuan rápido se actualiza la pantalla
fondo = pygame.image.load("assets/fondo.png").convert()
papita = pygame.image.load("assets/papita.png").convert()
papita.set_colorkey(BLANCO)
papita2 = pygame.image.load("assets/papita2.png").convert()
papita2.set_colorkey(BLANCO)
fondo2 = pygame.image.load("assets/fondo2.png").convert()
fondo3 = pygame.image.load("assets/fondo3.png").convert()
mov = 900
mov2 = -250
cont = 1
lado = 2
cont2 = 1
cond = 0

# Bucle principal
while not hecho:
    # Bucle de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            hecho = True
        
    # Dibujos
    pantalla.fill(NEGRO)
    pantalla.blit(fondo, [0, 0])
    if lado==2:
        if cont==1:
            mov-=2
        elif cont==2:
            mov+=4
            if mov >=900:
                lado=1
        pantalla.blit(papita, [mov, 200])
        if mov<=625:
            cont=2
            
    elif lado==1:
        
        if cont2==1:
            mov2+=2
            if mov2>=-80:
                cont2=2
        elif cont2==2:
            mov2-=4
            if mov2 <= -250:
                lado=3
        pantalla.blit(papita2, [mov2, 200])
        
    elif lado==3:
        
        pantalla.fill(NEGRO)
        pantalla.blit(fondo2,[0, 0])
        key = pygame.key.get_pressed()    
        if key[pygame.K_i]:
            cond = 1
            
            
        elif key[pygame.K_SPACE]:
            lado = 4
    
    elif lado ==4:
        import game.py
        
    if(cond == 1):
        pantalla.fill(NEGRO)
        pantalla.blit(fondo3, [0,0])

        
    pygame.display.flip() # Avanza el fotograma
 
    reloj.tick(60) # Limitamos a 60 fps
     
pygame.quit() # Cerramos la ventana y salimos.