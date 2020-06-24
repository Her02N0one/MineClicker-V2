import pygame
from game import Game



if __name__ == '__main__':
    screen_dimensions = (768, 544)
    screen = pygame.display.set_mode(screen_dimensions)
    game = Game()
    game.run(screen)
