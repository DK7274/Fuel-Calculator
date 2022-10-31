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
button_font = pygame.font.SysFont("Arial",15)
title_font = pygame.font.SysFont("Arial",50)
a = 0
resetScreen = False

#setting up window#
win =pygame.display.set_mode((600,600))
pygame.display.set_caption("Fuel Calculator")
bgColor = (50, 131, 168)
win.fill(bgColor)
pygame.display.flip()

##defining windows##
def startWindow(): #defines initial loading screen that displays a title
    global a
    global loading_array
    global calcStart
    title_text = title_font.render("Fuel Usage Calculator",True, text_color)
    win.blit(title_text,(100,200))
    pygame.display.update()
    time.sleep(2)
    calcStart = True

def menuWindow(): #initialises selection screen which shows different vehicle selection
    global mouseX
    global mouseY
    global resetScreen
    if resetScreen == False:
        win.fill(bgColor)
        pygame.display.flip()
        resetScreen = True
    button_width = 100
    button_height = 50
    currentButtonList = ["penis","balls"]
    buttonList1 =["PC-21","BC Super King","BAE Hawk","Dassault Falcon 7X","Boeing 737"]
    buttonList2 = ["C-130J","C-27J","C-17A","KC-30","P-8A Poseiden"]
    buttonList3 = ["AP-3C Orion","MC-55A Peregrine","EA-18G Growler","FA-18 super hornet","F-35A Lightning II"]
    button1_rect = [100,100,button_width,button_height]
    button1_text = button_font.render(currentButtonList[0],True,text_color)
    button2_rect = [250,100,button_width,button_height]
    button2_text = button_font.render(currentButtonList[1],True,text_color)
    pygame.draw.rect(win,button_color,button1_rect)
    win.blit(button1_text, (button1_rect[0], button1_rect[1]))
    pygame.draw.rect(win,button_color,button2_rect)
    win.blit(button2_text,(button2_rect[0],button2_rect[1]))
    pygame.display.update()

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