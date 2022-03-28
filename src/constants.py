import pygame


SIZE = 600
WIN = pygame.display.set_mode((SIZE, SIZE))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 30)
TEXTSURFACE = FONT.render('Press Space to Start and C to Clear', False, (0, 0, 0))
