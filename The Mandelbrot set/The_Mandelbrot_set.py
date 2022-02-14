from os import environ 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame 

pygame.font.init() 

def color_input_R () : 

  colR = int(input('Enter the value of R (0..255): '))
  D = colR
  if(colR > 255 or colR < 0): 
    print('Error entering values, please try again: ')
    D = color_input_R() 
  return D 

def color_input_G () :

  colG = int(input('Enter the value of G (0..255): '))
  D = colG
  if(colG > 255 or colG < 0):
    print('Error entering values, please try again: ')
    D = color_input_G()
  return D

def color_input_B () :

  colB = int(input('Enter the value of B (0..255): '))
  D = colB
  if(colB > 255 or colB < 0):
    print('Error entering values, please try again: ')
    D = color_input_B()
  return D

def color_main():
 
  color_ans = input('Do you want to enter a color? (yes / no) (default blue): ') 
  color_ans = color_ans.lower() 
  if(color_ans == 'yes'): 
   
    colR = color_input_R() 
    colG = color_input_G() 
    colB = color_input_B()

  else: 
   
    colR = 235
    colG = 239
    colB = 61

  return colR, colG, colB 

iterations = int(input('Number of iterations for the set: ')) 

axes_ans = input('Show axes? (yes / no): ')  
axes_ans = axes_ans.lower() 

colR, colG, colB = color_main()   

win = pygame.display.set_mode((1000, 1000)) 
win.fill((255 - colR, 255 - colG, 255 - colB))

white = (255, 255, 255) 

pygame.display.set_caption("Mandelbrot Set") 

for x in range(900): 
  for y in range(900): 
    
    i = (x - 450) / 225 
    j = (y - 450) / 225 
    
    c = i + j * (-1) ** .5 

    In_Mandelbrot = True 
    z = 0 

    for k in range(iterations):
      z = z ** 2 + c 
      if abs(z) >= 2: 
        In_Mandelbrot = False 
        break 

    if (In_Mandelbrot): 
      pygame.draw.line(win, (0,0,0), (x + 50, y + 50), (x + 50, y + 50), 1) 

    else:

      base = round(255 * k / iterations) 

      colorR = abs(abs(base - colR) - 255) 
      colorG = abs(abs(base - colG) - 255)  
      colorB = abs(abs(base - colB) - 255) 

      pygame.draw.line(win, (colorR, colorG, colorB), (x + 50, y + 50), (x + 50, y + 50), 1) 

if (axes_ans == 'yes'): 

    pygame.draw.line(win, white, (0, 500), (1000, 500), 1) 
    pygame.draw.line(win, white, (500, 0), (500, 1000), 1)    

    pygame.draw.line(win, white, (50, 495), (50, 505), 1) 
    pygame.draw.line(win, white, (275, 495), (275, 505), 1) 
    pygame.draw.line(win, white, (725, 495), (725, 505), 1) 
    pygame.draw.line(win, white, (950, 495), (950, 505), 1) 

    pygame.draw.line(win, white, (495, 50), (505, 50), 1) 
    pygame.draw.line(win, white, (495, 275), (505, 275), 1) 
    pygame.draw.line(win, white, (495, 725), (505, 725), 1) 
    pygame.draw.line(win, white, (495, 950), (505, 950), 1) 

    font = pygame.font.SysFont('calibri', 20) 

    text1 = font.render("1", True, white)  
    text2 = font.render("2", True, white)  
    text0 = font.render("0", True, white)  
    text_1 = font.render("-1", True, white)  
    text_2 = font.render("-2", True, white)  

    win.blit(text0, [475,515]) 

    win.blit(text1, [720,515]) 
    win.blit(text2, [945,515]) 
    win.blit(text_1, [265,515]) 
    win.blit(text_2, [40,515]) 

    win.blit(text_1, [475,715]) 
    win.blit(text_2, [475,940]) 
    win.blit(text1, [480,265]) 
    win.blit(text2, [480,40])
    
    font = pygame.font.SysFont('calibri', 24) 

    textRe = font.render("Re[c]", True, white)
    textIm = font.render("Im[c]", True, white) 
  
    win.blit(textRe, [945,445]) 
    win.blit(textIm, [540,36]) 

RUN = True 
while RUN: 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      RUN = False 
  pygame.display.update() 

pygame.quit() 
