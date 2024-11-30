#-------------------tetrUs-----------------------
import sys
import time
import random
import pygame
import functies
from pygame.locals import QUIT
from pygame.surface import SurfaceType
import win32gui, win32con

pygame.init()

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

#-------------------Variabelen-------------------
#Scherm
SCREEN_COLOUR = (155,155,155)
SCREEN_NAME = "Tetris"
pixelSize = 30

#Boundary
relative = 10 * pixelSize
LINE_COLOUR = (255,0,0)
LINE_LEFT_X = 0 * pixelSize + (relative / 2)
LINE_RIGHT_X  = 10 * pixelSize + (relative / 2)
LINE_BOTTOM_Y = 18 * pixelSize
LINE_TOP_Y = 3 * pixelSize

#Colour
xycolour = []

#Score
score = 0
score_increment = 10

#Pieces
pieces = ["I", "J", "L", "O", "S", "T", "Z"]
piece = random.choice(pieces)
piece1 = random.choice(pieces)
piece2 = random.choice(pieces)
piece3 = random.choice(pieces)
hold = 0

#Coordinaten
coordsx = []
coordsy = []
pixelx =functies.decodex(piece, pixelSize, relative)
pixely = functies.decodey(piece, pixelSize)


#Overig variabele
rotations = 0
x = 1
OutOfBoundsLeft = False
OutOfBoundsRight = False
HoldAble = True
counter = 0
#-----------------------------------------------

