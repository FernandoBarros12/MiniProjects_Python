from cgitb import text
from cmath import sqrt
import pygame
from pygame import mixer
import random
import math

# Inicializar pygame
pygame.init()

# Crear pantalla de juego
pantalla = pygame.display.set_mode((800,600))

# Titulo e icono
pygame.display.set_caption('Invasion Espacial')
icono=pygame.image.load('./recursos/ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('./recursos/Fondo.jpg')

# Agregar musica
mixer.music.load('./recursos/MusicaFondo.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Variables de jugador
img_jugador= pygame.image.load('./recursos/nave.png')
jugador_x, jugador_y = 368, 500 # resta el tamano de la imagen
jugador_x_cambio=0


# Variables de enemigo
img_enemigo= pygame.image.load('./recursos/enemigo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(0, 200)
enemigo_x_cambio=0.1
enemigo_y_cambio = 50

# Creacion varios enemigos
img_enemigo= []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio=[]
enemigo_y_cambio = []
cantidad_enemigos = 6

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('./recursos/enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)



# Variables de bala
img_bala= pygame.image.load('./recursos/bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio=0 # Esta variable quedara en 0
bala_y_cambio = 0.4
bala_visible = False


# Variables de Puntaje
puntaje=0
fuente = pygame.font.Font('./recursos/PressStart2P-Regular.ttf', 20)
texto_x, texto_y = 10, 10

# Texto de Juego Terminado
fuente_final = pygame.font.Font('./recursos/PressStart2P-Regular.ttf', 20)

# Funcion texto final
def texto_final():
    fuente_f = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(fuente_f, (320, 250))

# Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Score: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x, y)) 


# Funcion enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x, y)) 


# Funcion disparar
def disparar(x,y):
    global bala_visible
    bala_visible=True
    pantalla.blit(img_bala, (x + 16, y + 10)) 

# Funcion para detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia <27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta=True
while se_ejecuta:

    # Cargar fondo
    pantalla.blit(fondo, (0, 0))

    # ITERAR EVENTOS
    for evento in pygame.event.get():

        # Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta=False
        
        # Evento presionar teclas
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
            if evento.key == pygame.K_SPACE:
                sonido_disparo=mixer.Sound('./recursos/disparo.mp3')
                sonido_disparo.play()
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar(bala_x, bala_y)

        # Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    

    # Modificar ubicacion JUGADOR
    jugador_x += jugador_x_cambio

    # Mantener en bordes a JUGADOR
    if jugador_x <= 0:
        jugador_x=0
    elif jugador_x>=736:
        jugador_x=736


    # Modificar ubicacion ENEMIGO
    for e in range(cantidad_enemigos):

        # FIN DEL JUEGO
        if enemigo_y[e] > 490 or hay_colision(jugador_x, jugador_y, enemigo_x[e], enemigo_y[e]) == True:
            for k in range (cantidad_enemigos):
                enemigo_y[k]=1000 # Sacar enemigos de pantalla
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]



    # Mantener en bordes a ENEMIGO
    for e in range(cantidad_enemigos):
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Analizar colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('./recursos/golpe.mp3')
            sonido_colision.play()
            bala_y=525
            bala_visible=False
            puntaje +=1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(0, 200)


        enemigo(enemigo_x[e], enemigo_y[e], e)


    #MOVIMIENTO BALA
    if bala_visible:
        disparar(bala_x, bala_y)
        bala_y-= bala_y_cambio
   
    #Tener mas de 1 bala
    if bala_y <= -64: # bala tiene 64 px de alto
        bala_y=525
        bala_visible=False
    


    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # ACTUALIZAR
    pygame.display.update()

    


