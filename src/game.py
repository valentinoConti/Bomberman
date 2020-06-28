import pygame
import pygame.locals
import os
import random

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
ROJO = (0, 255, 0)
ALTO = 50
LARGO = 50
MARGEN = 3
TAM = 15
velocidad = 6  # Velocidad, en píxeles, por fotograma
velocidad2 = 6  # Velocidad, en píxeles, por fotograma
aleatorio = random.randrange(3)
poder = 0
poderX = -5
poderY = -5
conti = 0
conti2 = 0
conti3 = 0
poderActivo2 = 0
poderActivo = 0

tile = [[0 for x in range(TAM)] for y in range(TAM)]  #Arreglo de Tiles, aquí se cargará el mapa

f = open("assets/mapa.txt") #Cargo el archivo mapa desde mapa.txt
car = f.read() #Asigno la variable que lee el mapa
for fila in range(TAM):
    for columna in range(TAM):
            tile[fila][columna] = int(car[columna*TAM+fila])
f.close() # Cierro el archivo mapa


class Player(object):
    
    def __init__(self,xxx,yyy):
        self.rect = pygame.Rect(xxx, yyy, 42, 42)

    def mover(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.mover_un_solo_eje(dx, 0)
        if dy != 0:
            self.mover_un_solo_eje(0, dy)
    
    def mover_un_solo_eje(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for pared in paredes:
            if self.rect.colliderect(pared.rect):
                if dx > 0: # Moviendose a la derecha; choca contra el lado izquierdo de una pared
                    self.rect.right = pared.rect.left
                if dx < 0: # Moviendose a la izquierda; choca contra el lado derecho de una pared
                    self.rect.left = pared.rect.right
                if dy > 0: # Moviendose hacia abajo; choca contra la parte de arriba de una pared
                    self.rect.bottom = pared.rect.top
                if dy < 0: # Moviendose hacia arriba; choca contra la parte de abajo de una pared
                    self.rect.top = pared.rect.bottom
                    
                    
class Wall(object):
    
    def __init__(self, pos):
        paredes.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
            

def dibujar_paredes():
    global paredes
    paredes = []
    for fila in range(TAM):
        for columna in range(TAM):
            
            if tile[fila][columna] == 0:
                Wall([fila*(LARGO+MARGEN)+MARGEN,columna*(ALTO+MARGEN)+MARGEN])
                
            elif tile[fila][columna] == 2:
                Wall([fila*(LARGO+MARGEN)+MARGEN,columna*(ALTO+MARGEN)+MARGEN])
                
#            elif tile[fila][columna] == 3:
#                Wall()

def explosion(holis): #Mostrar la explosion de la bomba
    if holis==1:
        if tile[posiXX+1][posiYY] != 0: #Si no es una pared irrompible, se muestra la explosion
            pantalla.blit(boom, [(posiXX+1)*(LARGO+MARGEN)+MARGEN,posiYY*(ALTO+MARGEN)+MARGEN])
        if tile[posiXX-1][posiYY] != 0:
            pantalla.blit(boom, [(posiXX-1)*(LARGO+MARGEN)+MARGEN,posiYY*(ALTO+MARGEN)+MARGEN])
        if tile[posiXX][posiYY+1] != 0:
            pantalla.blit(boom, [posiXX*(LARGO+MARGEN)+MARGEN,(posiYY+1)*(ALTO+MARGEN)+MARGEN])
        if tile[posiXX][posiYY-1] != 0:
            pantalla.blit(boom, [posiXX*(LARGO+MARGEN)+MARGEN,(posiYY-1)*(ALTO+MARGEN)+MARGEN])
            
        pantalla.blit(boom, [(posiXX)*(LARGO+MARGEN)+MARGEN,posiYY*(ALTO+MARGEN)+MARGEN])
        
    elif holis==2:
        if tile[posiXXXX+1][posiYYYY] != 0: #Si no es una pared irrompible, se muestra la explosion
            pantalla.blit(boom, [(posiXXXX+1)*(LARGO+MARGEN)+MARGEN,posiYYYY*(ALTO+MARGEN)+MARGEN])
        if tile[posiXXXX-1][posiYYYY] != 0:
            pantalla.blit(boom, [(posiXXXX-1)*(LARGO+MARGEN)+MARGEN,posiYYYY*(ALTO+MARGEN)+MARGEN])
        if tile[posiXXXX][posiYYYY+1] != 0:
            pantalla.blit(boom, [posiXXXX*(LARGO+MARGEN)+MARGEN,(posiYYYY+1)*(ALTO+MARGEN)+MARGEN])
        if tile[posiXXXX][posiYYYY-1] != 0:
            pantalla.blit(boom, [posiXXXX*(LARGO+MARGEN)+MARGEN,(posiYYYY-1)*(ALTO+MARGEN)+MARGEN])
        
        pantalla.blit(boom, [(posiXXXX)*(LARGO+MARGEN)+MARGEN,posiYYYY*(ALTO+MARGEN)+MARGEN])
        
    
def cambiar_tiles(holis): #Al explotar una bomba, romper las paredes.-
    global poder, poderX, poderY, personaje, personaje2, vivo, vivo2, ganador
    if holis==1:
        if tile[posiXX+1][posiYY] == 2:
            tile[posiXX+1][posiYY] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXX+1
                poderY = posiYY
                poder = 1
            dibujar_paredes()
        if tile[posiXX-1][posiYY] == 2:
            tile[posiXX-1][posiYY] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXX-1
                poderY = posiYY
                poder = 1
            dibujar_paredes()
        if tile[posiXX][posiYY+1] == 2:
            tile[posiXX][posiYY+1] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXX
                poderY = posiYY+1
                poder = 1
            dibujar_paredes()
        if tile[posiXX][posiYY-1] == 2:
            tile[posiXX][posiYY-1] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXX
                poderY = posiYY-1
                poder = 1
            dibujar_paredes()
            
        #Si la explosion tocó al jugador:
        if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX+1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX-1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY+1) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY-1):
            personaje, vivo, ganador
            personaje = pygame.image.load("assets/personaje_muerto.gif").convert()
            ganador = "NEGRO"
            vivo = 0
            vivo2=0
            
        if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX+1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX-1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY+1) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY-1):
            personaje2, vivo2, ganador
            personaje2 = pygame.image.load("assets/personaje_muerto.gif").convert()
            ganador = "BLANCO"
            vivo2 = 0 
            vivo=0
            
            
    elif holis==2:
        if tile[posiXXXX+1][posiYYYY] == 2:
            tile[posiXXXX+1][posiYYYY] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXXXX+1
                poderY = posiYYYY
                poder = 1
            dibujar_paredes()
        if tile[posiXXXX-1][posiYYYY] == 2:
            tile[posiXXXX-1][posiYYYY] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXXXX-1
                poderY = posiYYYY
                poder = 1
            dibujar_paredes()
        if tile[posiXXXX][posiYYYY+1] == 2:
            tile[posiXXXX][posiYYYY+1] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXXXX
                poderY = posiYYYY+1
                poder = 1
            dibujar_paredes()
        if tile[posiXXXX][posiYYYY-1] == 2:
            tile[posiXXXX][posiYYYY-1] = 1
            alea = random.randrange(3)
            if alea == aleatorio:
                poderX = posiXXXX
                poderY = posiYYYY-1
                poder = 1
            dibujar_paredes()
            
        #Si la explosion tocó al jugador:
        
        if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX+1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX-1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY+1) or (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY-1):
            # global personaje2, vivo2, ganador
            personaje2 = pygame.image.load("assets/personaje_muerto.gif").convert()
            ganador = "BLANCO"
            vivo2 = 0
            vivo=0  
        
        if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX+1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX-1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY+1) or (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY-1):
            # global personaje, vivo
            personaje = pygame.image.load("assets/personaje_muerto.gif").convert()
            ganador = "NEGRO"
            vivo = 0
            vivo2= 0
    
        
    

        
