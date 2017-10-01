from src.resources.gameobjects import GameObject


class Image(GameObject):
    def __init__(self, img, path, pos=(0, 0)):
        self.img = img
        self.pos = pos
        self.path = path

    def position(self, tup):
        self.pos = tup

    def draw(self, surf):
        surf.blit(self.img, self.pos)
