from PIL import ImageGrab
import win32gui
import msvcrt 
import time
import pygame
import ctypes
from random import randint

pygame.init()

window = pygame.display.set_mode((300,200))
pygame.display.set_caption('Color Picker V1 - Python')
clock = pygame.time.Clock()

#Set the fonts
title = pygame.font.SysFont("comicsansms", 18,True,False)
text = pygame.font.SysFont("comicsansms", 15,True,False)
credit = pygame.font.SysFont("arial", 10,True,False)

#Get the screen size
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)


window.fill(pygame.Color("black"))
Text = title.render("Rule the world and press L", 1, (255,255,255))
window.blit(Text, (25, 10))

#Feel free to change the credit <3
Credit  = credit.render("--By Guillaume D. @GuillaumeBeboop - Python 3.6--", 1, (255,255,255))
Licence = credit.render("-- Licence : Creative Commons BY NC SA--", 1, (255,255,255))
#Random text
randomtext = ["Keep Calm and press L","FUSH ROH DDD...PRESS L","We can have some fun","Damn, you found THE color","I'm not even tired","Feel free to use it","Share the colors","Hey, You're still there ?","Python over the world","French tech... uhg wait ?","Rule the world and press L","Press W. Just kidding, it's L","JUST DO IT. PRESS L","BLABLA L BLA BLA BLA","You're awesome <3 - Still L","Le meilleur color picker","In python we code - Still L","Is it your favourite color?"]

px=ImageGrab.grab().load()
pixel = 1 
pygame.display.update()
while pixel :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pixel =0         
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_l:
                #Get the cursor position
                flags, hcursor, (x,y) = win32gui.GetCursorInfo()
        
                if(0<=x<width and 0<=y<height):
                    #Blit the update
                    window.fill(pygame.Color("black"))
                    Text = title.render(randomtext[randint(0,17)], 1, (255,255,255))
                    window.blit(Text, (25, 10))
                    
                    #Get the RGB color
                    red,green,blue=px[x,y]
                    color = (red,green,blue)
                    rgb = "R-"+str(red)+" G-"+str(green)+" B-"+str(blue)
                    
                    #Get HEX from RGB
                    hexa = "#%02x%02x%02x" % (red, green, blue)

                    #Blit the Rgb Color
                    RGBrender = text.render(rgb, 1, (255,255,255))
                    window.blit(RGBrender, (10, 100))
                    
                    #If the color is white, we change the border color
                    if(hexa=="#ffffff"):
                        border = (238,75,182)
                    else:
                        border = (255,255,255)
                    #Blit the color viewer
                    pygame.draw.rect(window, border, pygame.Rect(188, 98, 30, 30))                    
                    pygame.draw.rect(window, color, pygame.Rect(190, 100, 26, 26))

                    #Blit the Hex color
                    HEXArender = text.render(hexa, 1, (255,255,255))
                    window.blit(HEXArender, (10, 130))

                    #Blit the credit
                    window.blit(Credit, (40, 170))
                    window.blit(Licence, (40, 180))
                else:
                    #UGH ?
                    window.fill(pygame.Color("black"))
                    Text = title.render("!#[à@&& N**ope", 1, (255,255,255))
                    window.blit(Text, (30, 10))
                    
                    rgb = "R-### G-### B-###"
                    
                    #BEEP BOOOP ERR ERRR
                    hexa = "#Out of screen" 

                    #NOPE NOPE
                    RGBrender = text.render(rgb, 1, (255,255,255))
                    window.blit(RGBrender, (10, 100))
                    
                    #ERROR #!$
                    border = (255,255,255)
                    color = (255,2,2)
                    
                    #SHMOUF POOF
                    pygame.draw.rect(window, border, pygame.Rect(218, 98, 30, 30))                    
                    pygame.draw.rect(window, color, pygame.Rect(220, 100, 26, 26))

                    #ZZZZZZZZ
                    HEXArender = text.render(hexa, 1, (255,255,255))
                    window.blit(HEXArender, (10, 130))

                    ##"^$"ùùù!!!!
                    window.blit(Credit, (40, 170))
                    window.blit(Licence, (40, 180))
            pygame.display.update()
            clock.tick(60)  
pygame.quit()
