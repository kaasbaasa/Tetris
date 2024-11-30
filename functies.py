import pygame
import random

#---------------------------------------------Defining-------------------------------------------------------
def decodex(piece, pixelSize, relative):
  if piece == "I":
    x = [5*pixelSize + (relative / 2),5*pixelSize + (relative / 2),5*pixelSize + (relative / 2),5*pixelSize + (relative / 2)]
  elif piece == "J":
    x =[5*pixelSize + (relative / 2),5*pixelSize + (relative / 2),5*pixelSize + (relative / 2),4*pixelSize + (relative / 2)]
  elif piece == "L":
    x =[5*pixelSize + (relative / 2), 5*pixelSize + (relative / 2),5*pixelSize + (relative / 2),6*pixelSize + (relative / 2)]
  elif piece == "O":
    x = [4*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 4*pixelSize + (relative / 2), 5*pixelSize + (relative / 2)]
  elif piece == "S":
    x = [6*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 4*pixelSize + (relative / 2)]
  elif piece == "T":
    x = [4*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 6*pixelSize + (relative / 2)]
  elif piece == "Z":
    x = [4*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 5*pixelSize + (relative / 2), 6*pixelSize + (relative / 2)]
  return x

def decodey(piece, pixelSize): 
  if piece == "I":
    y = [-1 *pixelSize, 0*pixelSize, 1*pixelSize, 2*pixelSize]
  elif piece == "J":
    y = [0*pixelSize, 1*pixelSize, 2*pixelSize, 2*pixelSize]
  elif piece == "L":
    y = [0*pixelSize, 1*pixelSize, 2*pixelSize, 2*pixelSize]
  elif piece ==  "O": 
    y = [0*pixelSize,0*pixelSize,1*pixelSize,1*pixelSize]
  elif piece == "S":
    y =[0*pixelSize, 0*pixelSize, 1*pixelSize, 1*pixelSize]
  elif piece == "T":
    y =[0*pixelSize, 0*pixelSize, 1*pixelSize, 0*pixelSize]
  elif piece == "Z":
    y =[0*pixelSize,0*pixelSize,1*pixelSize,1*pixelSize]
  return y
#-----------------------------------------Rotation------------------------------------------------------------
def rotatex(piece, pixelSize, rotations, pixelx):
  if piece == "I":
    if rotations == 0:
      pixelx[0] -= 2*pixelSize
      pixelx[1] -= 1*pixelSize
      pixelx[3] += 1*pixelSize
    elif rotations == 1:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] -= 2*pixelSize
    elif rotations == 2:
      pixelx[0] += 2*pixelSize
      pixelx[1] += 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 3:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] += 2*pixelSize
  elif piece == "J":
    if rotations == 0:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] += 0*pixelSize
    elif rotations == 1:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] += 2*pixelSize
    elif rotations == 2:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] -= 0*pixelSize
    elif rotations == 3:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] -= 2*pixelSize
  elif piece == "L":
    if rotations == 0:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] -= 2*pixelSize
    elif rotations == 1:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] += 0*pixelSize
    elif rotations == 2:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] += 2*pixelSize
    elif rotations == 3:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] -= 0*pixelSize
  elif piece == "O":
    pixelx = pixelx
  elif piece == "S":
    if rotations == 0:
      pixelx[0] += 0*pixelSize
      pixelx[1] += 1*pixelSize
      pixelx[3] += 1*pixelSize
    elif rotations == 1:
      pixelx[0] -= 2*pixelSize
      pixelx[1] -= 1*pixelSize
      pixelx[3] += 1*pixelSize
    elif rotations == 2:
      pixelx[0] += 0*pixelSize
      pixelx[1] -= 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 3:
      pixelx[0] += 2*pixelSize
      pixelx[1] += 1*pixelSize
      pixelx[3] -= 1*pixelSize
  elif piece == "T":
    if rotations == 0:
      pixelx[0] += 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 1:
      pixelx[0] += 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 2:
      pixelx[0] -= 1*pixelSize
      pixelx[2] += 1*pixelSize
      pixelx[3] += 1*pixelSize
    elif rotations == 3:
      pixelx[0] -= 1*pixelSize
      pixelx[2] -= 1*pixelSize
      pixelx[3] += 1*pixelSize
  elif piece == "Z":
    if rotations == 0:
      pixelx[0] += 2*pixelSize
      pixelx[1] += 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 1:
      pixelx[0] -= 0*pixelSize
      pixelx[1] -= 1*pixelSize
      pixelx[3] -= 1*pixelSize
    elif rotations == 2:
      pixelx[0] -= 2*pixelSize
      pixelx[1] -= 1*pixelSize
      pixelx[3] += 1*pixelSize
    elif rotations == 3:
      pixelx[0] += 0*pixelSize
      pixelx[1] += 1*pixelSize
      pixelx[3] += 1*pixelSize
  return pixelx

