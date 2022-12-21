def printing_text_box ():
    window.blit(text_box, (760, 105))
    


import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((1000, 600))

text_box = pygame.image.load("Other_pictures\\dialog_box.png")
text_box = pygame.transform.scale(text_box, (290,290))
gray_square = pygame.image.load("Other_pictures\\drawing.svg")
gray_square = pygame.transform.scale(gray_square, (1590,1890))
background = pygame.image.load("Other_pictures\\background.svg")
recipes = pygame.image.load("recipes\\computer_recipe.png")
recipes = pygame.transform.scale(recipes, (200,290))

flag = 1
count = 0
transparent = (128, 128, 128)

conv = ["Hello, I'm John!", "I'm having trouble with", "finding a manufacturer", "for the product I want.", "Could you help me", "with its development?"]
conv_1 = ["Hello, I'm Pablo!", "I'm having trouble with", "finding a manufacturer", "for the product I want.", "Could you help me", "with its development?"]

image_sprite = [pygame.image.load("meeting.svg"), pygame.image.load("meeting_1.svg")]

clock = pygame.time.Clock()
clock_1 = pygame.time.Clock()

black=(0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 16)

value = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(background, (0, 0))

#first product
    if(flag == 1):
        #this is till  the conversation
        if(count <= 6):
            if value >= len(image_sprite):
                value = 0
            clock.tick(1)
            image = image_sprite[value]

            window.blit(image, (150, 182))
            printing_text_box()

            pygame.display.update()
            value += 1   
            #this remove the white text box
            if(count == 6):
                count +=1
                window.blit(gray_square, (690, -62))
                window.blit(recipes, (803,100 ))
                pygame.display.update()

        #this renovate the text
        if (count < 6):
            sth = font.render(conv[count], True, black)
            window.blit(sth, (803,227.5))
            pygame.display.update()
            count += 1

    elif(flag == 2):
        if(count <= 6):
            if value >= len(image_sprite):
                value = 0
            clock.tick(1)
            image = image_sprite[value]

            window.blit(image, (150, 182))
            printing_text_box()

            pygame.display.update()
            value += 1
            if(count == 6):
                count +=1
                window.blit(gray_square, (690, -62))
                pygame.display.update()

        if (count < 6):
            sth = font.render(conv_1[count], True, black)
            window.blit(sth, (803,227.5))
            pygame.display.update()
            count += 1
pygame.quit()