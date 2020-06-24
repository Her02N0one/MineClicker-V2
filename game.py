import pygame
from pygame import freetype


class Game:
    
    def __init__(self):
        self.screen = None
        self.running = False
        self.screen_dimensions = ()
        self.width = 0
        self.height = 0

    def run(self, screen):
        print(self.running)


        pygame.font.init()
        pygame.freetype.init()
        # pygame.mixer.pre_init(44100, -16, 1, 512)
        # pygame.mixer.init()

        self.screen = screen
        self.running = True
        self.width, self.height = self.screen_dimensions = screen.get_size()
        self.start_game_loop()


    def start_game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()