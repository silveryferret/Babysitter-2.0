from unittest import TestCase
from pathlib import Path
from src.resources import images
from src.resources.director import Director
from src.resources.gameobjects import GameObject
import pygame

from src.resources.resourcemanager import NoFilePath


class DummyResourceManager(GameObject):
    def load_image(self, path):
        try:
            our_image = pygame.Surface((512, 512))
            return images.Image(our_image, path)
        except pygame.error:
            our_path = Path(path)
            if path == '' or our_path.exists() is False:
                raise NoFilePath
            else:
                raise


class TestDirector(TestCase):

    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1280, 720))

    def test_script_reader(self):
        director = Director(DummyResourceManager())
        test_objs = director.direct_script('Test (Image) 1')
        for gameobj in test_objs:
            self.assertEqual(gameobj.path, '../resources/images/TestImage.png')
            self.assertEqual(gameobj.pos, (0, 0))
