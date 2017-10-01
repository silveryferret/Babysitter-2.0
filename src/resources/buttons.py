from src.resources.gameobjects import GameObject


class Button(GameObject):
    def __init__(self, pos, action):
        self.pos = pos
        self.action = action

    def draw(self):
        pass