def dibujar_tiles():
    
    for fila in range(TAM):
        for columna in range(TAM):
            
            if tile[fila][columna] == 0:
                COLOR = ladrillo2
                
            elif tile[fila][columna] == 1:
                COLOR = pasto
                
            elif tile[fila][columna] == 2:
                COLOR = ladrillo
#            elif tile[fila][columna] == 3:
#                COLOR = otraTextura
#            elif tile[fila][columna] == 4:
#                COLOR = CELESTE
            if ((igual == 1) or (posiX*(LARGO+MARGEN)+MARGEN) == (fila*(LARGO+MARGEN)+MARGEN)) and ((posiY*(LARGO+MARGEN)+MARGEN) == (columna*(ALTO+MARGEN)+MARGEN)):
                pantalla.blit(COLOR, [fila*(LARGO+MARGEN)+MARGEN,columna*(ALTO+MARGEN)+MARGEN])
                pantalla.blit(bomba, [posiX*(LARGO+MARGEN)+MARGEN,posiY*(ALTO+MARGEN)+MARGEN])
            if ((igual2 == 1) or (posiXXX*(LARGO+MARGEN)+MARGEN) == (fila*(LARGO+MARGEN)+MARGEN)) and ((posiYYY*(LARGO+MARGEN)+MARGEN) == (columna*(ALTO+MARGEN)+MARGEN)):
                pantalla.blit(bomba, [posiXXX*(LARGO+MARGEN)+MARGEN,posiYYY*(ALTO+MARGEN)+MARGEN])                
                pantalla.blit(COLOR, [fila*(LARGO+MARGEN)+MARGEN,columna*(ALTO+MARGEN)+MARGEN])

            else:
                pantalla.blit(COLOR, [fila*(LARGO+MARGEN)+MARGEN,columna*(ALTO+MARGEN)+MARGEN])
            


