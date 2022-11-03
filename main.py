import pygame

pygame.init()
import time

# variable setup#
clock = pygame.time.Clock()
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
currentButtonList = ["PC-21", "BC Super King", "BAE Hawk", "Dassault Falcon 7X", "Boeing 737"]
pageNumber = 1
buttonNumber = 0
aircraftData = []

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


def getStatValues():  # function to assign txt file values to an array
    global buttonNumber
    global pageNumber
    global aircraftData
    dataRead = []
    with open('fuelValues.txt', 'rt') as myfile:
        for myline in myfile:
            dataRead.append(myline)
    if pageNumber == 1:  # set of if and elif statements that assigns the lines in the text document into an array
        if buttonNumber == 1:
            aircraftData = [dataRead[2].strip(), int(dataRead[3]), int(dataRead[4]), int(dataRead[5]),
                            float(dataRead[6])]
        elif buttonNumber == 2:
            aircraftData = [dataRead[7].strip(), int(dataRead[8]), int(dataRead[9]), int(dataRead[10]),
                            float(dataRead[11])]
        elif buttonNumber == 3:
            aircraftData = [dataRead[12].strip(), int(dataRead[13]), int(dataRead[14]), int(dataRead[15]),
                            float(dataRead[16])]
        elif buttonNumber == 4:
            aircraftData = [dataRead[17].strip(), int(dataRead[18]), int(dataRead[19]), int(dataRead[20]),
                            float(dataRead[21])]
        elif buttonNumber == 5:
            aircraftData = [dataRead[22].strip(), int(dataRead[23]), int(dataRead[24]), int(dataRead[25]),
                            float(dataRead[26])]
    elif pageNumber == 2:
        if buttonNumber == 1:
            aircraftData = [dataRead[27].strip(), int(dataRead[28]), int(dataRead[29]), int(dataRead[30]),
                            float(dataRead[31])]
        elif buttonNumber == 2:
            aircraftData = [dataRead[32].strip(), int(dataRead[33]), int(dataRead[34]), int(dataRead[35]),
                            float(dataRead[36])]
        elif buttonNumber == 3:
            aircraftData = [dataRead[37].strip(), int(dataRead[38]), int(dataRead[39]), int(dataRead[40]),
                            float(dataRead[41])]
        elif buttonNumber == 4:
            aircraftData = [dataRead[42].strip(), int(dataRead[43]), int(dataRead[44]), int(dataRead[45]),
                            float(dataRead[46])]
        elif buttonNumber == 5:
            aircraftData = [dataRead[47].strip(), int(dataRead[48]), int(dataRead[49]), int(dataRead[50]),
                            float(dataRead[51])]
    elif pageNumber == 3:
        if buttonNumber == 1:
            aircraftData = [dataRead[52].strip(), int(dataRead[53]), int(dataRead[54]), int(dataRead[55]),
                            float(dataRead[56])]
        elif buttonNumber == 2:
            aircraftData = [dataRead[57].strip(), int(dataRead[58]), int(dataRead[59]), int(dataRead[60]),
                            float(dataRead[61])]
        elif buttonNumber == 3:
            aircraftData = [dataRead[62].strip(), int(dataRead[63]), int(dataRead[64]), int(dataRead[65]),
                            float(dataRead[66])]
        elif buttonNumber == 4:
            aircraftData = [dataRead[67].strip(), int(dataRead[68]), int(dataRead[69]), int(dataRead[70]),
                            float(dataRead[71])]
        elif buttonNumber == 5:
            aircraftData = [dataRead[72].strip(), int(dataRead[73]), int(dataRead[74]), int(dataRead[75]),
                            float(dataRead[76])]
    print(aircraftData)


