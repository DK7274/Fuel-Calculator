import pygame
pygame.init()

#variable setup#
run = True
calculationMode = False
consumptionMode = False
mouseX,mouseY = (0,0) #gets cursor position#

#setting up window#
win =pygame.display.set_mode((600,600))
pygame.display.set_caption("Fuel Calculator")
bgColor = (50, 131, 168)
win.fill(bgColor)
pygame.display.flip()

##defining windows##
def menuWindow():
    global button_rect
#blitting the menu window
    button_text_color = (0,0,0)
    title_text_color = (0,0,0)
    button_color = (40, 81, 148)
    button_over_color = (23, 46, 84)
    button_width = 200
    button_height = 100
    button1_rect = [100,100,button_width,button_height]
    button_font = pygame.font.SysFont("Arial",20)

def calculationWindow():

def consumptionWindow():


###main loop###
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    if calculationMode == True:
        calculationWindow()
    elif consumptionMode == True:
        consumptionWindow()
    else:
        menuWindow()
#####
pygame.quit()