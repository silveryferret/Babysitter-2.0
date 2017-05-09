from unittest import TestCase
from src.resources.director import Director
import pygame


class TestDirector(TestCase):

    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1280, 720))

    def test_script_reader(self):
        director = Director()
        test_objs = director.direct_script('Test (Image) 1')
        for gameobj in test_objs:
            self.assertEqual(gameobj.path, '../resources/images/TestImage.png')
            self.assertEqual(gameobj.pos, (0, 0))
