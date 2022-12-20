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
proba = 0
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
# main game img
size = (160, 160)
box1 = pygame.transform.scale(
    pygame.image.load("box1.png").convert_alpha(), size)
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
alfa = pygame.image.load("alfa.png").convert_alpha()
beta = pygame.image.load("beta.png").convert_alpha()
combine = pygame.image.load("hi2.png").convert_alpha()
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
RIGHT = 800 - LEFT * 2
Y = 140
left_boxes_button = []
right_boxes_button = []
central_images = []
# _________________________________________________________________________
# combinations
right1_img = pygame.image.load("right1.png").convert_alpha()
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
        central_images.append(button.Button(
            SCREEN_WIDTH // 2, 150 * i, central[i], 1))
    for i in range(1, 4, 1):
        left_boxes_button.append(button.Button(LEFT, Y * i, left_boxes[i], 1))
        right_boxes_button.append(button.Button(
            RIGHT, Y * i, right_boxes[i], 1))
    screen.fill((200, 200, 200))
    for i in range(0, len(right_boxes_button), 1):
        right_boxes_button[i].draw(screen)
        left_boxes_button[i].draw(screen)
    for i in central_images:
        i.draw(screen)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_audio_settings():
    screen.fill((52, 78, 91))
    screen.blit(volume, (0, 0))


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
            draw_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # event handler
        if menu_state == "game":  # slagame go v nov if zashtoto v straiq ne se izpulnqva
            for i in range(0, 3, 1):
                if(left_boxes_button[i].draw(screen)):
                    central[1] = left_boxes[i + 1]
                    choices.append(i)
                if(right_boxes_button[i].draw(screen)):
                    central[1] = right_boxes[i + 1]
                    choices.append(i + 3)
        if menu_state == "game":
            if(central_images[2].draw(screen)):
                if(len(choices) == 4):
                    choices.sort()
                    if(choices == right_order):
                        central[1] = right[0]
                    else:
                        central[1] = xxx_img
                    choices.clear()
        pygame.display.update()
    pygame.quit()


main_menu()
