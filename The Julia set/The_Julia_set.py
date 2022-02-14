from os import environ 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' 

import pygame 
import math

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
        if(colR == 0):
            colR += 1
        colG = color_input_G() 
        if(colG == 0):
            colG += 1
        colB = color_input_B()
        if(colB == 0):
            colB += 1

    else: 
        
        colR = 1
        colG = 1
        colB = 255

    return colR, colG, colB

def complex_input (R):

    Re = float(input('Enter Re [c]: ')) 
    Im = float(input('Enter Im[c]: ')) 

    D1, D2 = Re, Im * (-1)
    if((Re ** 2 + Im ** 2) ** .5 > R ** 2 - R):
        print("Warning! Given this number, Julia's set will not fit in the radius!")
        ans = input('Do you want to enter again? (yes / no): ')
        ans = ans.lower()
        if(ans == 'yes'):
            T = complex_input(R)
            D1, D2 = T[0], T[1] 
    return D1, D2

def complex_main (R): 

    num_ans = input('Do you want to enter C? (yes / no) (default c = -0.74543 - 0.11301i): ') 
    num_ans = num_ans.lower() 

    Re_C = -0.74543 
    Im_C = 0.11301 
    
    if(num_ans == 'yes'):
    
        Re_C, Im_C = complex_input(R)
    
    c = complex(Re_C, Im_C) 
   
    return c 

def escape_radius():
    
    esc_ans = input('Do you want to enter the exit radius? (yes / no) (default R = 3.5): ')
    esc_ans = esc_ans.lower()
    if (esc_ans == 'yes'):
        R = float(input('Enter the exit radius: '))
    else:
        R = 3.5 
    return R

R = escape_radius() 
loop = R / 2
c = complex_main(R) 

colR, colG, colB = color_main() 

max_iteration = int(input('Enter the maximum iteration value (1000 recommended): '))

win = pygame.display.set_mode((1000, 1000)) 

pygame.display.set_caption("Julia Set")

for x in range(1000): 
    for y in range(1000): 
        
        Re_Z = x / 1000 * R - loop 
        Im_Z = y / 1000 * R - loop 

        z = complex(Re_Z, Im_Z)
        iteration = 0 
        
        while abs(z) < R and iteration < max_iteration: 

            z = z ** 2 + c
            iteration += 1 
        
        ratio = iteration / max_iteration
        base = round(255 * ratio)
        
        color1 = (((base % colR << 3) % colR + 25 * colR // 50)) - 255 * (((base % colR << 3) % colR + 25 * colR // 50) // 255)
        color2 = (((base % colG << 3) % colG + 25 * colG // 50)) - 255 * (((base % colG << 3) % colG + 25 * colG // 50) // 255) 
        color3 = (((base % colB << 3) % colB + 25 * colB // 50)) - 255 * (((base % colB << 3) % colB + 25 * colB // 50) // 255) 

        if(color1 < 50 and color2 < 50 and color3 < 50):
            color1 = 255 - color1 - 30 * colR // 50
            color2 = 255 - color2 - 30 * colG // 50
            color3 = 255 - color3 - 30 * colB // 50
            color = (color3, color2, color1)
        else :
            color = (color1 , color2, color3)

        pygame.draw.line(win, color , (x, y), (x, y), 1) 
        
RUN = True 
while RUN: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            RUN = False 
    pygame.display.update() 

pygame.quit() 
