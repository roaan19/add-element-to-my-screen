import pygame
import sys

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Rectangle color
BLACK = (0, 0, 0)   # Text color

rect_width, rect_height = 100, 50
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

font = pygame.font.SysFont(None, 36)
text = font.render("Hello, Pygame!", True, BLACK)
text_rect = text.get_rect(center=(screen_width // 2, rect_y - 40))  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, rectangle)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
