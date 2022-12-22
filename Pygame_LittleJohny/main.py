import pygame
import button
pygame.init()
pygame.font.init()
# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)
volume = font.render('volume', False, (255, 255, 255))
# define colors
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("button_resume.png").convert_alpha()
options_img = pygame.image.load("button_options.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
video_img = pygame.image.load('button_video.png').convert_alpha()
audio_img = pygame.image.load('button_audio.png').convert_alpha()
keys_img = pygame.image.load('button_keys.png').convert_alpha()
back_img = pygame.image.load('button_back.png').convert_alpha()
start_img = pygame.image.load('start_btn.png').convert_alpha()
laptop = pygame.image.load('Products\\laptop.svg').convert_alpha()
# main game img
size = (160, 150)
box1 = pygame.transform.scale(
    pygame.image.load("box1.png"), size)
box2 = pygame.transform.scale(
    pygame.image.load("box2.png").convert_alpha(), size)
box3 = pygame.transform.scale(
    pygame.image.load("box3.png").convert_alpha(), size)
left_boxes = [0, box1, box2, box3]
box4 = pygame.transform.scale(
    pygame.image.load("box4.png").convert_alpha(), size)
box5 = pygame.transform.scale(
    pygame.image.load("box5.png").convert_alpha(), size)
box6 = pygame.transform.scale(
    pygame.image.load("box6.png").convert_alpha(), size)
right_boxes = [0, box4, box5, box6]
alfa = pygame.image.load("Boss\\boss_face_up.svg").convert_alpha()
beta = pygame.image.load("Other_pictures\\metal_tray.svg").convert_alpha()
beta_1 = (button.Button(275, 125 * 1, beta, 1))
combine = pygame.transform.scale(pygame.image.load("Other_pictures\\Combine.png").convert_alpha(), (250, 90))
central = [alfa, beta, combine]
# create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
start_button = button.Button(260, 100, start_img, 1)
# create button instances for main_game
LEFT = 50
RIGHT = 700 - LEFT * 2
Y = 100
left_boxes_button = []
right_boxes_button = []
central_images = []
# _________________________________________________________________________
# combinations
right1_img = pygame.image.load("Products\\laptop.svg").convert_alpha()
right2_img = pygame.image.load("right2.png").convert_alpha()
right3_img = pygame.image.load("right3.png").convert_alpha()
right4_img = pygame.image.load("right4.png").convert_alpha()
right5_img = pygame.image.load("right5.png").convert_alpha()
right = [right1_img, right2_img, right3_img, right4_img, right5_img]
xxx_img = pygame.image.load("XXX.png").convert_alpha()
xxx = button.Button(SCREEN_WIDTH, 150, xxx_img, 1)
combinations = []
for i in range(0, 5, 1):
    combinations.append(button.Button(SCREEN_WIDTH // 2, 150, right[i], 1))
right_order = [0, 1, 2, 3]


def draw_game():
    for i in range(0, 3, 1):
        if(i == 0):
            central_images.append(button.Button(330, 150 * i, central[i], 1))
        if(i == 1):
            central_images.append(button.Button(275, 125 * i, central[i], 1))
        if(i == 2):
            central_images.append(button.Button(280, 250 * i, central[i], 1))
    for i in range(1, 4, 1):
        if(i == 1):
            left_boxes_button.append(button.Button(LEFT, 80, left_boxes[i], 1))
            right_boxes_button.append(button.Button(RIGHT, 80, right_boxes[i], 1))
        if(i == 2):
            left_boxes_button.append(button.Button(LEFT, 235, left_boxes[i], 1))
            right_boxes_button.append(button.Button(RIGHT, 235, right_boxes[i], 1))
        if(i == 3):
            left_boxes_button.append(button.Button(LEFT, 380, left_boxes[i], 1))
            right_boxes_button.append(button.Button(RIGHT, 380, right_boxes[i], 1))
    screen.fill((113,106,98))
    for i in range(0, len(right_boxes_button), 1):
        right_boxes_button[i].draw(screen)
        left_boxes_button[i].draw(screen)
    for i in central_images:
        i.draw(screen)

def conv ():
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

    conv = ["Hello, I'm John!", "I'm having trouble with", "finding a manufacturer", "for the product I want.", "Could you help me", "with its development?"]
    conv_1 = ["Hello, I'm Pablo!", "I'm having trouble with", "finding a manufacturer", "for the product I want.", "Could you help me", "with its development?"]

    image_sprite = [pygame.image.load("meeting.svg"), pygame.image.load("meeting_1.svg")]

    clock = pygame.time.Clock()

    black=(0, 0, 0)
    font = pygame.font.Font('freesansbold.ttf', 16)

    value = 0

    run = True
    while run:
    #first 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.blit(background, (0, 0))
        if(flag == 1):
            #this is till  the conversation
            if(count <= 6):
                if value >= len(image_sprite):
                    value = 0
                clock.tick(1)
                image = image_sprite[value]

                window.blit(image, (150, 182))
                printing_text_box(window,text_box)

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

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_audio_settings():
    screen.fill((52, 78, 91))
    screen.blit(volume, (0, 0))

def printing_text_box (window, text_box):
    window.blit(text_box, (760, 105))


def main_menu():
    # game loop
    choices = []
    menu_state = "main"
    run = True
    while run:

        screen.fill((52, 78, 91))
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if start_button.draw(screen):
                menu_state = "game"
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
            # check if the options menu is open
        if menu_state == "options":
            # draw the different options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
                menu_state = "audio"
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
        if menu_state == "audio":
            draw_audio_settings()
        if menu_state == "game":
            conv()
            menu_state = "game_1"
        if menu_state == "game_1":
            draw_game()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # event handler
        if menu_state == "game_1":  # slagame go v nov if zashtoto v straiq ne se izpulnqva
            for i in range(0, 3, 1):
                if(left_boxes_button[i].draw(screen)):
                    central[1] = left_boxes[i + 1]
                    choices.append(i)
                if(right_boxes_button[i].draw(screen)):
                    central[1] = right_boxes[i + 1]
                    choices.append(i + 3)
        if menu_state == "game_1":
            if(central_images[2].draw(screen)):
                if(len(choices) == 4):
                    choices.sort()
                    if(choices == right_order):
                        screen.blit(beta, (275, 125))
                        screen.blit(laptop, (275, 125))
                    else:
                        central[1] = xxx_img
                    choices.clear()
        pygame.display.update()
    pygame.quit()


main_menu()