os.environ["SDL_VIDEO_CENTERED"] = "1"  
pygame.init()

# pygame.mouse.set_visible(0) #Oculta el MOuse
 
dimensiones = [798,798]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Bomberman")

hecho = False
ladrillo2 = pygame.image.load("assets/ladrillo2.gif").convert()
ladrillo = pygame.image.load("assets/ladrillo.gif").convert()
pasto = pygame.image.load("assets/pasto.gif").convert()
personaje = pygame.image.load("assets/personaje.gif").convert()
personaje2 = pygame.image.load("assets/personaje2.gif").convert()
speed = pygame.image.load("assets/speed.gif").convert()
fuente = pygame.font.Font(None, 30)
vivo = 1
vivo2 = 1
igual = 0
igual2 = 0
ganador = ""
texto_de_salida2 = "Presione ESCAPE para Salir del juego"
texto2 = fuente.render(texto_de_salida2, True, ROJO)

#BOMBA
bomba = pygame.image.load("assets/bomba.png").convert()
boom = pygame.image.load("assets/boom.png").convert()
boom.set_colorkey(BLANCO)
bomba.set_colorkey(BLANCO)
puedoPoner = 1
puedoPoner2 = 1
cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
posiX = -50
posiXXX = -50
posiYYY = -50
posiY = -50

BOMBA=bomba.get_rect()
exp = 0
exp2 = 0
band=False
band2=False
#finBOMBA

reloj = pygame.time.Clock()  # Se usa para establecer cuan rápido se actualiza la pantalla
paredes = [] # Arreglo que contiene a las paredes
jugador = Player(60,64) # Creamos al jugador
enemigo = Player(695,695) # Creamos al jugador 2

dibujar_paredes()

