import util
import game

class ClickerState(util.State):
    def __init___(self, state_data):
        super().__init__(state_data)

    def process_events(self, events, pressed_keys):
        pass

    def update(self, dt):
        print(game.Game.instance().screen_dimensions)
    
    def render(self, target):
        pass
    
