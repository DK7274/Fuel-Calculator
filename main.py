import pygame
pygame.init()

run = True

#setting up window#
win =pygame.display.set_mode((500,500))
pygame.display.set_caption("Fuel Calculator")
bgColor = (50, 131, 168)
win.fill(bgColor)
pygame.display.flip()

###main loop###
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
#####
pygame.quit()