# Bucle principal
while not hecho:
    # Bucle de eventos
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            hecho = True
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_KP5:
            if vivo==1:
                if puedoPoner == 1:
                    puedoPoner = 0
                    posiX = (jugador.rect.x+20) // (LARGO + MARGEN)
                    posiY = (jugador.rect.y+20) // (ALTO + MARGEN)
                    igual = 1
                    posiXX = (jugador.rect.x+20) // (LARGO + MARGEN)
                    posiYY = (jugador.rect.y+20) // (ALTO + MARGEN)
                    
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            if vivo2==1:
                if puedoPoner2 == 1:
                    puedoPoner2 = 0
                    posiXXX = (enemigo.rect.x+20) // (LARGO + MARGEN)
                    posiYYY = (enemigo.rect.y+20) // (ALTO + MARGEN)
                    igual2 = 1
                    posiXXXX = (enemigo.rect.x+20) // (LARGO + MARGEN)
                    posiYYYY = (enemigo.rect.y+20) // (ALTO + MARGEN)
        
                

    
    key = pygame.key.get_pressed()
    if vivo==1:
        if key[pygame.K_LEFT]:
            jugador.mover(-velocidad, 0)
        if key[pygame.K_RIGHT]:
            jugador.mover(velocidad, 0)
        if key[pygame.K_UP]:
            jugador.mover(0, -velocidad)
        if key[pygame.K_DOWN]:
            jugador.mover(0, velocidad)
        if puedoPoner == 0:
            if(cont >= 120):
                band=False
                cont = 0
                posiX = -50
                posiY = -50
                exp = 1
                
            else:
                cont+=1
                band=True


    if vivo2==1:    
        if key[pygame.K_a]:
            enemigo.mover(-velocidad2, 0)
        if key[pygame.K_d]:
            enemigo.mover(velocidad2, 0)
        if key[pygame.K_w]:
            enemigo.mover(0, -velocidad2)
        if key[pygame.K_s]:
            enemigo.mover(0, velocidad2)
        if puedoPoner2 == 0:
            if(cont3 >= 120):
                band2=False
                cont3 = 0
                posiXXX = -50
                posiYYY = -50
                exp2 = 1
            else:
                cont3+=1
                band2=True

    if band:
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX+1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY):
	    	if key[pygame.K_LEFT]:
	    		jugador.rect.left = (posiXX+1)*(LARGO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX-1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY):
	    	if key[pygame.K_RIGHT]:
	    		jugador.rect.right = (posiXX)*(LARGO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY+1):
	    	if key[pygame.K_UP]:
	    		jugador.rect.top = (posiYY+1)*(ALTO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYY-1):
	    	if key[pygame.K_DOWN]:
	    		jugador.rect.bottom = (posiYY)*(ALTO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX+1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY):
	    	if key[pygame.K_a]:
	    		enemigo.rect.left = (posiXX+1)*(LARGO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX-1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY):
	    	if key[pygame.K_d]:
	    		enemigo.rect.right = (posiXX)*(LARGO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY+1):
	    	if key[pygame.K_w]:
	    		enemigo.rect.top = (posiYY+1)*(ALTO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYY-1):
	    	if key[pygame.K_s]:
	    		enemigo.rect.bottom = (posiYY)*(ALTO+MARGEN)

    if band2:
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX+1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY):
	    	if key[pygame.K_LEFT]:
	    		jugador.rect.left = (posiXXXX+1)*(LARGO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX-1 and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY):
	    	if key[pygame.K_RIGHT]:
	    		jugador.rect.right = (posiXXXX)*(LARGO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY+1):
	    	if key[pygame.K_UP]:
	    		jugador.rect.top = (posiYYYY+1)*(ALTO+MARGEN)
	    if (((jugador.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == posiYYYY-1):
	    	if key[pygame.K_DOWN]:
	    		jugador.rect.bottom = (posiYYYY)*(ALTO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX+1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY):
	    	if key[pygame.K_a]:
	    		enemigo.rect.left = (posiXXXX+1)*(LARGO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX-1 and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY):
	    	if key[pygame.K_d]:
	    		enemigo.rect.right = (posiXXXX)*(LARGO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY+1):
	    	if key[pygame.K_w]:
	    		enemigo.rect.top = (posiYYYY+1)*(ALTO+MARGEN)
	    if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == posiXXXX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == posiYYYY-1):
	    	if key[pygame.K_s]:
	    		enemigo.rect.bottom = (posiYYYY)*(ALTO+MARGEN)


    texto_de_salida = "Gana el Jugador {}! Presione ESPACIO para Reiniciar".format(ganador)
    texto = fuente.render(texto_de_salida, True, ROJO)
    
    
        
    # Dibujos
    pantalla.fill(NEGRO)
    dibujar_tiles()
    pantalla.blit(personaje, jugador.rect)
    pantalla.blit(personaje2, enemigo.rect)
    
    if poder==1:
        if(conti >= 120):
            poder=0
            conti=0
        else:
            conti+=1
            pantalla.blit(speed, (poderX * (LARGO + MARGEN) + 10, poderY * (ALTO + MARGEN) + 10))
            if (((jugador.rect.x+20) // (LARGO + MARGEN)) == poderX and ((jugador.rect.y+20) // (ALTO + MARGEN)) == poderY):
                poderActivo = 1
                poder = 0
            if (((enemigo.rect.x+20) // (LARGO + MARGEN)) == poderX and ((enemigo.rect.y+20) // (ALTO + MARGEN)) == poderY):
                poderActivo2 = 1
                poder = 0
    
    if poderActivo==1:
        if(conti2 >= 180):
            poderActivo=0
            conti2=0
            velocidad = 6
        else:
            conti2+=1
            velocidad = 8
            
    if poderActivo2==1:
        if(conti3 >= 180):
            poderActivo2=0
            conti3=0
            velocidad2 = 6
        else:
            conti3+=1
            velocidad2 = 8
            
  
    if vivo2==0:							#reiniciar el juego
        pantalla.blit(texto,(100 ,22))
        pantalla.blit(texto2,(200,758))
        if key[pygame.K_SPACE]:
        	pygame.quit()
        	os.system("python3 game.py && exit")
         

  
    if exp==1: #Explotó la bomba
        if(cont2 >= 20): #Desaparece fuego
            cont2 = 0
            exp = 0
            puedoPoner = 1
            posiXX = -50
            posiYY = -50
        else: #Empieza fuego, cambian tiles por la explosion
            explosion(1)
            if cont2 == 1:
                cambiar_tiles(1)
            cont2+=1
    
    if exp2==1: #Explotó la bomba
        if(cont4 >= 20): #Desaparece fuego
            cont4 = 0
            exp2 = 0
            puedoPoner2 = 1
            posiXXXX = -50
            posiYYYY = -50
        else: #Empieza fuego, cambian tiles por la explosion
            explosion(2)
            if cont4 == 1:
                cambiar_tiles(2)
            cont4+=1
     

    pygame.display.flip() # Avanza el fotograma
 
    reloj.tick(60) # Limitamos a 60 fps
     
pygame.quit() # Cerramos la ventana y salimos.