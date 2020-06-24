import pygame


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


class StateStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, state):
        if self.isEmpty() is not True:
            self.top().on_leave()
        self.items.append(state)
        self.top().on_enter()

    def pop(self):
        self.top().on_leave()
        self.items.pop()
        if self.isEmpty() is not True:
            self.top().on_enter()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class State:

    def __init__(self, state_data: dict):
        self.state_data = state_data
        self.screen = state_data["screen"]
        self.states = state_data["states"]

        self.mousePos = pygame.Vector2()
        self.quit = False
        self.target = None

    def get_quit(self):
        return self.quit

    def end_state(self):
        self.quit = True

    def on_enter(self):
        """
        Runs once every time the class enters top of the stack
        """
        pass

    def on_leave(self):
        """
        Runs once every time the class leaves top of the stack
        """
        pass

    def process_events(self, events, pressed_keys):
        assert 0, "update_input not implemented"

    def update(self, dt):
        assert 0, "update not implemented"

    def render(self, target=None):
        assert 0, "render not implemented"


class Player:

    def __init__(self):
        self.inventory = list()
        
        self.tools = {
            "pick": 1,
            "shovel": 0,
            "axe": 0
        }

        self.total_blocks_broken = 0
        self.total_clicks = 0

    def add_item(self, item, amount=1):
        for index, inv_item in enumerate(self.inventory):
            if inv_item[0] == item:
                self.inventory[index][1] += amount
                return
        self.inventory.append([item, 1])

