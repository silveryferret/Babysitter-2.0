from pathlib import Path
from src.resources import images, sounds, buttons
import pygame


class NoFilePath(Exception):
    def __init__(self):
        self.message = 'Wrong or no file path given.'
        super(NoFilePath, self).__init__(self.message)


class ResourceManager(object):
    def load_image(self, path):
        try:
            our_image = pygame.image.load(path).convert_alpha()
            return images.Image(our_image, path)
        except pygame.error:
            our_path = Path(path)
            if path == '' or our_path.exists() is False:
                raise NoFilePath
            else:
                raise

    def load_button(self, text):
        pass

    def load_sound(self, path):
        try:
            our_sound = pygame.mixer.Sound(path)
            return sounds.Sound(our_sound)
        except pygame.error:
            our_path = Path(path)
            if path == '' or our_path.exists() is False:
                raise NoFilePath
            else:
                raise