#-------------------Setup----------------------a
#Scherm setup
screen = pygame.display.set_mode((11 * pixelSize + relative, 20 * pixelSize + relative))
surface = pygame.Surface((11 * pixelSize + relative, 20 * pixelSize + relative))
pygame.display.set_caption(SCREEN_NAME)
#Timer setup
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
#------------------Gameloop-----------------------
run = True
while run:
  for i in range(0, len(coordsy)):
    if coordsy[i] < 3*pixelSize:
      run = False
  
  #Eventhandler
  for event in pygame.event.get():
    if event.type == QUIT:
      run = False
  
  #Refresh van scherm
  screen.blit(surface, (0, 0))

  #Colour picker
  PLAYER_COLOUR = functies.colourpicker(piece)
  PLAYER1_COLOUR = functies.colourpicker(piece1)
  PLAYER2_COLOUR = functies.colourpicker(piece2)
  PLAYER3_COLOUR = functies.colourpicker(piece3)
  if hold != 0:
    HOLD_COLOUR = functies.colourpicker(hold)

  pixelx1 = functies.decodex(piece1, pixelSize, relative)
  pixely1 = functies.decodey(piece1, pixelSize)
  pixelx2 = functies.decodex(piece2, pixelSize, relative)
  pixely2 = functies.decodey(piece2, pixelSize)
  pixelx3 = functies.decodex(piece3, pixelSize, relative)
  pixely3 = functies.decodey(piece3, pixelSize)
  if hold != 0:
    pixelxHOLD = functies.decodex(hold, pixelSize, relative)
    pixelyHOLD = functies.decodey(hold, pixelSize)

  #Draw player
  for i in range(len(pixelx)):
    player = pygame.Rect((pixelx[i], pixely[i], 1*pixelSize, 1*pixelSize))
    pygame.draw.rect(screen, (PLAYER_COLOUR), player)
  
  #Draw next
  for i in range(len(pixelx1)):
    piece1Draw = pygame.Rect((pixelx1[i] + (8 * pixelSize), pixely1[i] + (1 * pixelSize), 1*pixelSize, 1*pixelSize))
    pygame.draw.rect(screen, (PLAYER1_COLOUR), piece1Draw)

  for i in range(len(pixelx2)):
    piece2Draw = pygame.Rect((pixelx2[i] + (8 * pixelSize), pixely2[i] + (6 * pixelSize), 1*pixelSize, 1*pixelSize))
    pygame.draw.rect(screen, (PLAYER2_COLOUR), piece2Draw)

  for i in range(len(pixelx3)):
    piece3Draw = pygame.Rect((pixelx3[i] + (8 * pixelSize), pixely3[i] + (11 * pixelSize), 1*pixelSize, 1*pixelSize))
    pygame.draw.rect(screen, (PLAYER3_COLOUR), piece3Draw)
  
  #Draw Hold
  if hold != 0:
    for i in range(len(pixelxHOLD)):
      pieceHoldDraw = pygame.Rect((pixelxHOLD[i] - relative + 2 * pixelSize, pixelyHOLD[i] + (11 * pixelSize), 1*pixelSize, 1*pixelSize))
      pygame.draw.rect(screen, (HOLD_COLOUR), pieceHoldDraw)

  #Boundary
  pygame.draw.line(screen, (LINE_COLOUR), (LINE_LEFT_X, 0), (LINE_LEFT_X, LINE_BOTTOM_Y), 10)
  pygame.draw.line(screen, (LINE_COLOUR), (LINE_RIGHT_X, 0), (LINE_RIGHT_X, LINE_BOTTOM_Y), 10)
  Bottom_Line = pygame.draw.line(screen, (LINE_COLOUR), (LINE_LEFT_X, LINE_BOTTOM_Y), (LINE_RIGHT_X, LINE_BOTTOM_Y), 10)
  Top_Line = pygame.draw.line(screen, (LINE_COLOUR), (LINE_LEFT_X, LINE_TOP_Y), (LINE_RIGHT_X, LINE_TOP_Y), 3)
 
  #Vallende spelen
  
  for j in range(len(pixely)):
    if pixely[j] < (LINE_BOTTOM_Y):
      elapsed_time = pygame.time.get_ticks() - start_time
      if elapsed_time > 250 + ((((100*(score+200))**-0.1)*5000)-1000):
        for i in range(0,len(pixelx)):
          pixely[i] += 1*pixelSize
        elapsed_time = 0
        start_time = pygame.time.get_ticks()

  #----------------------------------------------------------------------Player movement-----------------------------------------------------------------
  Rechts = True
  def goRight():
    for i in range(0,len(pixelx)):
      pixelx[i] += 1*pixelSize
  Links = True
  def goLeft():
    for i in range(0,len(pixelx)):
      pixelx[i] -= 1*pixelSize
  def GoDown():
    for i in range(0,len(pixelx)):
          pixely[i] += 1*pixelSize
  DropDown = True
  #Input checken
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      #Move left
      if event.key == pygame.K_a:
        for k in range(len(pixelx)):
          if pixelx[k] == (LINE_LEFT_X):
            Links = False
        for i in range(len(coordsx)):
          for j in range(len(pixelx)):
            if (coordsy[i]) ==  pixely[j] and pixelx[j] == (coordsx[i] + 1*pixelSize): 
              Links = False
        if Links == True:
          goLeft()
      #Move right
      elif event.key == pygame.K_d:
        for k in range(len(pixelx)):
          if pixelx[k] == (LINE_RIGHT_X - 1*pixelSize):
            Rechts = False
        for i in range(len(coordsx)):
          for j in range(len(pixelx)):
            if (coordsy[i]) ==  pixely[j] and pixelx[j] == (coordsx[i] - 1*pixelSize): 
              Rechts = False
        if Rechts == True:
          goRight()
      #Rotate
      elif event.key == pygame.K_w:
        pixelx = functies.rotatex(piece,pixelSize,rotations,pixelx)
        pixely = functies.rotatey(piece,pixelSize,rotations,pixely)
        rotations += 1
        for k in range(len(pixelx)):
          if pixelx[k] < (LINE_LEFT_X): 
            OutOfBoundsLeft = True
          elif pixelx[k] > (LINE_RIGHT_X - 1 * pixelSize):
            OutOfBoundsRight = True
        if OutOfBoundsLeft == True:
          goRight()
          if piece == "I" and rotations == 1:
            goRight()
          OutOfBoundsLeft = False
        elif OutOfBoundsRight == True:
          goLeft()
          if piece == "I" and rotations == 3:
            goLeft()
          OutOfBoundsRight = False 
      #Hold
      elif event.key == pygame.K_c:
        if HoldAble == True:
          if hold == 0:
            hold = piece
            piece = piece1
            rotations = 0
            piece1 = piece2
            piece2 = piece3
            piece3 = random.choice(pieces)
            pixelx = functies.decodex(piece, pixelSize, relative)
            pixely = functies.decodey(piece, pixelSize)
            HoldAble = False
          else:
            tempPiece = piece
            piece = hold
            rotations = 0
            hold = tempPiece
            pixelx = functies.decodex(piece, pixelSize, relative)
            pixely = functies.decodey(piece, pixelSize)
            HoldAble = False
      #Move down
      elif event.key == pygame.K_s:
        GoDown()
      #Dropdown
      elif event.key == pygame.K_SPACE:
        while DropDown == True:
          for k in range(len(pixely)):
            if pixely[k] == (LINE_BOTTOM_Y - 1*pixelSize):
              DropDown = False
          for i in range(len(coordsy)):
            for j in range(len(pixely)):
              if (coordsy[i]) ==  pixely[j] - 1*pixelSize and pixelx[j] == (coordsx[i]): 
                DropDown = False
          if DropDown == True:
            GoDown()
          tempScore = score
          functies.collider(LINE_BOTTOM_Y, xycolour, PLAYER_COLOUR, score_increment, pixelSize, pieces, relative, coordsx, coordsy) 
          if score != tempScore:
            DropDown = False
    
  # W = -1y en S = +1y want linksboven is (0,0) dus omhoog gaan is -1y en omlaag gaan is +1y 
  if rotations == 4:
    rotations = 0
  #------------------------------------------------------------------------------------------------------------------------------------------------------------------
  #Collider
  functies.collider(LINE_BOTTOM_Y, xycolour, PLAYER_COLOUR, score_increment, pixelSize, pieces, relative, coordsx, coordsy)
  
  #Placeholder tekenen
  for i in range(len(coordsx)):
    player_placeholder = pygame.Rect(coordsx[i],coordsy[i],1*pixelSize,1*pixelSize)
    TempColour = xycolour[i]
    pygame.draw.rect(screen, TempColour, player_placeholder)

  #Rij-weghaler
  for i in coordsy:
    levels = coordsy.count(i)
    if levels >= 10:
      while x <= levels:
        plaats = coordsy.index(i)
        coordsy.remove(i)
        coordsx.pop(plaats)
        xycolour.pop(plaats)
        x = x + 1
      x = 1
      for x in range(0,len(coordsy)):
        if coordsy[x] <= i:
          coordsy[x] += 1*pixelSize
          x = x + 1
      x = 1 
      score += 10 * score_increment

  

  #Score setup
  font = pygame.font.Font(None, 36)
  score_text = font.render(f'Score: {score}', True, (255, 255, 255))
  screen.blit(score_text, (10, 10))

  #Next piece setup
  Next_piece = font.render(f'Next:', True, (255, 255, 255))
  screen.blit(Next_piece, (17 *pixelSize, 0 * pixelSize))

  #Hold setup
  Holdprint = font.render(f'Hold:', True, (255, 255, 255))
  screen.blit(Holdprint, (10, 10 * pixelSize))

  #Refresh van scherm
  pygame.display.update()

#Score
print("Game over")
print("Score:", score)
#---------------------------------------------------      

pygame.quit()
sys.exit()