import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Treasure Island")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Load music and sound effects
# pygame.mixer.music.load('background_music.mp3')
# pygame.mixer.music.play(-1)  # Play music on loop
win_sound = pygame.mixer.Sound('win_sound.wav')
lose_sound = pygame.mixer.Sound('lose_sound.wav')


# Game Text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# Game Logic
def check_choice(choice):
    if choice == "left":
        draw_text("You chose Left", small_font, black, screen, screen_width // 2, screen_height // 2 + 50)
        pygame.display.update()
        pygame.time.wait(1000)

        swim_choice = prompt_user("Do you want to Swim or Wait?")
        if swim_choice == "wait":
            door_choice = prompt_user("Which color door? (yellow, blue, red)").lower()
            if door_choice == "yellow":
                result = "You Win!"
                win_sound.play()
            elif door_choice == "blue":
                result = "Eaten by beasts. Game Over!"
                lose_sound.play()
            elif door_choice == "red":
                result = "Burned by fire. Game Over!"
                lose_sound.play()
            else:
                result = "Game Over!"
                lose_sound.play()
        else:
            result = "Attacked by a trout. Game Over!"
            lose_sound.play()
    else:
        result = "Fell in a hole. Game Over!"
        lose_sound.play()

    draw_text(result, font, black, screen, screen_width // 2, screen_height // 2 + 100)
    pygame.display.update()
    pygame.time.wait(3000)


# Simulated user prompt function (press a key to select)
def prompt_user(question):
    screen.fill(white)
    draw_text(question, small_font, black, screen, screen_width // 2, screen_height // 2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Press 'S' for Swim
                    return "swim"
                elif event.key == pygame.K_w:  # Press 'W' for Wait
                    return "wait"
                elif event.key == pygame.K_y:  # Press 'Y' for Yellow
                    return "yellow"
                elif event.key == pygame.K_b:  # Press 'B' for Blue
                    return "blue"
                elif event.key == pygame.K_r:  # Press 'R' for Red
                    return "red"


# Game Loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        draw_text("Welcome to Treasure Island!", font, black, screen, screen_width // 2, screen_height // 4)
        draw_text("Press 'L' for Left or 'R' for Right", small_font, black, screen, screen_width // 2,
                  screen_height // 2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            check_choice("left")
        elif keys[pygame.K_r]:
            check_choice("right")

        pygame.display.update()


game_loop()
