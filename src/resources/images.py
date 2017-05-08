from src.resources.gameobjects import GameObject


class Image(GameObject):
    def __init__(self, img):
        self.img = img

    def draw(self, surf, pos):
        surf.blit(self.img, pos)
        return surf
