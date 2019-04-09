import pygame, random, sys
from pygame.locals import *
ANCHOVENTANA = 900
ALTOVENTANA = 900
COLORVENTANA = (255, 255, 255)
COLORTEXTO = (130, 130,130)
COLORFONDO = (0, 255, 255)
FPS = 40
TAMAÑOMINMISIL = 10
TAMAÑOMAXMISIL = 40
TAMAÑOMINNUBE = 50
TAMAÑOMAXNUBE = 90
VELOCIDADMINMISIL = 1
VELOCIDADMAXMISIL = 8
VELOCIDADMINNUBE = 1
VELOCIDADMAXNUBE = 3
TASANUEVOMISIL = 6
TASANUEVONUBE=12
TASAMOVIMIENTOJUGADOR = 5
def terminar():
  pygame.quit()
  sys.exit()
def esperarTeclaJugador():
  while True:
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == K_ESCAPE: # Quita al presionar ESCAPE
          terminar()
        return
def jugadorGolpeaMisil(rectanguloJugador, misiles):
  for v in misiles:
    if rectanguloJugador.colliderect(v['rect']):
      return True
  return False
def dibujarTexto(texto, font, superficie, x, y):
  objetotexto = font.render(texto, 1, COLORTEXTO)
  rectangulotexto = objetotexto.get_rect()
  rectangulotexto.topleft = (x, y)
  superficie.blit(objetotexto, rectangulotexto)
# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption('AprenderPython - InvaSion')
pygame.mouse.set_visible(False)
# establece los fonts
font = pygame.font.SysFont(None, 48)
# establece los sonidos
gameOverSound = pygame.mixer.Sound('juegoterminado.wav')
pygame.mixer.music.load('musicajuego.mp3')
# establece las imagenes
playerImage = pygame.image.load('war_cursovideojuegos-python_opt.png')
rectanguloJugador = playerImage.get_rect()
baddieImage = pygame.image.load('misil_cursovideojuegos-python_opt2.png')
nubeImage = pygame.image.load('nube-war_cursovideojuegos-python.png')
# Muestra la pantalla inicial
dibujarTexto('AprenderPython - InvaSion', font, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3))
dibujarTexto('Presione una tecla para comenzar el juego', font, superficieVentana, (ANCHOVENTANA / 3) - 180, (ALTOVENTANA / 3) + 50)
pygame.display.update()
esperarTeclaJugador()
puntajeMax = 0
while True:
  # establece el comienzo del juego
  misiles = []
  nubes = [] 
  puntaje = 0
  rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
  moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
  trucoReversa = trucoLento = False
  contadorAgregarMisil = 0
  contadorAgregarNube = 0
  pygame.mixer.music.play(-1, 0.0)
  while True: # el ciclo del juego se mantiene mientras se este jugando
    puntaje += 1 # incrementa el puntaje
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == ord('z'):
          trucoReversa = True
        if evento.key == ord('x'):
          trucoLento = True
        if evento.key == K_LEFT or evento.key == ord('a'):
          moverDerecha = False
          moverIzquierda = True
        if evento.key == K_RIGHT or evento.key == ord('d'):
          moverIzquierda = False
          moverDerecha = True
        if evento.key == K_UP or evento.key == ord('w'):
          moverAbajo = False
          moverArriba = True
        if evento.key == K_DOWN or evento.key == ord('s'):
          moverArriba = False
          moverAbajo = True
      if evento.type == KEYUP:
       if evento.key == ord('z'):
          trucoReversa = False
          puntaje = 0
       if evento.key == ord('x'):
          trucoLento = False
          puntaje = 0
       if evento.key == K_ESCAPE:
          terminar()
       if evento.key == K_LEFT or evento.key == ord('a'):
         moverIzquierda = False
       if evento.key == K_RIGHT or evento.key == ord('d'):
         moverDerecha = False
       if evento.key == K_UP or evento.key == ord('w'):
         moverArriba = False
       if evento.key == K_DOWN or evento.key == ord('s'):
         moverAbajo = False
      if evento.type == MOUSEMOTION:
       # Si se mueve el ratón, este se mueve adonde el cursor esté.
        rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)
    # Añade misiles en la parte superior de la pantalla, de ser necesarios.
    if not trucoReversa and not trucoLento:
      contadorAgregarMisil += 1
    if contadorAgregarMisil == TASANUEVOMISIL:
      contadorAgregarMisil = 0
      baddieSize = random.randint(TAMAÑOMINMISIL, TAMAÑOMAXMISIL)
      newBaddie = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
      'speed': random.randint(VELOCIDADMINMISIL, VELOCIDADMAXMISIL),
      'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
      }
      misiles.append(newBaddie)
    # Añade nubes en la parte superior de la pantalla 
    if not trucoReversa and not trucoLento:
      contadorAgregarNube += 1 
    if contadorAgregarNube == TASANUEVONUBE:
      contadorAgregarNube = 0
      baddieSize1 = random.randint(TAMAÑOMINNUBE, TAMAÑOMAXNUBE)
      newBaddie1 = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize1), 0 - baddieSize1, baddieSize1, baddieSize1),
      'speed': random.randint(VELOCIDADMINNUBE, VELOCIDADMAXNUBE),
      'surface':pygame.transform.scale(nubeImage, (baddieSize1, baddieSize1)),
      }
      nubes.append(newBaddie1)
    # Mueve el jugador.
    if moverIzquierda and rectanguloJugador.left  > 0:
      rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
    if moverDerecha and rectanguloJugador.right < ANCHOVENTANA:
      rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
    if moverArriba and rectanguloJugador.top  > 0:
      rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
    if moverAbajo and rectanguloJugador.bottom < ALTOVENTANA:
      rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)
    # Mueve el cursor del ratón hacia el jugador.
    pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)
    # Mueve los misiles hacia abajo.
    for b in misiles:
      if not trucoReversa and not trucoLento:
        b['rect'].move_ip(0, b['speed'])
      elif trucoReversa:
        b['rect'].move_ip(0, -5)
      elif trucoLento:
        b['rect'].move_ip(0, 1)
    # Mueve las nubes hacia abajo.
    for b in nubes:
        b['rect'].move_ip(0, b['speed']) 
    # Elimina los misiles que han caido por debajo.
    for b in misiles[:]:
      if b['rect'].top > ALTOVENTANA:
        misiles.remove(b)
    # Elimina las nubes que han caido por debajo.
    for b in nubes[:]:
       if b['rect'].top > ALTOVENTANA:
          nubes.remove(b) 
    # Dibuja el mundo del juego en la ventana.
    superficieVentana.fill(COLORFONDO)
    # Dibuja el puntaje y el puntaje máximo
    dibujarTexto('Puntos: %s' % (puntaje), font, superficieVentana, 10, 0)
    dibujarTexto('Records: %s' % (puntajeMax), font, superficieVentana, 10, 40)
    # Dibuja el rectángulo del jugador
    superficieVentana.blit(playerImage, rectanguloJugador)
    # Dibuja cada misil
    for b in misiles:
      superficieVentana.blit(b['surface'], b['rect'])
    # Dibuja cada nube
    for b in nubes:
      superficieVentana.blit(b['surface'], b['rect']) 
    pygame.display.update()
    # Verifica si algún misil impactó en el jugador.
    if jugadorGolpeaMisil(rectanguloJugador, misiles):
      if puntaje > puntajeMax:
        puntajeMax = puntaje # Establece nuevo puntaje máximo
      break
    relojPrincipal.tick(FPS)
  # Frena el juego y muestra "Juego Terminado"
  pygame.mixer.music.stop()
  gameOverSound.play()
  dibujarTexto('Juego Terminado', font, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
  dibujarTexto('Presione una tecla para repetir.', font, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
  pygame.display.update()
  esperarTeclaJugador()
  gameOverSound.stop()