def rotatey(piece, pixelSize, rotations, pixely):
  if piece == "I":
    if rotations == 0:
      pixely[0] += 2*pixelSize
      pixely[1] += 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 1:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] -= 2*pixelSize
    elif rotations == 2:
      pixely[0] -= 2*pixelSize
      pixely[1] -= 1*pixelSize
      pixely[3] += 1*pixelSize
    elif rotations == 3:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] += 2*pixelSize
  elif piece == "J":
    if rotations == 0:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] -= 2*pixelSize
    elif rotations == 1:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] += 0*pixelSize
    elif rotations == 2:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] += 2*pixelSize
    elif rotations == 3:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] -= 0*pixelSize
  elif piece == "L":
    if rotations == 0:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] -= 0*pixelSize
    elif rotations == 1:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] -= 2*pixelSize
    elif rotations == 2:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] += 0*pixelSize
    elif rotations == 3:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] += 2*pixelSize
  elif piece == "O":
    pixely = pixely
  elif piece == "S":
    if rotations == 0:
      pixely[0] += 2*pixelSize
      pixely[1] += 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 1:
      pixely[0] += 0*pixelSize
      pixely[1] += 1*pixelSize
      pixely[3] += 1*pixelSize
    elif rotations == 2:
      pixely[0] -= 2*pixelSize
      pixely[1] -= 1*pixelSize
      pixely[3] += 1*pixelSize
    elif rotations == 3:
      pixely[0] += 0*pixelSize
      pixely[1] -= 1*pixelSize
      pixely[3] -= 1*pixelSize
  elif piece == "T":
    if rotations == 0:
      pixely[0] -= 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] += 1*pixelSize
    elif rotations == 1:
      pixely[0] += 1*pixelSize
      pixely[2] -= 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 2:
      pixely[0] += 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 3:
      pixely[0] -= 1*pixelSize
      pixely[2] += 1*pixelSize
      pixely[3] += 1*pixelSize
  elif piece == "Z":
    if rotations == 0:
      pixely[0] += 0*pixelSize
      pixely[1] += 1*pixelSize
      pixely[3] += 1*pixelSize
    elif rotations == 1:
      pixely[0] += 2*pixelSize
      pixely[1] += 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 2:
      pixely[0] -= 0*pixelSize
      pixely[1] -= 1*pixelSize
      pixely[3] -= 1*pixelSize
    elif rotations == 3:
      pixely[0] -= 2*pixelSize
      pixely[1] -= 1*pixelSize
      pixely[3] += 1*pixelSize
  return pixely
#-----------------------------------------Collider---------------------------------------------------------------
def collider(LINE_BOTTOM_Y, xycolour, PLAYER_COLOUR, score_increment, pixelSize, pieces, relative, coordsx, coordsy):
  import main
  def afterCollision():
        main.piece = main.piece1
        main.piece1 = main.piece2
        main.piece2 = main.piece3
        main.piece3 = random.choice(pieces)
        main.pixelx = decodex(main.piece, pixelSize, relative)
        main.pixely = decodey(main.piece, pixelSize)
        main.score += score_increment
        main.rotations = 0
        main.HoldAble = True
  #Floor collider
  for j in range(len(main.pixely)):
    if main.pixely[j] == LINE_BOTTOM_Y:
      for i in range(0,len(main.pixelx)):
        coordsx.append(main.pixelx[i])
        coordsy.append(main.pixely[i]-1*pixelSize)
        xycolour.append(PLAYER_COLOUR)
      afterCollision()
#Player Collider
  for i in range(len(coordsx)):
    for j in range(len(main.pixelx)):
      if main.pixely[j] == (coordsy[i]-1*pixelSize) and (coordsx[i]) == main.pixelx[j]:
        for k in range(0,len(main.pixelx)):
          coordsx.append(main.pixelx[k])
          coordsy.append(main.pixely[k])
          xycolour.append(PLAYER_COLOUR)
        afterCollision()      
#-----------------------------------------PlayerColour--------------------------------------------------------
def ColourDefiner (Colour):
  if Colour == "Cyan":
    return (0,255,255)
  elif Colour == "Yellow":
    return (255,255,0)
  elif Colour == "Purple":
    return (128,0,128)
  elif Colour == "Green":
    return (0,255,0)
  elif Colour == "Red":
    return (255,0,0)
  elif Colour == "Blue":
    return (0,0,255)
  elif Colour == "Orange": 
    return (255,127,0)

def colourpicker(piece):
  if piece == "I":
    Colour = "Cyan"
  elif piece == "J":
    Colour = "Blue"
  elif piece == "L":
    Colour = "Orange"
  elif piece == "O":
    Colour = "Yellow"
  elif piece == "S":
    Colour = "Green"
  elif piece == "T":
    Colour = "Purple"
  elif piece == "Z":
    Colour = "Red"
  ColourResult = ColourDefiner(Colour)
  return ColourResult