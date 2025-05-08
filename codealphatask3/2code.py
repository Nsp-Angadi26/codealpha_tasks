import pygame
import random
import time

pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Card variables
CARD_SIZE = 100
ROWS, COLS = 4, 4
cards = list(range(8)) * 2  # Two pairs of each card
random.shuffle(cards)
flipped = [False] * 16
first_card = None
start_time = time.time()
time_limit = 60  # 60 seconds to complete the puzzle

def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            index = row * COLS + col
            x, y = col * CARD_SIZE + 50, row * CARD_SIZE + 50
            if flipped[index]:
                pygame.draw.rect(screen, GREEN, (x, y, CARD_SIZE, CARD_SIZE))
                text = font.render(str(cards[index]), True, BLACK)
                screen.blit(text, (x + 35, y + 35))
            else:
                pygame.draw.rect(screen, RED, (x, y, CARD_SIZE, CARD_SIZE))

def check_win():
    return all(flipped)

running = True
while running:
    draw_board()
    elapsed_time = time.time() - start_time
    timer_text = font.render(f"Time Left: {max(0, time_limit - int(elapsed_time))} sec", True, BLACK)
    screen.blit(timer_text, (200, 10))
    
    if check_win() or elapsed_time >= time_limit:
        result_text = font.render("You Win!" if check_win() else "Time's Up!", True, BLACK)
        screen.blit(result_text, (220, 350))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = (x - 50) // CARD_SIZE
            row = (y - 50) // CARD_SIZE
            index = row * COLS + col
            
            if 0 <= index < 16 and not flipped[index]:
                if first_card is None:
                    first_card = index
                else:
                    if cards[first_card] == cards[index]:
                        flipped[first_card] = True
                        flipped[index] = True
                    first_card = None

pygame.quit()