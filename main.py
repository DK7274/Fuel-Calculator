import pygame

pygame.init()
import time

# variable setup#
run = True
calculationMode = False
consumptionMode = False
mouseX, mouseY = (0, 0)  # gets cursor position#
calcStart = False
text_color = (0, 0, 0)
button_color = (40, 81, 148)
button_over_color = (23, 46, 84)
button_font = pygame.font.SysFont("Arial", 15)
title_font = pygame.font.SysFont("Arial", 50)
a = 0
resetScreen = False
currentButtonList = ["penis", "balls", "cum", "sex", "amogus"]
pageNumber = 1

# setting up window#
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fuel Calculator")
bgColor = (50, 131, 168)
win.fill(bgColor)
pygame.display.flip()


##defining windows##
def startWindow():  # defines initial loading screen that displays a title
    global a
    global loading_array
    global calcStart
    title_text = title_font.render("Fuel Usage Calculator", True, text_color)
    win.blit(title_text, (100, 200))
    pygame.display.update()
    time.sleep(2)
    calcStart = True


def menuWindow():  # initialises selection screen which shows different vehicle selection
    global mouseX
    global mouseY
    global resetScreen
    global currentButtonList
    global pageNumber
    if resetScreen == False:
        win.fill(bgColor)
        pygame.display.flip()
        resetScreen = True
    button_width = 100
    button_height = 50
    buttonList1 = ["PC-21", "BC Super King", "BAE Hawk", "Dassault Falcon 7X", "Boeing 737"]
    buttonList2 = ["C-130J", "C-27J", "C-17A", "KC-30", "P-8A Poseiden"]
    buttonList3 = ["AP-3C Orion", "MC-55A Peregrine", "EA-18G Growler", "FA-18 super hornet", "F-35A Lightning II"]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION: #sets mouseX and mouseY to where the mouse has moved to
            mouseX,mouseY = event.pos

    # defining button text and positions
    button1_rect = [100, 100, button_width, button_height]
    button1_text = button_font.render(currentButtonList[0], True, text_color)
    button2_rect = [250, 100, button_width, button_height]
    button2_text = button_font.render(currentButtonList[1], True, text_color)
    button3_rect = [400, 100, button_width, button_height]
    button3_text = button_font.render(currentButtonList[2], True, text_color)
    button4_rect = [100, 250, button_width, button_height]
    button4_text = button_font.render(currentButtonList[3], True, text_color)
    button5_rect = [250, 250, button_width, button_height]
    button5_text = button_font.render(currentButtonList[4], True, text_color)
    button6_rect = [400, 250, button_width, button_height]
    button6_text = button_font.render("next page", True, text_color)

    # drawing buttons and names of buttons
    pygame.draw.rect(win, button_color, button1_rect)
    win.blit(button1_text, (button1_rect[0], button1_rect[1]))
    pygame.draw.rect(win, button_color, button2_rect)
    win.blit(button2_text, (button2_rect[0], button2_rect[1]))
    pygame.draw.rect(win, button_color, button3_rect)
    win.blit(button3_text, (button3_rect[0], button3_rect[1]))
    pygame.draw.rect(win, button_color, button4_rect)
    win.blit(button4_text, (button4_rect[0], button4_rect[1]))
    pygame.draw.rect(win, button_color, button5_rect)
    win.blit(button5_text, (button5_rect[0], button5_rect[1]))
    pygame.draw.rect(win, button_color, button6_rect)
    win.blit(button6_text, (button6_rect[0], button6_rect[1]))

    #part of code that tells the color of button change to button_over_color if mouse over it
    if(button1_rect[0] <= mouseX <= button1_rect[0] + button1_rect[2] and
            button1_rect[1] <= mouseY <= button1_rect[1] + button1_rect[3]):
        print("test")
        pygame.draw.rect(win,button_over_color,button1_rect)
    elif(button2_rect[0] <= mouseX <= button2_rect[0] + button2_rect[2] and
            button2_rect[1] <= mouseY <= button2_rect[1] + button2_rect[3]):
        pygame.draw.rect(win, button_over_color, button2_rect)
    elif(button3_rect[0] <= mouseX <= button3_rect[0] + button3_rect[2] and
            button3_rect[1] <= mouseY <= button3_rect[1] + button3_rect[3]):
        pygame.draw.rect(win, button_over_color, button3_rect)
    elif(button4_rect[0] <= mouseX <= button4_rect[0] + button4_rect[2] and
            button4_rect[1] <= mouseY <= button4_rect[1] + button4_rect[3]):
        pygame.draw.rect(win, button_over_color, button4_rect)
    elif(button5_rect[0] <= mouseX <= button5_rect[0] + button5_rect[2] and
            button5_rect[1] <= mouseY <= button5_rect[1] + button5_rect[3]):
        pygame.draw.rect(win, button_over_color, button5_rect)
    elif(button6_rect[0] <= mouseX <= button6_rect[0] + button6_rect[2] and
            button6_rect[1] <= mouseY <= button6_rect[1] + button6_rect[3]):
        pygame.draw.rect(win, button_over_color, button6_rect)

    pygame.display.update()


def calculationWindow():
    pass


def consumptionWindow():
    pass


###main loop###
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if calculationMode == True:
        calculationWindow()
    elif consumptionMode == True:
        consumptionWindow()
    elif calcStart == True:
        menuWindow()
    else:
        startWindow()
#####
pygame.quit()
