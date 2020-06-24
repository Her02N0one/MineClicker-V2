import pygame
import pygame.freetype
import util
import states
import time


small_font = pygame.freetype.SysFont(pygame.font.get_default_font(), 25)
medium_font = pygame.freetype.SysFont(pygame.font.get_default_font(), 50)
large_font = pygame.freetype.SysFont(pygame.font.get_default_font(), 80)

@util.Singleton
class Game:
    
    def __init__(self):
        self.screen = None
        self.running = False
        self.screen_dimensions = ()
        self.width = 0
        self.height = 0
        self.state_stack = util.StateStack()
        

    def run(self, screen):
        self.screen = screen
        self.running = True
        self.width, self.height = self.screen_dimensions = screen.get_size()

        text_surf = small_font.render("Loading...", fgcolor=(0, 0, 0), bgcolor=(255, 255, 255))
        screen.fill((255, 255, 255))
        screen.blit(text_surf[0], ((self.width // 2) - (text_surf[1].width // 2), (self.height // 2) - (text_surf[1].height // 2)))
        pygame.display.flip()

                

        state_data = {"screen": self.screen, "states": self.state_stack}
        self.state_stack.push(states.ClickerState(state_data))

        self.start_game_loop()


    def start_game_loop(self):
        self.screen.fill((255, 255, 255))

        while self.running:
            pressed_keys = pygame.key.get_pressed()
        
            # Event filtering
            filtered_events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_F4 and alt_pressed:
                        self.running = False
                

                filtered_events.append(event)
            
            self.state_stack.top().process_events(filtered_events, pressed_keys)
            self.state_stack.top().update(10)
            self.state_stack.top().render(self.screen)

            pygame.display.flip()

        pygame.quit()