def menuWindow():  # initialises selection screen which shows different vehicle selection
    global mouseX
    global mouseY
    global resetScreen
    global currentButtonList
    global pageNumber
    global buttonNumber
    global run
    clock.tick(15)
    if resetScreen == False:  # refrshes beackground of screen
        win.fill(bgColor)
        pygame.display.flip()
        resetScreen = True
    button_width = 100
    button_height = 50
    # list of aircraft on different pages
    buttonList1 = ["PC-21", "BC Super King", "BAE Hawk", "Dassault Falcon 7X", "Boeing 737"]
    buttonList2 = ["C-130J", "C-27J", "C-17A", "KC-30", "P-8A Poseiden"]
    buttonList3 = ["AP-3C Orion", "MC-55A Peregrine", "EA-18G Growler", "FA-18 Super Hornet", "F-35A Lightning II"]

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
    # getting mouse position during mouse motion and on clicking#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos  # sets mouse X and mouse Y for
            if (button6_rect[0] <= mouseX <= button6_rect[0] + button6_rect[
                2] and  # for clicking on the 'next' button and makes it switch aircraft lists#
                    button6_rect[1] <= mouseY <= button6_rect[1] + button6_rect[3]):
                pageNumber += 1
                print("switch page")
                if pageNumber == 1:
                    currentButtonList = buttonList1
                    resetScreen = False
                elif pageNumber == 2:
                    currentButtonList = buttonList2
                    resetScreen = False
                elif pageNumber == 3:
                    currentButtonList = buttonList3
                    resetScreen = False
                else:
                    pageNumber = 1
                    currentButtonList = buttonList1
                    resetScreen = False
            elif (button1_rect[0] <= mouseX <= button1_rect[0] + button1_rect[2] and
                  button1_rect[1] <= mouseY <= button1_rect[1] + button1_rect[3]):
                buttonNumber = 1
                print(buttonNumber)
                getStatValues()
            elif (button2_rect[0] <= mouseX <= button2_rect[0] + button2_rect[2] and
                  button2_rect[1] <= mouseY <= button2_rect[1] + button2_rect[3]):
                buttonNumber = 2
                print(buttonNumber)
                getStatValues()
            elif (button3_rect[0] <= mouseX <= button3_rect[0] + button3_rect[2] and
                  button3_rect[1] <= mouseY <= button3_rect[1] + button3_rect[3]):
                buttonNumber = 3
                print(buttonNumber)
                getStatValues()
            elif (button4_rect[0] <= mouseX <= button4_rect[0] + button4_rect[2] and
                  button4_rect[1] <= mouseY <= button4_rect[1] + button4_rect[3]):
                buttonNumber = 4
                print(buttonNumber)
                getStatValues()
            elif (button5_rect[0] <= mouseX <= button5_rect[0] + button5_rect[2] and
                  button5_rect[1] <= mouseY <= button5_rect[1] + button5_rect[3]):
                buttonNumber = 5
                print(buttonNumber)
                getStatValues()

        if event.type == pygame.MOUSEMOTION:  # sets mouseX and mouseY to where the mouse has moved to
            mouseX, mouseY = event.pos

    # part of code that tells the color of button change to button_over_color if mouse over it
    if (button1_rect[0] <= mouseX <= button1_rect[0] + button1_rect[2] and
            button1_rect[1] <= mouseY <= button1_rect[1] + button1_rect[3]):
        # print("test")
        pygame.draw.rect(win, button_over_color, button1_rect)
    elif (button2_rect[0] <= mouseX <= button2_rect[0] + button2_rect[2] and
          button2_rect[1] <= mouseY <= button2_rect[1] + button2_rect[3]):
        pygame.draw.rect(win, button_over_color, button2_rect)
    elif (button3_rect[0] <= mouseX <= button3_rect[0] + button3_rect[2] and
          button3_rect[1] <= mouseY <= button3_rect[1] + button3_rect[3]):
        pygame.draw.rect(win, button_over_color, button3_rect)
    elif (button4_rect[0] <= mouseX <= button4_rect[0] + button4_rect[2] and
          button4_rect[1] <= mouseY <= button4_rect[1] + button4_rect[3]):
        pygame.draw.rect(win, button_over_color, button4_rect)
    elif (button5_rect[0] <= mouseX <= button5_rect[0] + button5_rect[2] and
          button5_rect[1] <= mouseY <= button5_rect[1] + button5_rect[3]):
        pygame.draw.rect(win, button_over_color, button5_rect)
    elif (button6_rect[0] <= mouseX <= button6_rect[0] + button6_rect[2] and
          button6_rect[1] <= mouseY <= button6_rect[1] + button6_rect[3]):
        pygame.draw.rect(win, button_over_color, button6_rect)
    else:
        # drawing buttons with original color
        pygame.draw.rect(win, button_color, button1_rect)
        pygame.draw.rect(win, button_color, button2_rect)
        pygame.draw.rect(win, button_color, button3_rect)
        pygame.draw.rect(win, button_color, button4_rect)
        pygame.draw.rect(win, button_color, button5_rect)
        pygame.draw.rect(win, button_color, button6_rect)

    # drawing text onto the buttons
    win.blit(button1_text, (button1_rect[0], button1_rect[1]))
    win.blit(button2_text, (button2_rect[0], button2_rect[1]))
    win.blit(button3_text, (button3_rect[0], button3_rect[1]))
    win.blit(button4_text, (button4_rect[0], button4_rect[1]))
    win.blit(button5_text, (button5_rect[0], button5_rect[1]))
    win.blit(button6_text, (button6_rect[0], button6_rect[1]))

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
