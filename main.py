import pygame
pygame.init()
import time

#variable setup#
run = True
calculationMode = False
consumptionMode = False
mouseX,mouseY = (0,0) #gets cursor position#
calcStart = False
text_color = (0, 0, 0)
button_color = (40, 81, 148)
button_over_color = (23, 46, 84)
button_font = pygame.font.SysFont("Arial",20)
title_font = pygame.font.SysFont("Arial",50)
a = 0
loading_array = [".",".",".",".",".",".",".",".",".","."]


#setting up window#
win =pygame.display.set_mode((600,600))
pygame.display.set_caption("Fuel Calculator")
bgColor = (50, 131, 168)
win.fill(bgColor)
pygame.display.flip()

##defining windows##
def startWindow():
    global a
    global loading_array
    title_text = title_font.render("Fuel Usage Calculator",True, text_color)
    win.blit(title_text,(100,200))
    pygame.display.update()

def menuWindow():
    pass

def calculationWindow():
    pass

def consumptionWindow():
    pass

###main loop###
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    if calculationMode  == True:
        calculationWindow()
    elif consumptionMode == True:
        consumptionWindow()
    elif calcStart == True:
        menuWindow()
    else:
        startWindow()
#####
pygame.quit()