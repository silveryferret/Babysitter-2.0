from src.resources.gameobjects import GameObject


class Image(GameObject):
    def __init__(self, img):
        img.convert_alpha()
        # TODO: Dummy image object that draws to the screen
