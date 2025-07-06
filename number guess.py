import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 460, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

try:
    bg = pygame.image.load("background.jpg")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
except:
    bg = None


number = random.randint(1, 100)
attempts = 0
input_text = ''
feedback = "Guess a number between 1 and 100"
game_over = False

def draw_text(text, font, color, surface, x, y):
    txt_obj = font.render(text, True, color)
    txt_rect = txt_obj.get_rect(center=(x, y))
    surface.blit(txt_obj, txt_rect)

def reset_game():
    global number, attempts, input_text, feedback, game_over
    number = random.randint(1, 100)
    attempts = 0
    input_text = ''
    feedback = "Guess a number between 1 and 100"
    game_over = False
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    if bg:
        screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        guess = int(input_text)
                        attempts += 1
                        if guess < number:
                            feedback = "Too low! Try again."
                        elif guess > number:
                            feedback = "Too high! Try again."
                        else:
                            feedback = f"Correct! You guessed it in {attempts} attempts."
                            game_over = True
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    draw_text("Number Guessing Game", big_font, BLACK, screen, WIDTH // 2, 50)
    draw_text(feedback, font, BLACK, screen, WIDTH // 2, 120)

    if not game_over:

        pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 70, 170, 140, 40))
        draw_text(input_text, font, BLACK, screen, WIDTH // 2, 190)
        draw_text("Press Enter to Guess", font, BLACK, screen, WIDTH // 2, 240)
    else:
        draw_text("Press 'R' to play again", font, GREEN, screen, WIDTH // 2, 260)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
